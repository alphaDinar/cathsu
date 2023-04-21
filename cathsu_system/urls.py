from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('add_member', views.add_member, name='add_member'),
    path('executive', views.executive, name='executive'),
    path('document', views.document, name='document'),
    path('all_members', views.all_members, name='all_members'),
    path('attendance', views.attendance, name='attendance'),
    path('finance', views.finance, name='finance'),
    path('dashboard', views.dashboard, name='dashboard'),

    path('test', views.test)

]
