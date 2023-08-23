from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from myApp.models import Employee



class Command(BaseCommand):
    help = 'Send a test email to a specific employee'

    def handle(self, *args, **options):
        try:
            employee = Employee.objects.get(employee_id='1') 
        except Employee.DoesNotExist:
            self.stdout.write(self.style.ERROR('Employee not found'))
            return

        subject = 'Test Email Subject'
        message = 'This is a test email. If you receive this, your email functionality is working.'
        from_email = 'vivek_meshram12@outlook.com'
        recipient_list = [employee.email]

        send_mail(subject, message, from_email, recipient_list)

        self.stdout.write(self.style.SUCCESS(f'Test email sent to {employee.first_name} {employee.last_name}'))
