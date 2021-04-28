# Generated by Django 3.1.7 on 2021-03-31 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('percentageapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student1',
            fields=[
                ('sid', models.IntegerField(max_length=20, primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=30)),
                ('sbranch', models.CharField(max_length=30)),
                ('smarks', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
