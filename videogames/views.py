from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from videogames.models import VideoGame
from videogames.serializers import VideoGameSerializer
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

# TODO REMOVE THIS EXEMPTIOn
@api_view(['GET'] ) #, 'POST'])
def videogame_list(request, format=None):
    serializer_context = {
        'request': request,
    }
    #   List all games, or create a new game.
    if request.method == 'GET':
        videogames = VideoGame.objects.all()
        print("Video games get ", videogames)
        serializer = VideoGameSerializer(videogames, many=True, context=serializer_context)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VideoGameSerializer(data=data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET']) # 'PUT'])
def videogame_detail(request, pk, format=None):
    serializer_context = {
        'request': request,
    }

    """
    Retrieve, update or delete a videogame.
    """
    try:
        videogame = VideoGame.objects.get(pk=pk)
    except VideoGame.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VideoGameSerializer(videogame, context=serializer_context)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VideoGameSerializer(videogame, data=data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     videogame.delete()
    #     return HttpResponse(status=204)
