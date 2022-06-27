from django.shortcuts import render, redirect
from .forms import LoginForm, StudentProfileForm, EmployeeProfileForm, Person, Student, Employee
from .models import Message
from datetime import date
from django.http import HttpResponse
from django import forms


def register(request):
    if len(request.POST) > 0 and 'profileType' in request.POST:
        studentForm = StudentProfileForm(prefix="st")
        employeeForm = EmployeeProfileForm(prefix="em")
        if request.GET['profileType'] == 'student':
            studentForm = StudentProfileForm(request.POST, prefix="st")
            if studentForm.is_valid():
                studentForm.save()
                return redirect('login')

        elif request.POST['profileType'] == 'employee':
            employeeForm = EmployeeProfileForm(request.GET, prefix="em")
            if employeeForm.is_valid():
                employeeForm.save()
            return redirect('login')
            # Le formulaire envoyé n’est pas valide
        return render(request, 'appliweb/user_profile.html', {'studentForm': studentForm, 'employeeForm': employeeForm})
    else:
        studentForm = StudentProfileForm(prefix="st")
        employeeForm = EmployeeProfileForm(prefix="em")
        return render(request, 'appliweb/user_profile.html', {'studentForm': studentForm, 'employeeForm': employeeForm})


def login(request):
    # Teste si le formulaire a été envoyé
    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            logged_user = Person.objects.get(email=user_email)
            request.session['logged_user_id'] = logged_user.id
            return redirect('welcome')
        else:
            return render(request, 'appliweb/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'appliweb/login.html', {'form': form})


def welcome(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        if 'newMessage' in request.POST and request.POST['newMessage'] != '':
            newMessage = Message(author=logged_user, content=request.POST['newMessage'], publication_date=date.today())
            newMessage.save()

        friendMessages = Message.objects.filter(author__friends=logged_user).order_by('-publication_date')

        return render(request, 'appliweb/welcome.html', {'logged_user': logged_user, 'friendMessages': friendMessages})
    else:
        return redirect('login')


def get_logged_user_from_request(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        # On cherche un etudiant
        if len(Student.objects.filter(id=logged_user_id)) == 1:
            return Student.objects.get(id=logged_user_id)
            # On cherche un Employe
        elif len(Employee.objects.filter(id=logged_user_id)) == 1:
            return Employee.objects.get(id=logged_user_id)
            # Si on n’a rien trouve
        else:
            return None
    else:
        return None


def show_profile(request):
    # Vérification que l'utilisateur est authentifié
    logged_user = get_logged_user_from_request(request)
    #
    if logged_user:
        if 'User' in request.POST and request.POST['User'] != '':
            #
            User_id = int(request.POST['User'])
            #
            donnees = Person.objects.filter(id=User_id)

            if len(donnees) == 1:
                return render(request, 'webapp/show_profile.html', {'User': User})

            else:
                return render(request, 'webapp/show_profile.html', {'User': logged_user})

        else:
            return render(request, 'webapp/show_profile.html', {'User': logged_user})

    else:
        return redirect('login')


def add_friend(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        # Teste si le formulaire a été envoyé
        if len(request.GET) > 0:
            form = AddFriendForm(request.GET)
            if form.is_valid():
                new_friend_email = form.cleaned_data['email']
                newFriend = Person.objects.get(email=new_friend_email)
                logged_user.friends.add(newFriend)
                logged_user.save()
                return redirect('welcome')

            else:
                return render(request, 'add_friend.html', {'form': form})
            # Le formulaire n’a pas été envoyé
        else:
            form = AddFriendForm()
            return render(request, 'add_friend.html', {'form': form})
    else:
        return redirect('login')


def modify_profile(request):
    # Vérification que l'utilisateur est authentifié
    logged_user = get_logged_user_from_request(request)
    #
    if logged_user:
        #
        if len(request.POST) > 0:
            #
            if type(logged_user) == Student:
                #
                form = StudentProfileForm(request.POST, instance=logged_user)
            else:
                form = EmployeeProfileForm(request.POST, instance=logged_user)
            if form.is_valid:
                form.save()
                return redirect('welcome')
            else:
                return render(request, 'webapp/modify_profile.html', {'form': form})
        else:
            if type(logged_user) == Student:
                form = StudentProfileForm(instance=logged_user)
            else:
                form = EmployeeProfileForm(instance=logged_user)
            return render(request, 'webapp/modify_profile.html', {'form': form})
    else:
        return redirect('login')



def ajax_check_email_field(request):
    """Cette vue vérifie qu’une adresse de courriel passée en paramètre est valide et qu’elle
n’est pas déjà prise par un autre utilisateur."""

    html_to_return = ''
    if 'value' in request.POST:
        field = forms.EmailField()
        try:
            field.clean(request.GET['value'])
        except forms.ValidationError as ve:
            html_to_return = '<ul class="errorlist">'
            for message in ve.messages:
                html_to_return += '<li>' + message + '</li>'
            html_to_return += '</ul>'

        if len(html_to_return) == 0:
            if len(Person.objects.filter(email=request.GET['value'])) >= 1:
                html_to_return = '<ul class=”errorlist”>'
                html_to_return += '<li>Cette adresse est déjà utilisée!</li>'
                html_to_return += '</ul>'
        return HttpResponse(html_to_return)


def ajax_add_friend(request):
    html_to_return = ''
    logged_user = get_logged_user_from_request(request)
    if logged_user is not None:
        if 'email' in request.GET:
            new_friend_email = request.GET['email']
            if len(Person.objects.filter(email=new_friend_email)) == 1:
                new_friend = Person.objects.get(email=new_friend_email)
                logged_user.friends.add(new_friend)
                logged_user.save()

                html_to_return = '<li><a href="showProfile?userToShow='
                html_to_return += str(new_friend.id)
                html_to_return += '">'
                html_to_return += new_friend.first_name + ' ' + new_friend.last_name
                html_to_return += '</a></li>'

    return HttpResponse(html_to_return)
