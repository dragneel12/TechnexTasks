from django import forms

class SignupForm(forms.Form):
    login_widget = forms.TextInput(attrs={'placeholder':
                                          'First Name',
                                          'autofocus': 'autofocus',
                                          'class':'form-control'})
    first_name = forms.CharField(max_length=30,widget=login_widget)
    last_name = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control'}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
