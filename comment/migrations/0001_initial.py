# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.CharField(verbose_name='内容', max_length=2000)),
                ('nicname', models.CharField(verbose_name='昵称', max_length=50)),
                ('website', models.URLField(verbose_name='网站')),
                ('email', models.EmailField(verbose_name='邮箱', max_length=254)),
                ('status', models.PositiveSmallIntegerField(verbose_name='状态', default=1, choices=[(1, '正常'), (0, '删除')])),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('target', models.ForeignKey(verbose_name='评论目标', to='blog.Post')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
