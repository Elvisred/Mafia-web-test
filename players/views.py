from rest_framework import generics
from .serializers import PlayerSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Player, Club
from django.views.decorators.csrf import csrf_exempt

import json


class PlayerCreateView(generics.CreateAPIView):
    serializer_class = PlayerSerializer


@csrf_exempt
def delete_player_api(request, player_id):
    if 'DELETE' == request.method:
        try:
            player = get_object_or_404(Player, id=player_id)
            player.delete()
            return JsonResponse({'message': f'Player with ID {player_id} deleted successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def create_player(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nickname = data.get('nickname')
            name = data.get('name')
            club = data.get('club')

            # Добавьте проверки для всех обязательных полей
            if not nickname:
                return JsonResponse({'error': 'Nickname is required'}, status=400)
            if not name:
                return JsonResponse({'error': 'Name is required'}, status=400)
            if not club:
                return JsonResponse({'error': 'Club is required'}, status=400)

            # Проверка максимальной длины строк
            if len(nickname) > 30:
                return JsonResponse({'error': 'Nickname must be max 30 characters'}, status=400)
            if len(name) > 30:
                return JsonResponse({'error': 'Name must be 30 max characters'}, status=400)

            player, created = Player.objects.get_or_create(
                nickname=nickname,
                defaults={'name': name, 'club': club}
            )

            if not created:
                return JsonResponse({'error': 'Player with this nickname already exists'}, status=400)

            response_data = {
                'message': f'Player {nickname} created successfully',
                'id': player.id
            }
            return JsonResponse(response_data, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_players(request):
    if request.method == 'GET':
        try:
            players = Player.objects.all()
            players_data = []
            for player in players:
                player_data = {
                    'id': player.id,
                    'nickname': player.nickname,
                    'name': player.name,
                    'club': player.club
                }
                players_data.append(player_data)
            return JsonResponse({'players': players_data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def update_player(request, player_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            if 'id' not in data or data['id'] != player_id:
                return JsonResponse({'error': 'ID must be present in request body and match URL parameter'},
                                    status = 400)

            player = get_object_or_404(Player, id = player_id)

            nickname = data.get('nickname')
            name = data.get('name')
            club = data.get('club')

            if nickname is not None:
                player.nickname = nickname
            if name is not None:
                player.name = name
            if club is not None:
                player.club = club

            player.save()

            return JsonResponse({'message': f'Player with ID {player_id} updated successfully'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status = 400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status = 405)


def get_clubs(request):
    if request.method == 'GET':
        try:
            clubs = Club.objects.all()
            clubs_data = [{'id': club.id, 'club_name': club.club_name, 'city': club.city} for club in clubs]
            return JsonResponse({'clubs': clubs_data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def create_club(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            club_name = data.get('club_name')
            city = data.get('city')

            # Добавьте проверки для всех обязательных полей
            if not club_name:
                return JsonResponse({'error': 'Club name is required'}, status=400)
            if not city:
                return JsonResponse({'error': 'City is required'}, status=400)

            # Проверка максимальной длины строк
            if len(club_name) > 30:
                return JsonResponse({'error': 'Club name must be max 30 characters'}, status=400)
            if len(city) > 30:
                return JsonResponse({'error': 'City must be max 30 characters'}, status=400)

            club, created = Club.objects.get_or_create(
                club_name=club_name,
                defaults={'city': city}
            )

            if not created:
                return JsonResponse({'error': 'Club with this name already exists'}, status=400)

            response_data = {
                'message': f'Club {club_name} created successfully',
                'id': club.id
            }
            return JsonResponse(response_data, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def delete_club(request, club_id):
    if request.method == 'DELETE':
        try:
            club = get_object_or_404(Club, id=club_id)
            club.delete()
            return JsonResponse({'message': f'Club with ID {club_id} deleted successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def update_club(request, club_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            if 'id' not in data or data['id'] != club_id:
                return JsonResponse({'error': 'ID must be present in request body and match URL parameter'},
                                    status=400)

            club = get_object_or_404(Club, id=club_id)

            club_name = data.get('club_name')
            city = data.get('city')

            if club_name is not None:
                club.club_name = club_name
            if city is not None:
                club.city = city

            club.save()

            return JsonResponse({'message': f'Club with ID {club_id} updated successfully'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_players_by_club(request, club_name):
    if request.method == 'GET':
        try:
            club = Club.objects.get(club_name=club_name)
            players = Player.objects.filter(club=club)
            players_data = [{'id': player.id, 'nickname': player.nickname, 'name': player.name} for player in players]
            return JsonResponse({'players': players_data})
        except Club.DoesNotExist:
            return JsonResponse({'error': 'Club not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
