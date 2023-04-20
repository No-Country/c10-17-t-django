from django.urls import path
from .views import *
urlpatterns = [
    #FollowUp
    path('follow-user/',FollowUser.as_view()),
    path('unfollow-user/',UnFollowUser.as_view()),
    path('list-followings/',ListFollowings.as_view()),
    path('list-followers/',ListFollowers.as_view()),
]
