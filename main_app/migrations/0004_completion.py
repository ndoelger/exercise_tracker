# Generated by Django 4.2.3 on 2023-07-10 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_exercise_directions_alter_exercise_intensity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reps', models.IntegerField()),
                ('sets', models.IntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completion_set', to='main_app.exercise')),
            ],
        ),
    ]