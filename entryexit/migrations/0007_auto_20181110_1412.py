# Generated by Django 2.1.3 on 2018-11-10 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entryexit', '0006_auto_20181110_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entryexit',
            old_name='building_name',
            new_name='building_id',
        ),
    ]