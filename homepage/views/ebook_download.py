from django.shortcuts import render,redirect
from django.contrib import messages
from qtec_official import settings
from django.core.mail import send_mail, EmailMessage
from homepage.forms.ebook_form import Book_Download_Form

def download_book(request):
    form = Book_Download_Form()
    if request.method == 'POST':
        form = Book_Download_Form(request.POST)
        if form.is_valid():
            form.save()
            to_email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('user_name')
            subject = "Thanks for downloading the book"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [to_email]
            message ="Thanks "+ str(name) + " for downloading the book.\n"+"Click this link to download the book: http://127.0.0.1:8000/static/book/demo.pdf"

            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, "Success")
            return redirect("/e-book",modal_display=True)
    else:
        form = Book_Download_Form()
    
    return render(request, 'homepage/e-book.html', {'form': form})