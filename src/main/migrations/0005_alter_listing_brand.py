# Generated by Django 5.1.1 on 2024-10-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_likedlisting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='brand',
            field=models.CharField(choices=[('bmw', 'BMW'), ('mercedes benz', 'Mercedes Benz'), ('audi', 'Audi'), ('subaru', 'Subaru'), ('tesla', 'Tesla'), ('jaguar', 'Jaguar'), ('land rover', 'Land Rover'), ('bentley', 'Bentley'), ('bugatti', 'Bugatti'), ('ferrari', 'Ferrari'), ('lamborghini', 'Lamborghini'), ('honda', 'Honda'), ('toyota', 'Toyota'), ('chevrolet', 'Chevrolet'), ('porsche', 'Porsche'), ('dodge', 'Dodge')], default=None, max_length=24),
        ),
    ]
