from celery import Celery
from celery.schedules import crontab

celery = Celery(
    "hms",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

def init_celery(app):
    celery.conf.update(app.config)

    celery.conf.timezone = "Asia/Kolkata"

    celery.conf.beat_schedule = {
        "daily-reminder": {
            "task": "tasks.send_daily_reminders",
            # "schedule": crontab(minute="*/1"),
            "schedule": crontab(hour=8, minute=0),
        },
        "monthly-report": {
            "task": "tasks.send_monthly_doctor_reports",
            "schedule": crontab(day_of_month=1, hour=9, minute=0),
            # "schedule": crontab(minute="*/1"),
        },
    }

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return super().__call__(*args, **kwargs)

    celery.Task = ContextTask