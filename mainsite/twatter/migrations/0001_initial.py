# Generated by Django 3.0.8 on 2020-08-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Twaat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=40)),
                ('twaat_text', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]