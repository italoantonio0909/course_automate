# Generated by Django 3.2 on 2021-05-03 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='email',
            field=models.EmailField(max_length=120, unique=True),
        ),
    ]