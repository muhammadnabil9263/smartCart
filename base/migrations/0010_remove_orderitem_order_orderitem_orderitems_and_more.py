# Generated by Django 4.0.3 on 2022-05-13 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0009_rename_bar_code_product_barcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='orderItems',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderItems', to='base.order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.cart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='base.product'),
        ),
    ]