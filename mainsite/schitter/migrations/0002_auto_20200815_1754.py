# Generated by Django 3.0.8 on 2020-08-15 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schitter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Twaat',
            new_name='Schitt',
        ),
        migrations.RenameField(
            model_name='schitt',
            old_name='twaat_text',
            new_name='schitt_text',
        ),
    ]
