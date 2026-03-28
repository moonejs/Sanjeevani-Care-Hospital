import os
import csv
from celery_app import celery
from models import Patient,Doctor, Appointment
from datetime import datetime,timedelta
from utils.email_utils import send_email



@celery.task(bind=True)
def export_patient_treatments(self, patient_id):

    patient = Patient.query.get(patient_id)

    if not patient:
        return {"status": "error", "message": "Patient not found"}

    os.makedirs("exports", exist_ok=True)

    filename = f"patient_{patient_id}_treatments.csv"
    file_path = os.path.join("exports", filename)

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Patient Name",
            "Doctor Name",
            "Appointment Date",
            "Start Time",
            "Diagnosis",
            "Notes",
            "Medicines"
        ])

        for appointment in patient.appointments:
            writer.writerow([
                patient.name,
                appointment.doctor.name,
                appointment.appointment_date,
                appointment.start_time,
                appointment.treatment.diagnosis if appointment.treatment else "",
                appointment.treatment.notes if appointment.treatment else "",
                appointment.treatment.medicines if appointment.treatment else ""
            ])

    return {
        "status": "completed",
        "filename": filename
    }
    
    
@celery.task
def send_daily_reminders():

    today = datetime.now().date()

    appointments = Appointment.query.filter(
        Appointment.appointment_date == today,
        Appointment.status.in_(["pending", "confirmed"])
    ).all()

    for appointment in appointments:
        patient = appointment.patient

        html = f"""
        <h3>Appointment Reminder</h3>
        <p>Dear {patient.name},</p>
        <p>You have an appointment today at <b>{appointment.start_time}</b>.</p>
        <p>Please visit the hospital on time.</p>
        """

        send_email(
            patient.user.email,
            "Hospital Visit Reminder",
            html
        )

    return "Daily reminders sent"


@celery.task
def send_monthly_doctor_reports():

    today = datetime.now()

   
    first_day_this_month = today.replace(day=1)
    last_day_previous_month = first_day_this_month - timedelta(days=1)

    month = last_day_previous_month.month
    year = last_day_previous_month.year

    doctors = Doctor.query.all()

    for doctor in doctors:

        appointments = Appointment.query.filter(
            Appointment.doctor_id == doctor.id,
            Appointment.status == "completed"
        ).all()

        monthly_appointments = [
            a for a in appointments
            if a.appointment_date.month == month and
               a.appointment_date.year == year
        ]

        total_appointments = len(monthly_appointments)

        html = f"""
        <html>
        <body style="font-family: Arial;">
            <h2 style="color:#2c3e50;">
                Monthly Activity Report
            </h2>

            <p><b>Doctor:</b> Dr. {doctor.name}</p>
            <p><b>Month:</b> {month}-{year}</p>
            <p><b>Total Completed Appointments:</b> {total_appointments}</p>

            <hr>

            <h3>Appointment Details</h3>
            <table border="1" cellpadding="6" cellspacing="0" width="100%">
                <tr style="background-color:#f2f2f2;">
                    <th>Date</th>
                    <th>Patient</th>
                    <th>Diagnosis</th>
                    <th>Medicines</th>
                </tr>
        """

        for a in monthly_appointments:
            if a.treatment:
                html += f"""
                <tr>
                    <td>{a.appointment_date}</td>
                    <td>{a.patient.name}</td>
                    <td>{a.treatment.diagnosis}</td>
                    <td>{a.treatment.medicines}</td>
                </tr>
                """

        html += """
            </table>
        </body>
        </html>
        """

        send_email(
            doctor.user.email,
            "Monthly Activity Report",
            html
        )

    return "Monthly reports sent successfully"


from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os

@celery.task(bind=True)
def generate_appointment_pdf(self, appointment_id):

    appointment = Appointment.query.get(appointment_id)

    if not appointment:
        return {"status": "failed"}

    EXPORT_FOLDER = os.path.join(os.getcwd(), "exports")
    os.makedirs(EXPORT_FOLDER, exist_ok=True)

    filename = f"appointment_{appointment_id}.pdf"
    file_path = os.path.join(EXPORT_FOLDER, filename)

    doc = SimpleDocTemplate(file_path, pagesize=A4,
                            rightMargin=40, leftMargin=40,
                            topMargin=40, bottomMargin=30)

    styles = getSampleStyleSheet()

    
    title_style = ParagraphStyle(
        'title',
        parent=styles['Heading1'],
        alignment=1,
        textColor=colors.white,
        fontSize=18
    )

    section_style = ParagraphStyle(
        'section',
        parent=styles['Heading3'],
        textColor=colors.HexColor("#2E86C1"),
        spaceAfter=10
    )

    normal_style = styles['Normal']

    elements = []

    
    header = Table([["CityCare Hospital - Appointment Bill"]],
                   colWidths=[450])
    header.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#2E86C1")),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 16),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ]))

    elements.append(header)
    elements.append(Spacer(1, 20))

    
    elements.append(Paragraph("Patient Information", section_style))

    details = [
        ["Patient", appointment.patient.name],
        ["Doctor", f"Dr. {appointment.doctor.name}"],
        ["Department", appointment.doctor.department.name if appointment.doctor and appointment.doctor.department else "N/A"],
    ]

    table = Table(details, colWidths=[120, 300])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#F2F4F4")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("PADDING", (0, 0), (-1, -1), 8),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 20))

   
    elements.append(Paragraph("Appointment Details", section_style))

    appt_data = [
        ["Date", "Time", "Status"],
        [str(appointment.appointment_date), str(appointment.start_time), appointment.status.capitalize()],
    ]

    appt_table = Table(appt_data, colWidths=[140, 140, 140])
    appt_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D6EAF8")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("PADDING", (0, 0), (-1, -1), 8),
    ]))

    elements.append(appt_table)
    elements.append(Spacer(1, 20))

    if appointment.treatment:
        elements.append(Paragraph("Treatment Details", section_style))

        elements.append(Paragraph(f"<b>Diagnosis:</b> {appointment.treatment.diagnosis}", normal_style))
        elements.append(Paragraph(f"<b>Notes:</b> {appointment.treatment.notes}", normal_style))
        elements.append(Spacer(1, 20))


    elements.append(Paragraph("Billing Summary", section_style))

    fee = 500

    bill_data = [
        ["Consultation Fee", f"₹{fee}"],
        ["Total Amount", f"₹{fee}"],
    ]

    bill_table = Table(bill_data, colWidths=[300, 120])
    bill_table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, -1), (-1, -1), colors.HexColor("#D5F5E3")),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
        ("PADDING", (0, 0), (-1, -1), 8),
    ]))

    elements.append(bill_table)

   
    elements.append(Spacer(1, 30))
    elements.append(Paragraph(
        "Thank you for visiting CityCare Hospital. Wishing you good health!",
        ParagraphStyle(name="footer", alignment=1, textColor=colors.grey)
    ))

    doc.build(elements)

    return {
        "status": "completed",
        "filename": filename
    }
    
    
@celery.task(bind=True)
def export_all_doctors_csv(self):

    doctors = Doctor.query.all()

    if not doctors:
        return {"status": "error", "message": "No doctors found"}

    os.makedirs("exports", exist_ok=True)

    filename = "all_doctors.csv"
    file_path = os.path.join("exports", filename)

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Name",
            "Specialization",
            "Contact",
            "Age",
            "Gender",
            "Qualification",
            "Experience (Years)",
            "Fee",
            "Department",
            "Blocked"
        ])

        for d in doctors:
            writer.writerow([
                d.name,
                d.specialization,
                d.contact,
                d.age,
                d.gender,
                d.qualification,
                d.experience_years,
                d.consultation_fee,
                d.department.name if d.department else "",
                "Yes" if d.is_blocked else "No"
            ])

    return {
        "status": "completed",
        "filename": filename
    }
    
@celery.task(bind=True)
def generate_doctor_profile_pdf(self, doctor_id):

    import json

    doctor = Doctor.query.get(doctor_id)

    if not doctor:
        return {"status": "failed"}

    EXPORT_FOLDER = os.path.join(os.getcwd(), "exports")
    os.makedirs(EXPORT_FOLDER, exist_ok=True)

    filename = f"doctor_{doctor_id}_profile.pdf"
    file_path = os.path.join(EXPORT_FOLDER, filename)

    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()

    # 🎨 Custom Styles
    title_style = ParagraphStyle(
        'title',
        parent=styles['Heading1'],
        alignment=1,
        textColor=colors.white,
        fontSize=18
    )

    section_title = ParagraphStyle(
        'section',
        parent=styles['Heading3'],
        textColor=colors.HexColor("#2E86C1"),
        spaceAfter=8
    )

    normal = styles["Normal"]

    elements = []

    # 🔷 HEADER
    header = Table([[f"CityCare Hospital"]],
                   colWidths=[450])
    header.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#2E86C1")),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ]))

    elements.append(header)
    elements.append(Spacer(1, 15))

    # 👨‍⚕️ DOCTOR NAME
    elements.append(Paragraph(f"<b>Dr. {doctor.name}</b>", styles["Title"]))
    elements.append(Spacer(1, 10))

    # 🧾 BASIC INFO CARD
    elements.append(Paragraph("Basic Information", section_title))

    data = [
        ["Specialization", doctor.specialization],
        ["Experience", f"{doctor.experience_years} years"],
        ["Consultation Fee", f"₹{doctor.consultation_fee}"],
        ["Department", doctor.department.name if doctor.department else "N/A"],
        ["Room Number", doctor.room_number],
        ["Emergency Available", "Yes" if doctor.emergency_available else "No"],
        ["Contact", doctor.contact],
    ]

    table = Table(data, colWidths=[180, 260])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#F4F6F6")),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#D5DBDB")),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("PADDING", (0, 0), (-1, -1), 8),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 20))

    # 🎓 QUALIFICATIONS (FIXED JSON ISSUE)
    elements.append(Paragraph("Qualifications", section_title))

    qualifications = []

    try:
        if doctor.qualification:
            parsed = json.loads(doctor.qualification)
            for q in parsed:
                qualifications.append(
                    f"{q.get('degree')} - {q.get('institution')} ({q.get('year')})"
                )
    except:
        qualifications.append(doctor.qualification or "N/A")

    for q in qualifications:
        elements.append(Paragraph(f"• {q}", normal))

    elements.append(Spacer(1, 20))

    # 🧠 BIO
    if doctor.bio:
        elements.append(Paragraph("About Doctor", section_title))
        elements.append(Paragraph(doctor.bio, normal))
        elements.append(Spacer(1, 20))

    # 📅 FOOTER
    elements.append(Spacer(1, 30))
    elements.append(Paragraph(
        "Generated by CityCare Hospital Management System",
        ParagraphStyle(name="footer", alignment=1, textColor=colors.grey)
    ))

    doc.build(elements)

    return {
        "status": "completed",
        "filename": filename
    }
    
    
    
@celery.task(bind=True)
def export_all_appointments_csv(self):

    appointments = Appointment.query.all()

    if not appointments:
        return {"status": "error", "message": "No appointments found"}

    os.makedirs("exports", exist_ok=True)

    filename = "all_appointments.csv"
    file_path = os.path.join("exports", filename)

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Appointment ID",
            "Date",
            "Start Time",
            "End Time",
            "Status",
            "Type",
            "Session",

            "Doctor Name",
            "Department",

            "Patient Name",

            "Diagnosis",
            "Notes",
            "Medicines",
            "Follow Up Date"
        ])

        for a in appointments:
            writer.writerow([
                a.id,
                a.appointment_date,
                a.start_time,
                a.end_time,
                a.status,
                a.type,
                a.session,

                a.doctor.name if a.doctor else "",
                a.doctor.department.name if a.doctor and a.doctor.department else "",

                a.patient.name if a.patient else "",

                a.treatment.diagnosis if a.treatment else "",
                a.treatment.notes if a.treatment else "",
                a.treatment.medicines if a.treatment else "",
                a.treatment.follow_up_date if a.treatment and a.treatment.follow_up_date else ""
            ])

    return {
        "status": "completed",
        "filename": filename
    }