# Generated by Django 4.1.5 on 2023-01-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_quangcao', '0002_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(default=1, upload_to='media'),
            preserve_default=False,
        ),
    ]
