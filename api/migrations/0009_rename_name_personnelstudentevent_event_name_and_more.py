# Generated by Django 4.0.3 on 2022-03-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_today_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnelstudentevent',
            old_name='name',
            new_name='event_name',
        ),
        migrations.AlterField(
            model_name='personnelstudentevent',
            name='option',
            field=models.CharField(choices=[('COMPLETED', 'COMPLETED'), ('MARKED AS COMPLETE', 'MARKED AS COMPLETE')], default='MARKED AS COMPLETE', max_length=360),
        ),
    ]