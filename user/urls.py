from django.urls import path, include
from . import views

app_name = 'user'
urlpatterns = [
    # установний URL автентифікації
    path('', include('django.contrib.auth.urls')),
    # сторінка реєстрації
    path('register/', views.register, name='register'),
]
