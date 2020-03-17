# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categroy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='名称', max_length=50)),
                ('status', models.PositiveSmallIntegerField(verbose_name='状态', default=1, choices=[(1, '正常'), (0, '删除')])),
                ('is_nav', models.BooleanField(verbose_name='是否为导航', default=False)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('owner', models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=255)),
                ('desc', models.CharField(verbose_name='摘要', max_length=1024)),
                ('content', models.TextField(verbose_name='正文', help_text='正文必须为markdown格式')),
                ('status', models.PositiveSmallIntegerField(verbose_name='状态', default=1, choices=[(1, '正常'), (0, '删除'), (2, '草稿')])),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('category', models.ForeignKey(verbose_name='分类', to='blog.Categroy')),
                ('owner', models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='名称', max_length=10)),
                ('status', models.PositiveSmallIntegerField(verbose_name='状态', default=1, choices=[(1, '正常'), (0, '删除')])),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('owner', models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(verbose_name='标签', to='blog.Tag'),
        ),
    ]
