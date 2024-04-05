from django import forms
from my_to_do_list_app.models import ToDoList

# I have creted ModelForm to act as HTML form fields for perform CRUD operation on frontend side

class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ('title', 'descripton')
        error_messages = {
            'title':{'required':'You must have to fill title'},
            'descripton':{'required':'Description of To Do is compulsory'
            }
        }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Enter Title of To Do List'}),
            'descripton':forms.Textarea(attrs={'class':'form-control', 'required':True, 'placeholder':'Enter Description of To Do List', 'rows':5}),
            'created_at':forms.TextInput(attrs={'class':'form-control', 'readonly':True})
        }