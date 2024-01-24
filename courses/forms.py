from django import forms
from django.core.exceptions import ValidationError
from .models import Course, Description, Comment
from django.utils import timezone
import re

COURSE_NAME_REGEX = re.compile(r'^[A-Za-z0-9 ]+$')

# To dos:
    # add form validation for all

class FormCourse(forms.ModelForm):
    created_at = forms.DateField(
        widget=forms.DateInput(attrs={'type' : 'date'}), 
        required=False
    )

    class Meta:
        model = Course
        fields = "__all__"
        labels = {
            'name' : 'Course Name',
            'created_at' : 'Start Date'
        }
    


    """
    Validation for course name
    """
    def clean_name(self):
        name = self.cleaned_data.get('name', '')

        if len(name) < 5:
            raise ValidationError('Course name must be at least 5 characters')
        if not re.match(COURSE_NAME_REGEX, name):
            raise ValidationError('Course name must not have special characters')
        
        return name
    
    def clean_created_at(self):
        created_at = self.cleaned_data.get('created_at')
        
        if created_at and created_at < timezone.now().date():
            raise ValidationError('Date cannot be in the past')
        
        return created_at




class FormDescription(forms.ModelForm):
    class Meta:
        model = Description
        fields = ['content']
        labels = {
            'content' : 'Description'
        }

    """
    Validation for description, can be empty or must be more than 5 characters
    """
    def clean_content(self):
        content = self.cleaned_data.get('content', '')
        if len(content) < 15 and len(content) > 0:
            raise ValidationError('Description must be at least 15 characters')
        
        return content

class FormComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : 'Comment'
        }

