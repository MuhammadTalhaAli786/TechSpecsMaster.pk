# Generated by Django 4.2.7 on 2024-05-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='link',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
