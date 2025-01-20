from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('user/', views.UserDetailView.as_view(), name='user_detail'),
    path('deactivate/', views.DeactivateUserView.as_view(), name='deactivate_user'),
    path('admin/users/', views.AdminUserListView.as_view(), name='admin_user_list'),
]
