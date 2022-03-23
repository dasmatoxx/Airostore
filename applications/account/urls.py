from django.urls import path, include

from . import views
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('reg/', RegisterView.as_view()),
    path('activate/<str:activation_code>/', views.ActivationView.as_view()),
    path('log/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]