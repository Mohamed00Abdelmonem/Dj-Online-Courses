# Generated by Django 5.0.3 on 2024-04-19 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_question_choice_quiz_question_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='lesson',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]