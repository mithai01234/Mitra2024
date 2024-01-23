from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from videoupload.models import Video
from .models import Report
from .serializers import ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

@login_required(login_url='backend/login')
def report(request):
    catagoryapp=Report.objects.all()


    context={
        'banform': catagoryapp,
    }
    return render(request,'backend/reportlist.html',context)
@login_required(login_url='backend/login')
def activate_catagory(request, catagory_id):
    video = get_object_or_404(Video, id=catagory_id)
    video.status = True
    video.save()
    return redirect('reportlist')  # Redirect to your video list view
@login_required(login_url='backend/login')
def deactivate_catagory(request, catagory_id):
    video = get_object_or_404(Video, id=catagory_id)
    video.status = False
    video.save()
    return redirect('reportlist')  # Redirect to your video list view
# Create your views here.

@login_required(login_url='backend/login')
def delete_item(request, myid):
    report=Report.objects.get(id=myid)
    report.delete()
    return redirect('reportlist')
@login_required(login_url='backend/login')
def view_item(request, myid):
    sel_regform = Report.objects.get(id=myid)

    context = {

        'sel_regform': sel_regform,


    }
    return render(request, 'backend/reportview.html', context)
