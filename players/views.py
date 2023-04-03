from rest_framework import generics
from .serializers import PlayerSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Player
from django.views.decorators.csrf import csrf_exempt
import json


class PlayerCreateView(generics.CreateAPIView):
    serializer_class = PlayerSerializer


@csrf_exempt
def delete_player_api(request, player_id):
    if request.method == 'DELETE':
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
            nickname = data['nickname']
            name = data.get('name', '')
            club = data.get('club', '')
            player = Player(nickname=nickname, name=name, club=club)
            player.save()
            return JsonResponse({'message': 'Player created successfully'})
        except KeyError:
            return JsonResponse({'error': 'Invalid request format'}, status=400)
        except ValueError:
            return JsonResponse({'error': 'Invalid request data'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
