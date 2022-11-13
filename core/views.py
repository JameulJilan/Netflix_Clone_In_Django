from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:profile_list')            
        return render(request=request,template_name='index.html')

@method_decorator(login_required,name='dispatch')
class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()
        return render(request=request,template_name='profileList.html',context={
            'profiles':profiles
        })

class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        return render(request=request,template_name='profileCreate.html')



