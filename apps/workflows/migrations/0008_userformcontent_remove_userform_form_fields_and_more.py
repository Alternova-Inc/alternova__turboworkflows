# Generated by Django 4.2 on 2024-01-26 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_companyprofileset_role'),
        ('workflows', '0007_remove_userform_fields_userformfieldset_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFormContent',
            fields=[
                ('id', models.CharField(default='Empty', editable=False, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.PositiveIntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.company')),
                ('fields', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.userformfield')),
            ],
            options={
                'verbose_name': 'User Form Content',
                'verbose_name_plural': 'User Form Contents',
                'ordering': ['order'],
            },
        ),
        migrations.RemoveField(
            model_name='userform',
            name='form_fields',
        ),
        migrations.DeleteModel(
            name='UserFormFieldSet',
        ),
        migrations.AddField(
            model_name='userformcontent',
            name='user_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.userform'),
        ),
    ]
