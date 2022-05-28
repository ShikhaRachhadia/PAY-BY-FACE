from django import forms  
from .models import face_pay  
# Creating a form to add an article.
class NameForm(forms.Form):
   Name = forms.CharField(label='Name2', max_length=100)  
   Password = forms.IntegerField(label='pin')
   class Meta:
    model = face_pay
    fields = ['Name', 'Password']
#-----------instance-of-the-form---------------#
def save(self,*args,**kwargs):
    Profile = self.instance
    Profile.Name = self.cleaned_data["Name"]
    Profile.Password = self.cleaned_data["Password"]
form = NameForm()
  