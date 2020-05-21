from django.urls import path
from . import views

app_name = 'modal'
urlpatterns = [
	path('', views.HomeListView.as_view(), name='home'),
	path('create/post/', views.CreatePostView.as_view(), name='create_post'),	
	path('create/comment/', views.CreateCommentView.as_view(), name='create_comment'),	
	path('delete/post/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),	
	path('delete/comment/<int:pk>/', views.DeleteCommentView.as_view(), name='delete_comment'),	
]