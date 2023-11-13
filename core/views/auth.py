from django.contrib.auth import login

from core.models.auth import User


from django.shortcuts import redirect,render
def sing_in(request):

    if request.POST:
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        user = User.objects.filter(phone=phone).first()
        if not user:
            return render(request,'auth/login.html',{'error':'Password yoki Parol xato'})
        if not  user.check_password(password):
            return render(request, 'auth/login.html', {'error': 'Password yoki Parol xato'})
        login(request,user)
        return redirect('home')

    return render(request,'auth/login.html')
