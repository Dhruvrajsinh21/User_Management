from django.urls import path
from .views import RegisterView, LoginView, UserDetailView, SuperAdminView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/<int:user_id>/', UserDetailView.as_view(), name='user_detail'),
    path('superadmin/', SuperAdminView.as_view(), name='super_admin'),
]
