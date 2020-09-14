# Generated by Django 3.0.8 on 2020-08-21 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200806_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='news.Category', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]
