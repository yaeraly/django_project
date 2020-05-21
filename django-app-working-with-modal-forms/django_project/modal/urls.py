from django.urls import path

from . import views


app_name = 'modal'
urlpatterns = [
	path('', views.HomeListView.as_view(), name='home'),
	path('create/', views.CreateEmployeeView.as_view(), name='create'),
	path('update/<int:pk>/', views.UpdateEmployeeView.as_view(), name='update'),
	path('delete/<int:pk>/', views.DeleteEmployeeView.as_view(), name='delete'),

]