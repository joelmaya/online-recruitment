# Generated by Django 2.2 on 2022-06-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_user_resumes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='resumes',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
