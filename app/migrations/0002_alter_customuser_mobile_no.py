# Generated by Django 4.1.2 on 2022-10-20 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
