# Generated by Django 4.2 on 2024-01-27 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0010_alter_userformcontent_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userformcontent',
            name='user_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowstepform'),
        ),
        migrations.DeleteModel(
            name='UserForm',
        ),
    ]
