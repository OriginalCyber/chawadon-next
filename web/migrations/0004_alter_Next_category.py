# Generated by Django 3.2.4 on 2021-08-11 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_Next_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Next',
            name='category',
            field=models.IntegerField(choices=[(1, 'ข่าวประกาศ'), (2, 'โฆษณา'), (3, 'บันทึก')], default=1),
        ),
    ]
