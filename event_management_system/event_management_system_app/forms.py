from django import forms
from .models import Category, Event

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'name', 'category', 'start_date', 'end_date',
            'priority', 'description', 'location', 'organizer'
        ]
