# Generated by Django 5.1.3 on 2024-11-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Men', 'T-Shirt'), ('Men', 'Sports-T-Shirt'), ('Women', 'T-Shirt')], max_length=7),
        ),
    ]
