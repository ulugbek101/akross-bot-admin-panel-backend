# Generated by Django 5.0.6 on 2024-06-08 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_telegramuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='language_code',
            field=models.CharField(choices=[('uz', 'uz'), ('ru', 'ru'), ('en', 'en')], default='uz', max_length=2),
        ),
    ]
