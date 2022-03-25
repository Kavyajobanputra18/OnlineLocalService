from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import ListView, DetailView
from .models import Customer,ServiceProvider

# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def category(request):
    return render(request, 'user/category.html')

def contact(request):
    return render(request, 'user/contact.html')

def listing(request):
    return render(request, 'user/listing.html')

class UserLogin(LoginView):
    template_name = 'user/login.html'

class UserLogout(LogoutView):
    pass

class UserSignup(CreateView):
    model = Customer
    fields = ['username','password','email']
    template_name = 'user/signup.html'
    success_url = '/user/'

class AddServiceProvider(CreateView):
    model = ServiceProvider
    fields = ['name','address','email','phone','website','description']
    template_name = 'user/add_serviceprovider.html'
    success_url = '/user/view'

class ViewServiceProvider(ListView):
    model = ServiceProvider
    serviceproviders = model.objects.all()
    context_object_name = 'serviceproviders'
    template_name = 'user/view_serviceprovider.html'

class DetailServiceProvider(DetailView):
    model = ServiceProvider
    context_object_name = 'serviceprovider'
    template_name = 'user/detail_serviceprovider.html'

class DeleteServiceProvider(DeleteView):
    model = ServiceProvider
    template_name = "user/delete.html"
    success_url = '/user/view'


class UpdateServiceProvider(UpdateView):
    model = ServiceProvider
    fields = ['name', 'address', 'email', 'phone', 'website', 'description']
    template_name = 'user/update_serviceprovider.html'
    success_url = '/user/view'