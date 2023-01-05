from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # to let access other domain to access our api
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from pokemonapp.models import Pokemon, Trainer
from pokemonapp.serializers import PokemonSerializer, TrainerSerializer

# Create your views here.
@csrf_exempt
def pokemonApi(request, id=0):
 
    if request.method == 'GET':
        pokemons = Pokemon.objects.all()
        pokemons_serializers = PokemonSerializer(pokemons, many=True)
        return JsonResponse(pokemons_serializers.data, safe=False)
    
    elif request.method == 'POST':
        pokemon_data = JSONParser().parse(request)
        pokemons_serializers = PokemonSerializer(data=pokemon_data)
        if pokemons_serializers.is_valid():
            pokemons_serializers.save()
            return JsonResponse("Uploaded Successfully", safe=False)
        return JsonResponse("Upload Fails", safe=False)
    
    elif request.method == 'PUT':
        pokemon_data = JSONParser().parse(request)
        pokemons = Pokemon.objects.get(pokemon_id=pokemon_data['pokemon_id'])
        pokemons_serializers = PokemonSerializer(pokemons, data=pokemon_data)
        if pokemons_serializers.is_valid():
            pokemons_serializers.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Update Fails", safe=False)
    
    elif request.method == 'DELETE':
        pokemons = Pokemon.objects.get(pokemon_id=id)
        pokemons.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def trainerApi(request, id=0):
 
    if request.method == 'GET':
        trainers = Trainer.objects.all()
        trainers_serializers = TrainerSerializer(trainers, many=True)
        return JsonResponse(trainers_serializers.data, safe=False)
    
    elif request.method == 'POST':
        trainer_data = JSONParser().parse(request)
        trainers_serializers = TrainerSerializer(data=trainer_data)
        if trainers_serializers.is_valid():
            trainers_serializers.save()
            return JsonResponse("Uploaded Successfully", safe=False)
        return JsonResponse("Upload Fails", safe=False)
    
    elif request.method == 'PUT':
        trainer_data = JSONParser().parse(request)
        trainers = Trainer.objects.get(trainer_id=trainer_data['trainer_id'])
        trainers_serializers = TrainerSerializer(trainers, data=trainer_data)
        if trainers_serializers.is_valid():
            trainers_serializers.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Update Fails", safe=False)
    
    elif request.method == 'DELETE':
        trainers = Pokemon.objects.get(pokemon_id=id)
        trainers.delete()
        return JsonResponse("Deleted Successfully", safe=False)







