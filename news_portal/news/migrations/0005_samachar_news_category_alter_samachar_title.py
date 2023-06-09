# Generated by Django 4.1.5 on 2023-04-24 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_link_samachar_image_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='samachar',
            name='news_category',
            field=models.CharField(choices=[('P', 'Politics'), ('S', 'Sports'), ('H', 'Health'), ('B', 'Business'), ('E', 'Environment'), ('O', 'Others'), ('T', 'Technology'), ('R', 'Random')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='samachar',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
