from django.urls import path
from . import views


urlpatterns = [
    path('api/players', views.create_player, name='create_player'),
    path('api/players/<int:player_id>', views.delete_player_api, name = 'delete_player_api'),
]
