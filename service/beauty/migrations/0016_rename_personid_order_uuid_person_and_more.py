# Generated by Django 4.1.2 on 2022-10-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0015_alter_person_id_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='personID',
            new_name='uuid_person',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='servicesID',
            new_name='uuid_services',
        ),
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(max_length=255, verbose_name='Пол'),
        ),
    ]