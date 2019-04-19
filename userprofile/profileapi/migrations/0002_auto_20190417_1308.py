# Generated by Django 2.1.3 on 2019-04-17 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]