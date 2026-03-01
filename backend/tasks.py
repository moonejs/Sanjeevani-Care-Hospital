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
            if appointment.treatment:
                writer.writerow([
                    patient.name,
                    appointment.doctor.name,
                    appointment.appointment_date,
                    appointment.start_time,
                    appointment.treatment.diagnosis,
                    appointment.treatment.notes,
                    appointment.treatment.medicines
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