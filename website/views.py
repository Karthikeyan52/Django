from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import models
from django.contrib import messages


def create(request):
    data = models.Enquiry.object.all()
    context = {'data': data}
    if request.method == 'POST':
        x = models.Enquiry(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            contact=request.POST.get('contact'),
            subject=request.POST.get('subject')
        )
        if x is not None:
            x.save()
    return render(request, 'context.html', context)


def service_off(request):
    return render(request, 'service.html')


def login_user(request):
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
            )
        if user is not None:
            login(request, user=user)
            return redirect('read')
    return render(request, 'login_page.html')


def sample(request):
    context = {}
    return render(request, 'sam.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login_page")
