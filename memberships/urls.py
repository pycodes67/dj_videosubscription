from django.urls import path
from .views import (
        MembershipSelectView,
        PaymentView,
        updateTransaction,
        Profile,
        cancelSubscription,
        registerView)
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'memberships'

urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select'),
    path('profile/', Profile, name='profile'),
    path('payment/', PaymentView, name='payment'),
    path('update-transaction/<subscription_id>/', updateTransaction, name='update-transactions'),
    path('cancel/', cancelSubscription, name='cancel'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', registerView, name='register'),

]
