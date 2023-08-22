from django import forms 
from.models import LoginRecord,SignupRecord,MembersRecord


class loginform(forms.ModelForm): 
    class Meta:
        model=LoginRecord
        fields='__all__'
        
        
class signupform(forms.ModelForm): 
    class Meta:
        model=SignupRecord
        fields='__all__'
              
              
class memberform(forms.ModelForm): 
    class Meta:
        model=MembersRecord
        fields='__all__'
              