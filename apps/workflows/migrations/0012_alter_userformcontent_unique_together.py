# Generated by Django 4.2 on 2024-01-31 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0011_alter_userformcontent_user_form_delete_userform'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userformcontent',
            unique_together={('user_form', 'order')},
        ),
    ]
