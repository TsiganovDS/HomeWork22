from django.urls import path
from catalog.views import HomeView
from users.views import RegisterView, LogoutView, LoginView

app_name = 'users'

urlpatterns = [
    path('', HomeView.as_view(template_name='users/login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:home'), name='logout'),

]