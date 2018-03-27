# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-27 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gratudated_and_employ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.CharField(max_length=8, verbose_name='学号')),
                ('date', models.DateField(auto_now_add=True)),
                ('gratudated', models.CharField(max_length=2, verbose_name='是否毕业')),
                ('gratudated_reason', models.CharField(blank=True, default=None, max_length=200, verbose_name='未毕业原因')),
                ('degree', models.CharField(blank=True, default=None, help_text='可以不填，以下同上', max_length=2, verbose_name='是否授予学位')),
                ('degree_reason', models.CharField(blank=True, default=None, max_length=200, verbose_name='未授予学位原因')),
                ('back_xinjiang', models.CharField(max_length=2, verbose_name='是否返回新疆')),
                ('employ_apartment', models.CharField(blank=True, default=None, max_length=15, verbose_name='就业单位')),
                ('employ_apartment_manager', models.CharField(blank=True, default=None, max_length=5, verbose_name='就业单位联系人')),
                ('employ_apartment_phone', models.CharField(blank=True, default=None, max_length=15, verbose_name='就业单位联系电话')),
            ],
            options={
                'verbose_name': '毕业就业',
                'verbose_name_plural': '毕业就业',
            },
        ),
        migrations.CreateModel(
            name='parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.CharField(blank=True, max_length=8, verbose_name='学号')),
                ('name', models.CharField(blank=True, max_length=10, verbose_name='姓名')),
                ('relation_of_student', models.CharField(blank=True, help_text='父亲/母亲/妹妹', max_length=6, verbose_name='与本人关系')),
                ('work_location', models.CharField(blank=True, max_length=20, verbose_name='工作单位')),
                ('post', models.CharField(blank=True, max_length=10, verbose_name='职务')),
                ('Political_level_p', models.CharField(blank=True, max_length=20, verbose_name='政治面貌')),
                ('phone_number', models.CharField(blank=True, max_length=10, verbose_name='联系电话')),
            ],
            options={
                'verbose_name': '家庭信息',
                'verbose_name_plural': '家庭信息',
            },
        ),
        migrations.CreateModel(
            name='student_personal_massage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=8, verbose_name='学号')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('sex', models.CharField(blank=True, max_length=10, verbose_name='性别')),
                ('family_address', models.CharField(blank=True, default=None, max_length=50, verbose_name='家庭住址')),
                ('academy', models.CharField(blank=True, default=None, max_length=15, verbose_name='学院')),
                ('class_num', models.CharField(blank=True, max_length=100, verbose_name='班级')),
                ('train_level', models.CharField(blank=True, help_text='本科/专科', max_length=5, verbose_name='学制')),
                ('registered_residence', models.CharField(blank=True, max_length=20, verbose_name='入学前户口')),
                ('length_of_schooling', models.CharField(blank=True, help_text='例如四年/三年', max_length=10, verbose_name='学制')),
                ('Political_level', models.CharField(blank=True, max_length=20, verbose_name='政治面貌')),
                ('graduated_high_school', models.CharField(blank=True, max_length=20, verbose_name='高中毕业学校')),
                ('graduation_grades', models.IntegerField(blank=True, verbose_name='高考总分')),
                ('single_kinds', models.CharField(blank=True, max_length=5, verbose_name='是否独生子女')),
                ('study_way', models.CharField(blank=True, help_text='汉语/其他语言', max_length=15, verbose_name='入学前授课方式')),
                ('status', models.BooleanField(default=False, verbose_name='验证状态')),
            ],
            options={
                'verbose_name': '学生基本信息',
                'verbose_name_plural': '学生基本信息填写',
            },
        ),
        migrations.CreateModel(
            name='update_massage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True, auto_now_add=True)),
                ('stu_id', models.CharField(blank=True, max_length=8, verbose_name='学号')),
                ('living_room', models.CharField(blank=True, max_length=6, verbose_name='所在宿舍')),
                ('phone_number', models.CharField(blank=True, max_length=11, verbose_name='电话')),
                ('pareants_single', models.CharField(blank=True, max_length=2, verbose_name='是/否单亲家庭')),
                ('basic_living_allowances', models.CharField(blank=True, max_length=2, verbose_name='是否拥有最低城市/农村生活保障')),
                ('orphan_disablity', models.CharField(blank=True, max_length=2, verbose_name='是/否孤残')),
                ('martyr', models.CharField(blank=True, max_length=2, verbose_name='是/否烈士子女')),
                ('party_member', models.CharField(blank=True, max_length=2, verbose_name='是/否党员')),
                ('party_member_application', models.CharField(blank=True, max_length=2, verbose_name='是/否递交入党申请书')),
                ('population', models.CharField(blank=True, max_length=5, verbose_name='家庭人口数')),
                ('poor', models.CharField(blank=True, help_text='是/否', max_length=5, verbose_name='家庭是否困难')),
                ('poor_reason', models.CharField(blank=True, max_length=50, verbose_name='困难原因')),
                ('Instructor', models.CharField(max_length=10, verbose_name='辅导员姓名')),
                ('Instructor_nmber', models.CharField(max_length=11, verbose_name='辅导员电话')),
            ],
            options={
                'verbose_name': '就读信息',
                'verbose_name_plural': '就读信息',
            },
        ),
    ]
