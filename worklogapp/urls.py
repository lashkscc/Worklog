from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('todo',views.todo, name='todo'),
    path('inprogress',views.inprogress, name='inprogress'),
    path('done',views.done, name='done'),
    path('task/<int:id>',views.task, name='task'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
    path('newtask/', views.newtask, name='newtask'),
    path('newcomment/<int:id>', views.newcomment, name='newcomment'),
    # path('testtask/<int:id>',views.testtask, name='testtask'),
]