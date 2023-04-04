from django.urls import path
from . import views

urlpatterns = [
    path('create-post/',views.CreatePostView.as_view(),name='create-post'),
    path('show-post/',views.ShowPostView.as_view(),name='show-post')
]
