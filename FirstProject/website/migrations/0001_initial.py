# Generated by Django 5.0 on 2023-12-31 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_name', models.CharField(max_length=50)),
                ('std_roll', models.IntegerField()),
                ('std_class', models.CharField(max_length=20)),
            ],
        ),
    ]
