# Generated by Django 3.0 on 2019-12-14 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioTemplate', '0003_auto_20191212_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecontent',
            name='image',
            field=models.ImageField(default='offecial.jpeg', upload_to='profile_image'),
        ),
    ]
