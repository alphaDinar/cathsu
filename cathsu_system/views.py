from django.shortcuts import render,redirect
from .models import Member
from .models import Attendance
from django.utils import timezone

# Create your views here.
def login(request):
    return render(request, 'login.html' )

def add_member(request):
    if request.method == 'POST':
        member = Member()
        member.pro_pic = request.FILES.get('pro_pic')
        member.first_name = request.POST.get('first_name')
        member.last_name = request.POST.get('last_name')
        member.dob = request.POST.get('dob')
        member.gender = request.POST.get('gender')
        member.marital_status = request.POST.get('marital_status')
        member.home_address = request.POST.get('home_address')
        member.res_address = request.POST.get('res_address')
        member.contact = request.POST.get('contact')
        member.email = request.POST.get('email')
        member.cur_level = request.POST.get('cur_level')
        member.institution = request.POST.get('institution')
        member.baptism = request.POST.get('baptism')
        member.confirmation = request.POST.get('confirmation')
        member.position = request.POST.get('position')
        member.year = request.POST.get('year')
        member.save()
        return redirect('all_members')
    return render(request, 'add_member.html' )

def all_members(request):
    att = Attendance.objects.last()
    # for li in att.list:

    members = Member.objects.all()
    context = {
        'members' : members
    }
    return render(request, 'all_members.html', context )

def executive(request):
    return render(request, 'executive.html' )

def document(request):
    return render(request, 'document.html')

def attendance(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        csrf_token = post_data.pop('csrfmiddlewaretoken', None)
        att_box = []
        for key, value in post_data.items():
            if value == 'present':
                status = {
                    'member' : f"{Member.objects.get(id=key).first_name} {Member.objects.get(id=key).last_name}",
                    'status' : 'present',
                    'image_url' : Member.objects.get(id=key).pro_pic.url
                }
                att_box.append(status)
            else:
                status = {
                    'member' : f"{Member.objects.get(id=key).first_name} {Member.objects.get(id=key).last_name}",
                    'status' : 'absent',
                    'image_url' : Member.objects.get(id=key).pro_pic.url
                }
                att_box.append(status)
        print(att_box)
        attendance = Attendance()
        attendance.list = att_box
        attendance.save()
        return redirect('attendance_records')
    members = Member.objects.all()
    context = {
        'members' : members,
        'time' : timezone.now()
    }
    return render(request, 'attendance.html', context )

def attendance_records(request):
    attendance = Attendance.objects.last()

    context ={
        'attendance' :  Attendance.objects.last()
    }
    return render(request, 'attendance_records.html', context )

def finance(request):
    return render(request, 'finance.html' )


def dashboard(request):
    return render(request, 'dashboard.html' )




def test(request):
    user_username = request.POST.get('username')
    user_password = request.POST.get('pass1')
    user = authenticate(username=user_username, password=user_password)
    login(request, user)
    return render(request, 'test.html')