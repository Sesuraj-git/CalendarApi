# Generated by Django 4.0.3 on 2022-03-10 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_class_options_alter_collegeevent_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': ' 3. Classes'},
        ),
        migrations.AlterModelOptions(
            name='dayorder',
            options={'verbose_name_plural': ' 4. Time Table'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name_plural': ' 6. Departments'},
        ),
        migrations.AlterModelOptions(
            name='personnelstudentevent',
            options={'verbose_name_plural': ' 9. Student Personnel Event'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': ' 5. Students'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name_plural': ' 2. Teachers'},
        ),
        migrations.AlterModelOptions(
            name='today',
            options={'verbose_name_plural': " 1. Today's DayOrder"},
        ),
        migrations.AlterModelOptions(
            name='url',
            options={'verbose_name_plural': ' 7. College URLS'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': ' 8. User'},
        ),
    ]
