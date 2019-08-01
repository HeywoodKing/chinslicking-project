# Generated by Django 2.2.2 on 2019-07-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190714_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chinaboutresource',
            name='type_name',
        ),
        migrations.AlterField(
            model_name='chinaboutresource',
            name='type_code',
            field=models.PositiveSmallIntegerField(choices=[(1, '企业文化'), (2, '品牌荣誉'), (3, '企业资质'), (4, '团队风采'), (5, '品牌故事'), (6, '组织架构')], default=0, verbose_name='图片业务类型'),
        ),
    ]