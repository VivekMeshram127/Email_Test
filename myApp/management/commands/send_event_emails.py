from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from myApp.models import Event, EmailLog, EmailTemplate
from datetime import date
import retrying
import logging



# Create a logger
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Send event-related emails'

    @retrying.retry(stop_max_attempt_number=3, wait_fixed=1000)
    def send_email(self, employee, event_type, email_template):
        subject = f"Happy {event_type}!"
        message = email_template.template.format(employee.first_name)
        from_email = 'vivekmeshram127@gmail.com'
        recipient_list = [employee.email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            logger.info(f"Email sent to {employee.email} for event: {event_type}")
        except Exception as e:
            logger.error(f"Error sending email to {employee.email} for event: {event_type} - {e}")


    def handle(self, *args, **options):
        today = date.today()
        events_today = Event.objects.filter(event_date=today)

        for event in events_today:
            employee = event.employee
            event_type = event.event_type
            try:
                email_template = EmailTemplate.objects.get(event_type=event_type)
                self.send_email(employee, event_type, email_template)
                EmailLog.objects.create(event=event, status="Sent")
            except EmailTemplate.DoesNotExist:
                error_message = f"Email template not found for event: {event_type}"
                EmailLog.objects.create(event=event, status="Failed", error_message=error_message)
                logger.error(error_message)
            except Exception as e:
                error_message = f"Error sending email for event: {event_type} - {e}"
                EmailLog.objects.create(event=event, status="Failed", error_message=error_message)
                logger.error(error_message)
