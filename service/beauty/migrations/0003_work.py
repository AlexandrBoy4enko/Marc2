# Generated by Django 4.1.2 on 2022-10-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0002_materials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('uuid', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]