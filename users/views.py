"""
    This document is build up on different view types.
    1: Shared Views
    2: Staff Views
    3: Customer Views

    WORK WITH STAFF VIEWS:

    GENERAL: When we work with user types, we need to inherit necessary Class from .decorators

    a) @method_decorator([login_required, staff_required], name='dispatch')
    - The above code is used above customer related Class
    b) @login_required
    @staff_required
    - The above code is used above customer related Def

    WORK WITH CUSTOMER VIEWS:

    a) @method_decorator([login_required, customer_required], name='dispatch')
    - The above code is used above customer related Class
    b) @login_required
    @customer_required
    - The above code is used above customer related Def
"""
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .forms import CustomerSignUpForm
from .models import User


class CustomerRegisterView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(request, 'You\'ve been signed up')
        return redirect('webshop:shop-home')


def users_login(request):
    context = {
        'title': 'Login',
        'bodyClass': 'productCLogin',
    }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'You\'ve been logged out')
    return redirect('users:login')
