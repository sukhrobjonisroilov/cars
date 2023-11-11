import random

from django.shortcuts import redirect, render


def permission_check(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('sign-in')
        if not request.user.is_staff or not request.user.is_superuser:
            return render(request, 'base.html', {'error': 404})
        if request.user.user_type != 1:
            return render(request, 'base.html', {'error': 404})

        return func(*args, **kwargs)

    return wrapper


def card_mask(number):
    number = number.replace(' ', '')
    return f'{number[:4]} **** **** {number[-4:]}'


def generate_number():
    return '5614 ' + ' '.join(str(random.randint(1000, 9999)) for x in range(4))


def created_un_number():
    numbers = generate_number()
    with open('card_number.txt', 'r') as file:
        if not numbers in file.read().split("\n"):
            with open('card_number.txt', 'w') as write_file:
                write_file.write(f"{numbers}\n")
            return numbers

    return created_un_number()


def admin_permission_check(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('sign-in')

        if request.user.user_type != 1:
            return render(request, 'base.html', {'error': 404})

        return func(*args, **kwargs)

    return wrapper