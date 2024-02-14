# Generated by Django 4.2 on 2024-02-14 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_companydepartment_department_name_and_more'),
        ('workflows', '0015_remove_workflowsequence_content_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflowstepapproval',
            name='required_position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.companyposition'),
        ),
        migrations.AlterUniqueTogether(
            name='workflowstepapproval',
            unique_together={('company', 'required_position')},
        ),
    ]
