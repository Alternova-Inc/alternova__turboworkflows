# Generated by Django 4.2 on 2024-01-19 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_remove_profile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofileset',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.role'),
        ),
    ]
