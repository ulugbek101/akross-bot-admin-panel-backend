# Generated by Django 5.0.6 on 2024-06-07 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_telegramuser_language_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='status',
            field=models.CharField(choices=[('bronze', '🥉 Bronze'), ('silver', '🥈 Silver'), ('gold', '🥇 Gold'), ('platinum', '🌟 Platinum')], default='bronze', max_length=200),
        ),
    ]
