# Generated by Django 4.0 on 2022-01-03 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Fragatapp', '0002_rename_place_park'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]