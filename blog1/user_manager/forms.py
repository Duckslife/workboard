from django import forms

class join_form(forms.Form):
    
    id = forms.CharField(label="ID", max_length=12)
   
    password = forms.CharField(label= "PASSWORD", 
                               max_length= 12,
                               min_length= 6,
                               required= True,
                               widget= forms.PasswordInput)
    
    
    password_check = forms.CharField(label= "PASSWORD(check)", 
                                     max_length= 12,
                                     min_length= 6,
                                     required= True,
                                     widget= forms.PasswordInput)


    

class LoginForm(forms.Form):
    
    id = forms.CharField(label="ID", max_length=12)
   
    password = forms.CharField(label="PASSWORD", max_length=12)

 
