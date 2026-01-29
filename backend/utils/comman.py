from models import Appointment,Availability

from datetime import datetime

def is_doctor_bookable(doctor, date=None):
    """
    Returns True if doctor can accept bookings on given date (or today).
    """
    if not doctor.profile_completed:
        return False

    check_date = date or datetime.now().date()

    availability = Availability.query.filter_by(
        doctor_id=doctor.id,
        date=check_date,
        online_booking=True
    ).first()

    if not availability:
        return False

    sessions = [
        ("morning", availability.morning_enabled,
         availability.morning_start, availability.morning_end,
         availability.morning_slot_duration, availability.morning_max_patients),

        ("afternoon", availability.afternoon_enabled,
         availability.afternoon_start, availability.afternoon_end,
         availability.afternoon_slot_duration, availability.afternoon_max_patients),

        ("evening", availability.evening_enabled,
         availability.evening_start, availability.evening_end,
         availability.evening_slot_duration, availability.evening_max_patients),
    ]

    for _, enabled, start, end, duration, max_patients in sessions:
        if not enabled or not start or not end:
            continue

        total_slots = int(
            ((datetime.combine(check_date, end)
              - datetime.combine(check_date, start)).seconds / 60) / duration
        )

        booked = Appointment.query.filter(
            Appointment.doctor_id == doctor.id,
            Appointment.appointment_date == check_date,
            Appointment.status.in_(["pending", "confirmed"])
        ).count()

        if booked < total_slots * max_patients:
            return True

    return False
