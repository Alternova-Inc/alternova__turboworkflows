# Generated by Django 4.2 on 2024-02-15 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_companydepartment_department_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofileset',
            name='direct_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager_profile', to='authentication.profile'),
        ),
        migrations.AlterField(
            model_name='companyprofileset',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='authentication.profile'),
        ),
    ]
