from django.contrib.auth import views
from django.urls import path,include
from accounts.views import AccountProfile, RegisterAccount
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', AccountProfile.as_view(), name='accounts.profile'),
    path('register', RegisterAccount.as_view(), name='accounts.register')
]