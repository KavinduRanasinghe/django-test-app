# Generated by Django 5.0.6 on 2024-06-21 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitems',
            old_name='course',
            new_name='category',
        ),
    ]
