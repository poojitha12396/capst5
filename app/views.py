from django.shortcuts import render,redirect
from django.core.mail import send_mail
import random
# Create your views here.
def login_view(request):
    if request.method=="POST":
        email=request.POST.get('email')
        otp=str(random.randint(1000,9999))
        request.session['email']=email
        request.session['otp']=otp
        send_mail(
            'Your otp code',
            f'Your otp is:{otp}',
            'poojithayallavula310@gmail.com',
            [email],
        )
        return redirect('verify_otp')
    return render(request,'app/login.html')
def verify_otp(request):
    if request.method == 'POST':
        user_otp=request.POST.get('user_otp')
        session_otp=request.session.get('otp')
        if user_otp == session_otp:
            return render(request,'app/success.html')
        else:
            return render(request,'app/failure.html')
    return render(request,'app/verify_otp.html')