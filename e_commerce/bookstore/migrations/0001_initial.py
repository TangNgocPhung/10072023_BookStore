# Generated by Django 4.2.3 on 2023-07-11 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to='images')),
                ('is_pdf', models.BooleanField(default=False)),
                ('is_physical', models.BooleanField(default=False)),
                ('is_ebook', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('review', models.CharField(max_length=500)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.userid')),
            ],
        ),
    ]
