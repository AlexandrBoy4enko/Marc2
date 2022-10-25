# Generated by Django 4.1.2 on 2022-10-20 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPerson',
            fields=[
                ('uuid', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('uuid', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('uuid', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('uuid', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.DecimalField(decimal_places=0, max_digits=3)),
                ('mail', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=255, verbose_name='Пол')),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.categoryperson')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('uuid', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateField()),
                ('profit', models.IntegerField()),
                ('uuid_materials', models.ManyToManyField(to='core.material')),
                ('uuid_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='core.person')),
                ('uuid_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='core.services')),
            ],
        ),
    ]
