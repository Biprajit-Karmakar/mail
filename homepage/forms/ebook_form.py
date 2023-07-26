# from django import forms
# from homepage.models import BookDownloader


# class Book_Download_Form(forms.Form):
#     user_name = forms.CharField(label='Your Name', max_length=100)
#     phone_number = forms.EmailField(label='Your Email')
#     email = forms.CharField(label='Your Message', widget=forms.Textarea)


from django import forms
from homepage.models import BookDownloader

class Book_Download_Form(forms.ModelForm):
    class Meta:
        model = BookDownloader
        fields = ['user_name', 'phone_number', 'email']
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'inputfield', 'type': 'tel', 'placeholder': 'Write your name', 'id': 'phonenumber','autocomplete': 'off'}),
            'phone_number': forms.TextInput(attrs={'class': 'inputfield', 'type': 'tel', 'placeholder': 'Write your phone number', 'id': 'phonenumber','autocomplete': 'off'}),
            'email': forms.TextInput(attrs={'class': 'inputfield', 'type': 'tel', 'placeholder': 'Write your mail', 'id': 'phonenumber','autocomplete': 'off'})
        }