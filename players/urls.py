from django.urls import path
from . import views


urlpatterns = [
    path('api/players', views.create_player, name='create_player'),
    path('api/players/<int:player_id>', views.delete_player_api, name='delete_player'),
    path('api/players/', views.get_players, name = 'get_players'),
    path('api/players/<int:player_id>/', views.update_player, name='update_player'),
    path('api/clubs/', views.create_club, name='create_club'),
    path('api/clubs', views.get_clubs, name='get_clubs'),
    path('api/clubs/<int:club_id>/', views.update_club, name='update_club'),
    path('api/clubs/<int:club_id>', views.delete_club, name='delete_club'),
    path('api/players/players_by_club/<str:club_name>/', views.get_players_by_club, name='get_players_by_club'),
]
