# Generated by Django 4.1.7 on 2023-03-28 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_seller_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('ph_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='costomer/')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]