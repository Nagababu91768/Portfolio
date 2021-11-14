from django.shortcuts import render,redirect
from .models import Download_Resume,About_Us,Team,Work_history,Project,Certifictions,LinkedIn,Youtube,Github,Stack,Resume,Education_data
from .forms import contact_form
from django.core.mail import BadHeaderError,send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def home(request):
    # profile = Profile_About.objects.get(id=1)
    # all_jobs = Projects1.objects.all()
    # return render(request,'profile/home1.html',{"profile":profile,"all_jobs":all_jobs})
    down_resume=Download_Resume.objects.get(id=1)
    education=Education_data.objects.all()
    resume=Resume.objects.all()
    team_data=Team.objects.all()
    work_data=Work_history.objects.all()
    about_us=About_Us.objects.get(id=1)
    project=Project.objects.all()
    certifications=Certifictions.objects.all()
    projects=Project.objects.all()
    form = contact_form()
    return render(request, 'profile/home1.html',{"projects":projects,"down_resume":down_resume,"education":education,"resume":resume,"contact_form":form,"team_data":team_data,"work_data":work_data,"about_us":about_us,"project":project,"certifications":certifications})




def home1(request):
    if request.method=="POST":
        filled_form=contact_form(request.POST)
        if filled_form.is_valid():
            filled_full_name=filled_form.cleaned_data["full_name"]
            filled_email=filled_form.cleaned_data["email"]
            filled_subject=filled_form.cleaned_data["subject"]
            filled_message=filled_form.cleaned_data["message"]
            filled_form.save()
            from_email_user="nagababuupputuri@gmail.com"
            receiver="nagababuupputuri@gmail.com"
            subject="Your Portfolio subject +' ' +{}".format(filled_subject)
            website_messages="You are Received mail from {} with this {} sent by {}  information was  {}".format(filled_email,filled_subject,filled_full_name,filled_message)
            try:
                status=send_mail(subject,website_messages,from_email_user,[receiver])
                messages.success(request,"Your request Stored , will reach you asap")
                return redirect("home")
            except Exception:
                messages.warning(request,"form invalid, please check once")



def linkedin(request):
    link_data=LinkedIn.objects.get(id=1)
    # return  render(request,"profile/home1.html",{"linkedin_data":link_data})
    return redirect(link_data.linkedin)

    # return redirect(link_data.linkedin)
def github(request):
    git_data = Github.objects.get(id=1)
    return redirect(git_data.github)
    # return render(request,"profile/home1.html",{"git_data":git_data})
def youtube(request):
     you_data = Youtube.objects.get(id=1)
     return  redirect(you_data.youtube)
     # return  render(request,'profile/home1.html',{"resume_data":resume_data})


def stack(request):
    stack_data = Stack.objects.get(id=1)
    return  redirect(stack_data.stack)
    # return render(request, 'profile/home1.html', {"stack_data": stack_data})

# this is opitional function for send mails using django
# def Mail(request):
#     # profile = Profile_About.objects.get(id=1)
#     if request.method=="POST":
#         filled_form=sample_mail_form(request.POST)
#         if filled_form.is_valid(): # check if form valid or not
#             filled_form.save()
#             sen_email=filled_form.cleaned_data["email"]
#             mail_header=filled_form.cleaned_data["subject"]
#             mail_body=filled_form.cleaned_data["body"]
#             fr_mail=request.POST["email"]
#             message=request.POST["body"]
#             subject=request.POST["header"]
#             print(fr_mail)
#             print(message)
#             print(subject)
#             if fr_mail and message and subject:
#                 try:
#                     send_mail(subject,message,fr_mail,['nagababuupputuri@gmail.com'])
#                     mail_st="Mail send to "
#                 except BadHeaderError:
#                     return HttpResponse('Invalid header found.')
#             else:
#                 return HttpResponse("Please Check All Fileds Thank you")
#
#             form=sample_mail_form()
#             note="Mail Sent Thank you"
#             return render(request,'profile/mail.html',{"form":form,"status":note,"mail_st":mail_st})
#         else:
#             note="Mail sent failed"
#             form=sample_mail_form()
#             return render(request,"profile/mail.html",{"form":form,"status":note})
#     else:
#         form=sample_mail_form()
#         return render(request, "profile/mail.html",{"form":form})
#
# def Project_details1(request,pro_id):
#     # pro=Projects1.objects.get(id=pro_id)
#     return render(request,"profile/prodetails.html",)
