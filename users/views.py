from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'Utilisateur non trouvé'}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        User.objects.create_user(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=request.data.get('password')  # Ne pas oublier de récupérer le password brut !
        )
        return Response({'message': 'Utilisateur créé'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return Response({'message': 'Utilisateur supprimé'})
    except User.DoesNotExist:
        return Response({'error': 'Utilisateur non trouvé'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'Utilisateur non trouvé'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Utilisateur mis à jour'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def login_api(request):
    """
    API de connexion - POST { username, password }
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Connexion réussie.'})
        else:
            return JsonResponse({'success': False, 'message': 'Identifiants invalides.'}, status=401)

    return JsonResponse({'success': False, 'message': 'Méthode non autorisée.'}, status=405)

@csrf_exempt
def logout_api(request):
    """
    API de déconnexion
    """
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'success': True, 'message': 'Déconnexion réussie.'})

    return JsonResponse({'success': False, 'message': 'Méthode non autorisée.'}, status=405)


@csrf_exempt
def register_api(request):
    """
    API d'inscription - POST { username, password }
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return JsonResponse({'success': False, 'message': 'Username et password requis.'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': 'Ce username existe déjà.'}, status=400)

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return JsonResponse({'success': True, 'message': 'Utilisateur créé avec succès.'})

    return JsonResponse({'success': False, 'message': 'Méthode non autorisée.'}, status=405)

