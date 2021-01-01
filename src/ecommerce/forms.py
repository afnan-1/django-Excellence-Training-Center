from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
	fullname = forms.CharField(
		widget=forms.TextInput(
			attrs={
			"class": "form-control", 
			"placeholder": "Your Full name"
			}
			)
		)

	email = forms.EmailField(
		widget=forms.EmailInput(
			attrs={
			"class": "form-control","placeholder": "your Email"
			}
			))

	content = forms.CharField(
		widget=forms.Textarea(
			attrs={
			"class": "form-control","placeholder": "your message"
			}
			))

	# def clean_email(self):
	# 	email = self.cleaned_data.get("email")
	# 	if not "gmail.com" in email:
	# 			raise forms.ValidationError("Email has to be a gmail.com")
	# 	return email





class LoginForm(forms.Form):
		username = forms.CharField()
		password = forms.CharField(widget=forms.PasswordInput)



class RegisterForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label='confirm your password', widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username = username)
		if qs.exists():
			raise forms.ValidationError("i think username exists bro")
		return username


	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email = email)
		if qs.exists():
			raise forms.ValidationError("i think email exists bro")
		return email


	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')

		if password2 != password:
			raise forms.ValidationError("Please check your passwords as they are not the same")
		return data