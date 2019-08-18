# Generated by Django 2.2.2 on 2019-08-03 06:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190803_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChinStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operate_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='操作人名称')),
                ('operate_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='操作人ID')),
                ('create_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='创建人名称')),
                ('create_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='创建人ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operate_time', models.DateTimeField(auto_now=True, verbose_name='操作时间')),
                ('short_title', models.CharField(default='', max_length=80, verbose_name='短板故事标题')),
                ('short_content', models.TextField(default='', max_length=1000, verbose_name='短板故事')),
                ('long_title', models.CharField(default='', max_length=80, verbose_name='长板故事标题')),
                ('long_content', models.TextField(default='', max_length=4000, verbose_name='长板故事')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否启用')),
            ],
            options={
                'verbose_name': '秦始皇故事',
                'verbose_name_plural': '秦始皇故事',
                'db_table': 'chin_story',
                'ordering': ['-create_time'],
            },
        ),
    ]
