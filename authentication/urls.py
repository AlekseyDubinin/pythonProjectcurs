from django.urls import path
from authentication.apps import AuthenticationConfig
from authentication.views import SignupView, SigninView, SignoutView

app_name = AuthenticationConfig.name

urlpatterns = [
    path('signup/', SignupView.as_view(),  name='signup_view'),
    path('signin/', SigninView.as_view(), name='signin_view'),
    path('signout/', SignoutView.as_view(), name='signout_view'),

]