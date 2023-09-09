from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_id})" 

class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20)
    event_date = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.event_type} on {self.event_date}"

class EmailLog(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    sent_datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.event.event_type} Email Log - {self.sent_datetime}"


class EmailTemplate(models.Model):
    event_type = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    template = models.TextField()

    def __str__(self):
        return f"{self.event_type} Template"


    