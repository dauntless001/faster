# Generated by Django 3.2 on 2021-12-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('quote_type', models.CharField(choices=[('Lagos', 'Lagos'), ('Inter-State', 'Inter-State')], default='Lagos', max_length=255)),
                ('date_requested', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
