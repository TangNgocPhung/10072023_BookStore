# Generated by Django 4.2.1 on 2023-07-12 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_alter_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
