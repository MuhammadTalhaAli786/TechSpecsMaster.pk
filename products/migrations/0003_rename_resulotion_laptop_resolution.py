# Generated by Django 5.0.2 on 2024-02-24 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_laptop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laptop',
            old_name='resulotion',
            new_name='resolution',
        ),
    ]
