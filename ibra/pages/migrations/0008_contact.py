# Generated by Django 4.2.11 on 2024-03-08 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_delete_contact_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('report', models.CharField(max_length=2048)),
            ],
        ),
    ]