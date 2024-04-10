from django import forms

class TodoListForm(forms.Form):
    text=forms.CharField(max_length=1000,
                         widget=forms.TextInput(
                             attrs={'class':'form-control','placeholder':'any new tasks???','aria-label':'Todo','aria-describeby':'add-btn'}
                         )   )                     