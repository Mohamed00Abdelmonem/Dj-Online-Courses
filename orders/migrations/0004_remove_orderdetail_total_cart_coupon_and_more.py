# Generated by Django 5.0.3 on 2024-07-08 06:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_coupon_order_orderdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='total',
        ),
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_coupon', to='orders.coupon'),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_after_coupon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('InProgress', 'InProgress')], max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='4EWCNGPO', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('InProgress', 'InProgress')], default='InProgress', max_length=10),
        ),
    ]
