# Generated by Django 2.2 on 2022-06-13 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0003_auto_20220613_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='resumes',
            field=models.ImageField(default='./img/johnny.jpg', upload_to='img'),
        ),
    ]
