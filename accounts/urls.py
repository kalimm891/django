from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('signuppage',views.signupPage,name="signuppage"),
    path('signinpage',views.signinPage,name="signinpage"),
    path('signup',views.signUp,name='signup'),
    path('signin',views.signIn,name='signin'),
    path('logout',views.signOut,name='logout'),
    path('userhome',views.userHome,name='userhome'),
]
