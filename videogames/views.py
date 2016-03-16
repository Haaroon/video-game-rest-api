from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from videogames.models import VideoGame
from videogames.serializers import VideoGameSerializer
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# TODO REMOVE THIS EXEMPTIOn
@csrf_exempt
def videogame_list(request):
    serializer_context = {
        'request': request,
    }
    #   List all games, or create a new game.
    if request.method == 'GET':
        videogames = VideoGame.objects.all()
        print("Video games get ", videogames)
        serializer = VideoGameSerializer(videogames, many=True, context=serializer_context)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VideoGameSerializer(data=data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def videogame_detail(request, pk):
    serializer_context = {
        'request': request,
    }

    """
    Retrieve, update or delete a videogame.
    """
    try:
        videogame = VideoGame.objects.get(pk=pk)
    except VideoGame.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VideoGameSerializer(videogame, context=serializer_context)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VideoGameSerializer(videogame, data=data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        videogame.delete()
        return HttpResponse(status=204)
