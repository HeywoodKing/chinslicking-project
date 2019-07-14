# Generated by Django 2.2.2 on 2019-07-14 07:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChinQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operate_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='操作人名称')),
                ('operate_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='操作人ID')),
                ('create_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='创建人名称')),
                ('create_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='创建人ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operate_time', models.DateTimeField(auto_now=True, verbose_name='操作时间')),
                ('name', models.CharField(max_length=200, verbose_name='问题标题')),
                ('content', models.TextField(blank=True, default=None, null=True, verbose_name='问题描述')),
                ('type', models.SmallIntegerField(choices=[(-1, '不是问题'), (0, '浏览器问题'), (1, '操作系统问题'), (2, '真bug'), (3, '其他问题')], default=-1, verbose_name='问题类型')),
                ('state', models.SmallIntegerField(choices=[(-1, '待解决'), (0, '未解决'), (1, '已解决'), (2, '延期处理')], default=-1, verbose_name='问题状态')),
            ],
            options={
                'verbose_name': '问题汇总列表',
                'verbose_name_plural': '问题汇总列表',
                'db_table': 'chin_question',
                'ordering': ['-create_time'],
            },
        ),
        migrations.AlterField(
            model_name='chincooperation',
            name='type',
            field=models.CharField(choices=[('0', '合作政策'), ('1', '项目优势'), ('2', '经销商问答'), ('3', '支持与服务')], default=0, max_length=10, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='chinnews',
            name='brief',
            field=models.CharField(max_length=120, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='chinnews',
            name='title',
            field=models.CharField(max_length=64, verbose_name='标题'),
        ),
        migrations.CreateModel(
            name='SysNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operate_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='操作人名称')),
                ('operate_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='操作人ID')),
                ('create_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='创建人名称')),
                ('create_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='创建人ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operate_time', models.DateTimeField(auto_now=True, verbose_name='操作时间')),
                ('code', models.CharField(default=None, max_length=20, verbose_name='标识')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('url', models.CharField(max_length=200, verbose_name='链接')),
                ('remark', models.CharField(blank=True, max_length=300, verbose_name='描述')),
                ('is_root', models.BooleanField(default=True, verbose_name='是否一级菜单')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否启用')),
                ('parent', models.ForeignKey(blank=True, default=0, limit_choices_to={'is_delete': False, 'is_root': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='home.SysNav', verbose_name='父级')),
            ],
            options={
                'verbose_name': '导航菜单管理',
                'verbose_name_plural': '导航菜单管理',
                'db_table': 'sys_nav',
                'ordering': ['sort', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='ChinBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operate_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='操作人名称')),
                ('operate_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='操作人ID')),
                ('create_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='创建人名称')),
                ('create_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='创建人ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operate_time', models.DateTimeField(auto_now=True, verbose_name='操作时间')),
                ('image_url', models.ImageField(blank=True, default=None, null=True, upload_to='banner/%Y/%m', verbose_name='图片')),
                ('text', models.CharField(default=None, max_length=150, verbose_name='Banner上文本描述')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否启用')),
                ('nav', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='navs', related_query_name='nav_query', to='home.SysNav', verbose_name='Banner页面')),
            ],
            options={
                'verbose_name': 'Banner管理',
                'verbose_name_plural': 'Banner管理',
                'db_table': 'chin_banner',
                'ordering': ['nav', 'sort', '-create_time'],
            },
        ),
    ]
