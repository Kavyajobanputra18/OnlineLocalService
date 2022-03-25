from django.contrib import admin
from django.urls import path,include
from user import views
from .views import UserLogin,UserSignup,UserLogout
from .views import AddServiceProvider, ViewServiceProvider, DetailServiceProvider,DeleteServiceProvider,UpdateServiceProvider

urlpatterns = [
    path('',views.index, name= 'index'),
    path('contact/',views.contact, name= 'contact'),
    path('category/',views.category, name= 'category'),
    path('listing/',views.listing, name= 'listing'),
    path('login/',UserLogin.as_view(), name= 'login'),
    path('logpout/',UserLogout.as_view(), name= 'logout'),
    path('signup/',UserSignup.as_view(), name= 'register'),
    path('add/',AddServiceProvider.as_view(),name='add_serviceprovider'),
    path('view/',ViewServiceProvider.as_view(),name='view_serviceprovider'),
    path('<int:pk>/view/',DetailServiceProvider.as_view(),name='detail_serviceprovider'),
    path('<int:pk>/delete/',DeleteServiceProvider.as_view(),name='delete_serviceprovider'),
    path('<int:pk>/update/',UpdateServiceProvider.as_view(),name='update_serviceprovider'),
    


]