from rest_framework import serializers
from pokemonapp.models import Pokemon, Trainer

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('pokemon_id', 'pokemon_name', 'type', 'fast_move', 'charged_move', 'created')

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ('trainer_id', 'trainer_name', 'team', 'poke', 'age')