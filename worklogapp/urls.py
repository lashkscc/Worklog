from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('todo',views.todo, name='todo'),
    path('inprogress',views.inprogress, name='inprogress'),
    path('done',views.done, name='done'),
    path('task/<int:id>',views.task, name='task'),
]