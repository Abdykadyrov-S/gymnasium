# Generated by Django 4.2.1 on 2023-05-30 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0014_alter_student_11_options_alter_student_11_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Окучулардын Тизмеси', 'verbose_name_plural': 'Окучулардын Тизмеси'},
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_saving',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Катталган датасы'),
        ),
    ]
