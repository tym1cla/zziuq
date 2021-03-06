# Generated by Django 3.0.6 on 2020-06-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer_1', models.CharField(max_length=256)),
                ('answer_2', models.CharField(max_length=256)),
                ('answer_3', models.CharField(max_length=256)),
                ('answer_4', models.CharField(max_length=256)),
                ('correct_answer', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer_1', models.CharField(max_length=256)),
                ('answer_2', models.CharField(max_length=256)),
                ('answer_3', models.CharField(max_length=256)),
                ('answer_4', models.CharField(max_length=256)),
                ('correct_answer', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer_1', models.CharField(max_length=256)),
                ('answer_2', models.CharField(max_length=256)),
                ('answer_3', models.CharField(max_length=256)),
                ('answer_4', models.CharField(max_length=256)),
                ('correct_answer', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Literature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer_1', models.CharField(max_length=256)),
                ('answer_2', models.CharField(max_length=256)),
                ('answer_3', models.CharField(max_length=256)),
                ('answer_4', models.CharField(max_length=256)),
                ('correct_answer', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Science',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer_1', models.CharField(max_length=256)),
                ('answer_2', models.CharField(max_length=256)),
                ('answer_3', models.CharField(max_length=256)),
                ('answer_4', models.CharField(max_length=256)),
                ('correct_answer', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer_1', models.CharField(max_length=256)),
                ('answer_2', models.CharField(max_length=256)),
                ('answer_3', models.CharField(max_length=256)),
                ('answer_4', models.CharField(max_length=256)),
                ('correct_answer', models.CharField(max_length=8)),
            ],
        ),
    ]
