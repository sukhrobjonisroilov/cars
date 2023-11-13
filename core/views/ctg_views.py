from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.models.cars import Brand, Car
from  core.models.auth import User
from core.form.forms import BrendForm,CarForm,UserForm
from core.service.service import get_brend,get_car
@login_required(login_url='login')
def ctg_view(request, key, status=None):
    try:
        Model = {
            'brend': Brand,
            'car':Car,
            'user':User
        }[key]
    except:
        redirect('home')
    brand = Model.objects.all().order_by('-id')
    total_second = Model.objects.count()
    print(total_second)

    ctx = {'brand_all': brand[:4],
           'total_second':total_second}

    if status == 'form':

        form = eval(f"{key.capitalize()}Form")(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('ctg',key= key,status=status)
        ctx.update({'form': form, 'status': status})


    return render(request, f'category/{key}.html', ctx)


