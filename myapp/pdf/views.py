from django.shortcuts import render,redirect
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io
import os
# Create your views here.
def accept(request):
    if request.method=="POST":
       name=request.POST.get("name","")
       phone=request.POST.get("phone","")
       email=request.POST.get("email","")
       school=request.POST.get("school","")
       degree=request.POST.get("degree","")
       university=request.POST.get("university","")
       skill=request.POST.get("skill","")
    #    about_you=request.POST.get("about_you","")
    #    previous_work=request.POST.get("previous_work","")

       profile=Profile(name=name,phone=phone,email=email,school=school,degree=degree,university=university,skill=skill)
       profile.save()
    # return redirect('/accept' )
    return render(request,'accept.html' )

def resume(request, id):

    user_profile=Profile.objects.get(pk=id)
    # template=loader.get_template("resume.html")
    # # html=template.render({'user_profile':user_profile})
    # html={'user_profile':user_profile}
    # return HttpResponse(template.render(html, request), content_type='application/xhtml+xml')
    return render(request,"resume.html",{'user_profile':user_profile})
    # # option={
    # #     'page-size':'Letter',
    # #     'encoding':'UTF-8'
    # #     }
    # # pdf=pdfkit.from_string(html,False,option)
    # # response=HttpResponse(pdf,content_type='application/pdf')
    # # response['Content-Disposition']='attachment'
    # # return response

def list(request): 
    profile=Profile.objects.all()
    return render(request,"list.html",{'profile':profile})

def home(request):
    return render(request,"home.html")
    