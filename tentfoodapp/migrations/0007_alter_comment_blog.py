# Generated by Django 5.1.1 on 2024-10-17 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tentfoodapp', '0006_alter_menubakery_description_alter_menubakery_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tentfoodapp.blog'),
        ),
    ]