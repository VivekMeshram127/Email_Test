from django.shortcuts import render
from rest_framework import serializers, viewsets
from myApp.models import Employee, Event, EmailTemplate
from datetime import date

from django.shortcuts import render
from myApp.models import Event  # Import your Event model

# def event_list(request):
#     # Query the events from the database, adjust this query as needed
#     events = Event.objects.filter(event_date=date.today())

#     return render(request, "index.html", {'events': events})


def home(request):
    # context={}
    events = Event.objects.filter(event_date=date.today())

    return render(request, "index.html",{'events': events})


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EmailTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = '__all__'

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EmailTemplateViewSet(viewsets.ModelViewSet):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailTemplateSerializer