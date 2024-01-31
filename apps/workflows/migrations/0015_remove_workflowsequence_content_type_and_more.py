# Generated by Django 4.2 on 2024-01-31 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0014_remove_workflowstepaction_workflow_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workflowsequence',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='workflowsequence',
            name='object_id',
        ),
        migrations.AddField(
            model_name='workflowsequence',
            name='action_step',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowstepaction'),
        ),
        migrations.AddField(
            model_name='workflowsequence',
            name='approval_step',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowstepapproval'),
        ),
        migrations.AddField(
            model_name='workflowsequence',
            name='form_step',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowstepform'),
        ),
    ]