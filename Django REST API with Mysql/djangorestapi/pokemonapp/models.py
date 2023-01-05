from datetime import datetime
from django.db import models

# Create your models here.

class Pokemon(models.Model):
    pokemon_id = models.IntegerField(primary_key=True)
    pokemon_name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    fast_move = models.CharField(max_length=20)
    charged_move = models.CharField(max_length=20)
    created = models.DateField(default=datetime.now)

class Trainer(models.Model):
    trainer_id = models.IntegerField(primary_key=True)
    trainer_name = models.CharField(max_length=50)
    team = models.CharField(max_length=10)
    poke = models.ForeignKey("Pokemon", on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)

