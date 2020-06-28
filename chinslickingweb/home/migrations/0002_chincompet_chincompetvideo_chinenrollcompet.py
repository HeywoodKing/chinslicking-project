# Generated by Django 3.0.5 on 2020-06-28 06:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChinCompet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operate_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='操作人名称')),
                ('operate_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='操作人ID')),
                ('create_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='创建人名称')),
                ('create_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='创建人ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operate_time', models.DateTimeField(auto_now=True, verbose_name='操作时间')),
                ('title', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='标题(中文)')),
                ('en_title', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='标题(英文)')),
                ('slug', models.SlugField(blank=True, help_text='根据title生成的，用于生成页面URL，必须唯一', max_length=255, null=True, unique=True, verbose_name='Slug')),
                ('content', models.TextField(blank=True, default='', null=True, verbose_name='描述(中文)')),
                ('en_content', models.TextField(blank=True, default='', null=True, verbose_name='描述(英文)')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否启用')),
            ],
            options={
                'verbose_name': '公益大赛',
                'verbose_name_plural': '公益大赛',
                'db_table': 'chin_compet',
                'ordering': ['sort', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='ChinEnrollCompet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operate_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='操作人名称')),
                ('operate_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='操作人ID')),
                ('create_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='创建人名称')),
                ('create_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='创建人ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operate_time', models.DateTimeField(auto_now=True, verbose_name='操作时间')),
                ('title', models.CharField(max_length=150, verbose_name='主题(中文)')),
                ('en_title', models.CharField(max_length=300, verbose_name='主题(英文)')),
                ('content', models.TextField(blank=True, default='', null=True, verbose_name='描述(中文)')),
                ('en_content', models.TextField(blank=True, default='', null=True, verbose_name='描述(英文)')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否启用')),
            ],
            options={
                'verbose_name': '大赛活动信息',
                'verbose_name_plural': '大赛活动信息',
                'db_table': 'chin_enrollcompet',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='ChinCompetVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operate_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='操作人名称')),
                ('operate_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='操作人ID')),
                ('create_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='创建人名称')),
                ('create_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='创建人ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operate_time', models.DateTimeField(auto_now=True, verbose_name='操作时间')),
                ('title', models.CharField(max_length=150, verbose_name='主题(中文)')),
                ('en_title', models.CharField(max_length=300, verbose_name='主题(英文)')),
                ('brief', models.CharField(blank=True, max_length=512, null=True, verbose_name='摘要(中文)')),
                ('en_brief', models.CharField(blank=True, max_length=1024, null=True, verbose_name='摘要(英文)')),
                ('content', models.TextField(blank=True, default='', null=True, verbose_name='描述(中文)')),
                ('en_content', models.TextField(blank=True, default='', null=True, verbose_name='描述(英文)')),
                ('cover_image_url', models.ImageField(blank=True, max_length=255, null=True, upload_to='compet/%Y/%m', verbose_name='封面图片')),
                ('video_source', models.FileField(blank=True, max_length=500, null=True, upload_to='compet/%Y/%m', verbose_name='视频文件地址')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否启用')),
                ('compet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.ChinCompet', verbose_name='历届大赛')),
            ],
            options={
                'verbose_name': '历届大赛视频',
                'verbose_name_plural': '历届大赛视频',
                'db_table': 'chin_competvideo',
                'ordering': ['sort', '-create_time'],
            },
        ),
    ]
