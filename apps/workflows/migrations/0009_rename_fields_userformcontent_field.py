# Generated by Django 4.2 on 2024-01-26 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0008_userformcontent_remove_userform_form_fields_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userformcontent',
            old_name='fields',
            new_name='field',
        ),
    ]
