# Generated by Django 5.0.2 on 2024-02-24 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('carbs', models.FloatField()),
                ('fats', models.FloatField()),
                ('protein', models.FloatField()),
                ('calorie', models.IntegerField()),
            ],
        ),
    ]
