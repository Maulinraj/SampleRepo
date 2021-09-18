# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User, auth
# from accounts.forms import RegistrationForm
# from .models import Profile,Repositories
# from django.contrib import messages
# import requests
# import datetime
# # Create your views here.

# def logout(request) :
#     auth.logout(request)
#     return redirect('/')  

# def login(request) :
#     if request.method == 'POST' :
#         password = request.POST['password']
#         username = request.POST['username']

#         user = auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect("/")
#         else:
#             messages.info(request,'invalid credentials')
#             return redirect('login')

#     else:
#         return render(request,'login.html')    

# #-------

# #def register(request):
# #    if request.method =='POST':
# #        form = RegistrationForm(request.POST)
# #        if form.is_valid():
# #            form.save()
# #            return redirect(reverse('accounts:home'))
# #    else:
# #        form = RegistrationForm()
# #
# #        args = {'form': form}
# #        return render(request, 'accounts/reg_form.html', args)

# #------
# def register(request) :

# #    if request.method == 'POST' :
# #        first_name = request.POST['first_name']
# #        last_name = request.POST['last_name']
# #        password1 = request.POST['password1']
# #        password2 = request.POST['password2']
# #        username = request.POST['username']

# 	if request.method =='POST':
#             form = RegistrationForm(request.POST)
#             if form.is_valid():
#             	form.save()
#             	return redirect('register.html')

# 	    username = RegistrationForm.username
# 	    first_name = RegistrationForm.first_name
# 	    last_name = RegistrationForm.last_name
# 	    password1 = RegistrationForm.password1
# 	    password2 = RegistrationForm.password2
        
#         if password1==password2:
#                 if User.objects.filter(username=username).exists():
#                     messages.info(request,'Username Taken')
#                     return redirect('register')
#                 else:   
#                     response = requests.get('https://api.github.com/users/'+username)
#                     default = User.objects.create_user(username=username, password=password1,first_name=first_name,last_name=last_name)
#                     default.save()
#                     user1 = Profile.objects.get(user = default)
#                     user1.followers = response.json()['followers']
#                     user1.update_last = datetime.datetime.now()
#                     user1.save()
#                     repos_json = requests.get('https://api.github.com/users/'+username+'/repos')

#                     for i in range(len(repos_json.json())) :
#                         repo = Repositories()
#                         repo.repo_name = repos_json.json()[i]['name']
#                         repo.repo_star = repos_json.json()[i]['stargazers_count']
#                         repo.username = user1
#                         repo.save()
#                     return redirect('login')
                    

#         else:
#             messages.info(request,'password not matching..')    
#             return redirect('register')
#         return redirect('/')
    
#     else:
#     #return render(request,'register.html')
#         form = RegistrationForm()

#         args = {'form': form}
#         return render(request, 'register.html', args)

# def explore(request) :

#     profile = User.objects.all()

#     return render(request,"explore.html",{'profile' : profile})

# def other_profile(request):

#     if request.method == 'POST' :
#         user_name = request.POST['user_name']
#         User_model = User.objects.get(username = user_name)
#         user_profile =  Profile.objects.get(user = User_model)
#         followers = user_profile.followers
#         last_update = user_profile.update_last
#         Repo = Repositories.objects.filter(username_id = user_profile.id)
#         return render(request,"other_profile.html",{'user_name':user_name,'followers':followers,'last_update':last_update,'Repo':Repo})

# def my_profile(request):
#     if request.method == 'POST' :
#         current_user = request.user
#         response = requests.get('https://api.github.com/users/'+ current_user.username)
#         print(current_user)
#         user1 = Profile.objects.get(user = current_user)
#         user1.followers = response.json()['followers']
#         user1.update_last = datetime.datetime.now()
#         user1.save()
#         repos_json = requests.get('https://api.github.com/users/'+current_user.username+'/repos')
#         repos_set = Repositories.objects.filter(username_id = user1.id)
#         for i in range(len(repos_json.json())) :
#             for j in repos_set :
#                 if j.repo_name ==  repos_json.json()[i]['name'] :
#                     #print(j.repo_name)
#                     #print(repos_json.json()[i]['name'])
#                     #print('bas')
#                     break
#                 else : 
#                     print('bas')
#                     repo = Repositories()
#                     repo.repo_name = repos_json.json()[i]['name']
#                     print(repo.repo_name)
#                     repo.repo_star = repos_json.json()[i]['stargazers_count']
#                     repo.username_id = user1.id
#                     print(user1.user_id)
#                     repo.save()
#                     break
#         return redirect('my_profile')
#     else :
#         User_model = request.user
#         user_profile =  Profile.objects.get(user = User_model)
#         followers = user_profile.followers
#         last_update = user_profile.update_last
#         Repo = Repositories.objects.filter(username_id = user_profile.id)
#         return render(request,"my_profile.html",{'user_name':User_model.username,'followers':followers,'last_update':last_update,'Repo':Repo})

from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import Profile,Repositories
from django.contrib import messages
from accounts.forms import RegistrationForm
import requests
from django.utils import timezone
timezone.localtime()
# Create your views here.
def logout(request) :
    auth.logout(request)
    return redirect('/')  
def login(request) :
    if request.method == 'POST' :
        password = request.POST['password']
        username = request.POST['username']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')    


def register(request) :
    if request.method == 'POST' :
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # password1 = request.POST['password1']
        # password2 = request.POST['password2']
        # username = request.POST['username']

        form = RegistrationForm(request.POST)
        # args1 = {'user':request.user}
        # username = args1['user'].username
        # first_name = args1['user'].first_name
        # last_name = args1['user'].last_name
        # password1 = args1['user'].password1
        # password2 = args1['user'].password2
        if form.is_valid():
            form.save()
        return redirect('login')

        # username = RegistrationForm.username
        # first_name = RegistrationForm.first_name
        # last_name = RegistrationForm.last_name
        # password1 = RegistrationForm.password1
        # password2 = RegistrationForm.password2

        

        # if password1==password2:
        #     if User.objects.filter(username=username).exists():
        #         messages.info(request,'Username Taken')
        #         return redirect('register')
        #     else:   
        #         response = requests.get('https://api.github.com/users/'+username)
        #         default = User.objects.create_user(username=username, password=password1,first_name=request.user.first_name,last_name=last_name)
        #         default.save()
        #         user1 = Profile.objects.get(user = default)
        #         user1.followers = response.json()['followers']
        #         user1.update_last = timezone.localtime()
        #         user1.save()
        #         repos_json = requests.get('https://api.github.com/users/'+username+'/repos')
        #         for i in range(len(repos_json.json())) :
        #             repo = Repositories()
        #             repo.repo_name = repos_json.json()[i]['name']
        #             repo.repo_star = repos_json.json()[i]['stargazers_count']
        #             repo.username = user1
        #             repo.save()
        #         return redirect('login')
                
        # else:
        #     messages.info(request,'password not matching..')    
        #     return redirect('register')
        # return redirect('/')
        
    else:
        #return render(request,'register.html')
        form = RegistrationForm()

        args = {'form': form}
    return render(request, 'register.html', args)
    
def explore(request) :
    profile = User.objects.filter(is_superuser = False)
    return render(request,"explore.html",{'profile' : profile})
def other_profile(request):
    if request.method == 'POST' :
        user_name = request.POST['user_name']
        User_model = User.objects.get(username = user_name)
        user_profile =  Profile.objects.get(user = User_model)
        followers = user_profile.followers
        last_update = user_profile.update_last
        Repo = Repositories.objects.filter(username_id = user_profile.id)
        return render(request,"other_profile.html",{'user_name':user_name,'followers':followers,'last_update':last_update,'Repo':Repo})
def my_profile(request):
    if request.method == 'POST' :
        current_user = request.user
        response = requests.get('https://api.github.com/users/'+ current_user.username)
        print(current_user)
        user1 = Profile.objects.get(user = current_user)
        user1.followers = response.json()['followers']
        user1.update_last = timezone.localtime()
        user1.save()
        Repositories.objects.filter(username_id = user1.id).delete()
        repos_json = requests.get('https://api.github.com/users/'+current_user.username+'/repos')
        for i in range(len(repos_json.json())) :
            repo = Repositories()
            repo.repo_name = repos_json.json()[i]['name']
            repo.repo_star = repos_json.json()[i]['stargazers_count']
            repo.username = user1
            repo.save()
        #return redirect('login')
        """repos_set = Repositories.objects.filter(username_id = user1.id)
        for i in range(len(repos_json.json())) :
            bo = False
            for j in repos_set :
                if j.repo_name ==  repos_json.json()[i]['name'] :
                    #print(j.repo_name)
                    #print(repos_json.json()[i]['name'])
                    #print('bas')
                    bo = True
                    break
            if bo == False :
                print('bas')
                repo = Repositories()
                repo.repo_name = repos_json.json()[i]['name']
                print(repo.repo_name)
                repo.repo_star = repos_json.json()[i]['stargazers_count']
                repo.username_id = user1.id
                print(user1.user_id)
                repo.save()"""
            
        return redirect('my_profile')
    else :
        User_model = request.user
        user_profile =  Profile.objects.get(user = User_model)
        followers = user_profile.followers
        last_update = user_profile.update_last
        Repo = Repositories.objects.filter(username_id = user_profile.id)
        return render(request,"my_profile.html",{'user_name':User_model.username,'followers':followers,'last_update':last_update,'Repo':Repo})