# Generated by Django 3.2.6 on 2022-10-11 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('uuid', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
    ]
