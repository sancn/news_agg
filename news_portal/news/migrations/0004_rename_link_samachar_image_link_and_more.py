# Generated by Django 4.2 on 2023-04-20 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_samachar_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='samachar',
            old_name='link',
            new_name='image_link',
        ),
        migrations.RemoveField(
            model_name='samachar',
            name='photo',
        ),
        migrations.AddField(
            model_name='samachar',
            name='news_link',
            field=models.CharField(default='', max_length=200),
        ),
    ]