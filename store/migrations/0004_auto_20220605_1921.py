# Generated by Django 3.2.9 on 2022-06-05 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20220604_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='shortdescription',
            field=models.CharField(default='this is a short description ', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='file',
            field=models.FileField(upload_to='storefile'),
        ),
    ]
