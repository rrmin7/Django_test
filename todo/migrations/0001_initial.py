# Generated by Django 5.0.4 on 2024-04-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.CharField(max_length=200)),
                ('due_date', models.DateField()),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
