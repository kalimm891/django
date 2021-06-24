from django.urls import path
from . import views

urlpatterns = [
    path('empform',views.empForm,name='empform'),
    path('addemp',views.addEmp,name='addemp'),
    path('empdetails',views.empDetails,name='empdetails'),
    path('editEmp/<int:id>',views.editEmp,name='editEmp'),
    path('updateEmp/<int:id>',views.updateEmp,name='updateEmp'),
    path('deleteEmp/<int:id>',views.destroy,name='deleteEmp'),
]
 