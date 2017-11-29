from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.utils import timezone
from .models import Submit
from .forms import UserForm
from django.contrib.auth.views import logout

# Create your views here.
def post_list(request):
    if request.user.is_authenticated():
        submits = Submit.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'submission/post_list.html',{'submits':submits})
    else:
        return redirect('/login')

    
    
class UserFormView(View):#register
    form_class = UserForm
    template_name = 'submission/register.html'
    
    def get(self,request):
        if request.user.is_authenticated():
            submits = Submit.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'submission/post_list.html',{'submits':submits})
        else:
            form = self.form_class(None)
            return render(request, self.template_name,{'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        
        if form.is_valid():     
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            user = authenticate(username=username, password=password)
            if user is not None:
                
                if user.is_active:
                     login(request, user)
                     submits = Submit.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
                     return render(request, 'submission/post_list.html',{'submits':submits})

                 
        return render(request, self.template_name,{'form':form})
    
#def logout_page(request, *args, **kwargs):
#    logout(request, *args, **kwargs)
                    
                    
                    
                    
    
    