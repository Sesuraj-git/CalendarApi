# Generated by Django 4.0.3 on 2022-03-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_today_day_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='today',
            name='day_order',
            field=models.IntegerField(),
        ),
    ]