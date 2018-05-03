# Generated by Django 2.0.4 on 2018-04-26 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('created', models.DateTimeField(verbose_name='date created')),
                ('due_to', models.DateTimeField(verbose_name='due to date')),
                ('status', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
                ('completness', models.IntegerField(default=0)),
            ],
        ),
    ]
