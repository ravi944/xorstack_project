# Generated by Django 4.0.5 on 2022-09-08 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('salary', models.CharField(max_length=10)),
                ('phone', models.IntegerField()),
                ('country', models.CharField(choices=[('IN', 'INDIA'), ('USA', 'AMERICA'), ('RUS', 'RUSSIA'), ('AUSTR', 'AUSTRALIA')], default=None, max_length=20)),
            ],
        ),
    ]
