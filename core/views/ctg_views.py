from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.models.cars import Brand
from core.form.forms import BrendForm

@login_required(login_url='login')
def ctg_view(request, key, status=None):
    try:
        Model = {
            'brend': Brand
        }[key]
    except:
        redirect('home')
    brand = Model.objects.all()
    ctx = {'brand_all': brand}

    if status == 'form':
        roots = None
        form = eval(f"{key.capitalize()}Form")(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('ctg', key)
        ctx.update({'form': form, 'status': status})

    return render(request, 'category/ctg.html', ctx)
