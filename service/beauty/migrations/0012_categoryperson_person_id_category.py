# Generated by Django 4.1.2 on 2022-10-12 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0011_delete_categoryperson'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPerson',
            fields=[
                ('uuid', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='id_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='beauty.categoryperson'),
            preserve_default=False,
        ),
    ]
