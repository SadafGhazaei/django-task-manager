from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status','priority','due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter task title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Enter task description'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'priority': forms.Select(choices=Task.PRIORITY_CHOICES),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        if not self.instance.pk: 
            self.fields['status'].initial = 'todo'