# Generated by Django 3.2.9 on 2021-12-03 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_premium'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='edad',
            field=models.DecimalField(decimal_places=0, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sexo',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
