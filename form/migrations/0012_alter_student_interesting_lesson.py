# Generated by Django 4.1.3 on 2023-05-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0011_alter_student_hobbies_alter_student_name_of_dud_mum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='interesting_lesson',
            field=models.CharField(max_length=120, verbose_name='Кызыккан сабагы'),
        ),
    ]
