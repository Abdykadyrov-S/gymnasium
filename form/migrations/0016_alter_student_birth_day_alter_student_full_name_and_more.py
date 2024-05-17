# Generated by Django 4.2.1 on 2023-06-03 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0015_alter_student_options_alter_student_date_of_saving'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birth_day',
            field=models.CharField(max_length=120, verbose_name='Тууган күнү, айы, жылы'),
        ),
        migrations.AlterField(
            model_name='student',
            name='full_name',
            field=models.CharField(max_length=120, verbose_name='Окуучунун толук аты жөнү'),
        ),
        migrations.AlterField(
            model_name='student',
            name='hobbies',
            field=models.CharField(max_length=120, verbose_name='Өнөрлөрү (Жөндөмдүүлүктөрү)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='image_path',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='Окуучунун сүрөтү (3Х4 өлчөмүндө)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='interesting_lesson',
            field=models.CharField(max_length=120, verbose_name='Кызыккан сабактары'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name_guardian',
            field=models.CharField(max_length=120, verbose_name='Окуучуга жоопту кишинин толук аты-жөнү'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name_of_dud_mum',
            field=models.CharField(max_length=120, verbose_name='Ата-энесинин аты-жөнү'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_guardian',
            field=models.CharField(max_length=120, verbose_name='Окуучуга жоопту кишинин номери'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_of_dud_mum',
            field=models.CharField(max_length=120, verbose_name='Ата-энесинин байланыш номери'),
        ),
        migrations.AlterField(
            model_name='student',
            name='region',
            field=models.CharField(max_length=120, verbose_name='Жашаган облусу, району, айылы'),
        ),
        migrations.AlterField(
            model_name='student',
            name='success',
            field=models.CharField(max_length=120, verbose_name='Ийгиликтери (олимпиада, сабактар, спорт, маданий ж.б.)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='whatsapp',
            field=models.CharField(max_length=120, verbose_name='Ар дайым байланышта болгон вотсап номери'),
        ),
    ]
