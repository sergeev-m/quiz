# Generated by Django 3.2 on 2023-05-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.PositiveIntegerField(db_index=True, unique=True, verbose_name='id вопроса')),
                ('question', models.TextField(verbose_name='Текст вопроса')),
                ('answer', models.TextField(verbose_name='Ответ на вопрос')),
                ('created_at', models.DateTimeField(verbose_name='Дата публикации вопроса')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]
