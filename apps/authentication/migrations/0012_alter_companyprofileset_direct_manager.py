# Generated by Django 4.2 on 2024-02-15 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_alter_companyprofileset_direct_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofileset',
            name='direct_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager_profile', to='authentication.profile'),
        ),
    ]
