# Generated by Django 4.2 on 2023-04-14 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_api', '0003_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('URGENT!', 'urgent'), ('DO', 'do'), ('DEFER', 'defer')], default='DO'),
        ),
    ]
