# Generated by Django 4.2.3 on 2023-07-10 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_exercise_completed_exercise_directions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='directions',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='intensity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='musclegroups',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]