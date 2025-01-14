# Generated by Django 5.1.3 on 2024-11-20 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids')], default='Men', max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Men', 'T-Shirt'), ('Men', 'Sports-T-Shirt'), ('Women', 'T-Shirt'), ('Women', 'Sports-T-Shirt'), ('Kids', 'T-Shirt'), ('Kids', 'Sports-T-Shirt')], max_length=20),
        ),
    ]
