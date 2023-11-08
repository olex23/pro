"""Defines URl patterns for learning_logs."""  # написали докстрінг з вказанням з яким urls.py працюємо
"""визначаємо шаблони для learning_logs."""

from django.urls import path

from . import views

app_name = "learning_logs"
urlpatterns = [

    # """Головна сторінка"""

    path('', views.index, name="index"),

    # ''' Сторінка що відображає всі теми '''
    path('topics/', views.topics, name='topics'),

    # ''' сторінка окремоїтеми'''

    path("topics/<int:topic_id>/", views.topic, name='topic'),

    # """ сторінка для доданої нової теми"""

    path("new_topic/", views.new_topic, name='new_topic'),

    # сторінка для додавання нового допису

    path("new_entry/<int:topic_id>/", views.new_entry, name='new_entry'),

    # сторінка для редагування дописів

    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
