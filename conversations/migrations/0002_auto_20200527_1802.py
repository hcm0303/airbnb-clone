# Generated by Django 2.2.5 on 2020-05-27 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='converstion',
            new_name='conversation',
        ),
    ]
