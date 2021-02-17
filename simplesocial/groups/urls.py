#GROUPS URL.PY

from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name = 'create'),
    path('posts/in/(?P<slug>[-\w]+)/', views.SingleGroup.as_view(), name = 'single'),
    path('join/(?P<slug>[-\w]+)/', views.JoinGroup.as_view(), name = 'join'),
    path('leave/(?P<slug>[-\w]+)/', views.LeaveGroup.as_view(), name = 'leave')
]

# urlpatterns = [
#     path("", views.PostList.as_view(), name="all"),
#     path("new/", views.CreatePost.as_view(), name="create"),
#     path("by/<username>/",views.UserPosts.as_view(),name="for_user"),
#     path("by/<username>/<int:pk>/",views.PostDetail.as_view(),name="single"),
#     path("delete/<int:pk>/",views.DeletePost.as_view(),name="delete"),


    # path('posts/in/<slug>/', views.SingleGroup.as_view(), name = 'single'),
    # path('join/(<slug>/', views.JoinGroup.as_view(), name = 'join'),
    # path('leave/<slug>/', views.LeaveGroup.as_view(), name = 'leave')

# ]