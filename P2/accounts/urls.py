from django.urls import path
from accounts.views.login import LoginView
from accounts.views.register import RegisterView
from accounts.views.profile import ProfileView
from accounts.views.getuser import GetUserView
from accounts.views.profileupdate import ProfileUpdateView
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views.follow import FollowedRestaurantView
from accounts.views.unfollow import UnfollowedRestaurantView

from accounts.views.feed import FeedView
from accounts.views.browsing import BrowsingView
from accounts.views.notifications import NotificationView

app_name = 'accounts'

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='login-refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/user/auth/', GetUserView.as_view(), name='get-user'),
    path('api/profile/<int:id>/', ProfileView.as_view(), name='profile'),
    path('api/profile/edit/', ProfileUpdateView.as_view(), name='profile-update'),
    path('api/restaurant/<int:id>/follow/', FollowedRestaurantView.as_view(), name='follow-restaurant'),
    path('api/restaurant/<int:id>/unfollow/', UnfollowedRestaurantView.as_view(), name='unfollow-restaurant'),
    path('api/feed/', FeedView.as_view(), name='feed'),
    path('api/browse/', BrowsingView.as_view(), name='browsing'),
    path('api/notifications/', NotificationView.as_view(), name='notifications')
]