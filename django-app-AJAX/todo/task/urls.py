from django.urls import path

from . import views 


urlpatterns = [
	path('', views.TaskList.as_view(), name='task_list_url'),
]