# Generated by Django 4.1.5 on 2023-01-04 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pokemonapp", "0003_alter_pokemon_pokemon_id_alter_trainer_trainer_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="trainer", old_name="pk_id", new_name="poke",
        ),
    ]
