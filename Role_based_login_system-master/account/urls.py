from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('user/', views.customer, name='user'),
    path('employee/', views.employee, name='employee'),
    path('delete/<int:id>/',views.delete,name='admindelete' ),
    path('edit/<int:id>/',views.admin_edit,name='admindelete' ),
    path('update/<int:id>/',views.update,name='update' ),
    path('add/', views.add,name='add'),  

]