from django.urls import path
from .views import list_books
from .views import (
    list_books,
    LibraryDetailView,
    UserLoginView,
    UserLogoutView,
    register
)

app_name = 'relationship_app'

urlpatterns = [
    # existing views
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # authentication
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]

["views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="]