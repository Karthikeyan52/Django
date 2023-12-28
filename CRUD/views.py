from django.shortcuts import render, redirect
from website import models


def read(request):
    data = models.Enquiry.object.all()
    context = {'data': data}
    return render(request, 'read.html', context)


def update(request, pk):
    data = models.Enquiry.object.get(pk=pk)
    context = {'data': data}
    if request.method == "POST":
        data.name = request.POST.get("name")
        data.email = request.POST.get("email")
        data.contact = request.POST.get("contact")
        data.subject = request.POST.get("subject")
        data.status = request.POST.get("status")
        data.comment = request.POST.get("comment")
        if data is not None:
            data.save()
            return redirect('read')
    return render(request, 'update.html', context)


def delete(request, pk):
    data = models.Enquiry.object.get(pk=pk)
    data.delete()
    return redirect('read')
