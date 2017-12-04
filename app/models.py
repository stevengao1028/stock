# -*- coding: utf-8 -*-
from __future__ import unicode_literals



from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cashflow(models.Model):
    year = models.CharField(max_length=20, blank=True, null=True)
    quarter = models.CharField(max_length=20, blank=True, null=True)
    field_field = models.CharField(db_column='\u80a1\u7968\u4ee3\u7801', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_0 = models.CharField(db_column='\u80a1\u7968\u540d\u79f0', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_1 = models.CharField(db_column='\u7ecf\u8425\u73b0\u91d1\u51c0\u6d41\u91cf\u5bf9\u9500\u552e\u6536\u5165\u6bd4\u7387(%)\u2193', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_2 = models.CharField(db_column='\u8d44\u4ea7\u7684\u7ecf\u8425\u73b0\u91d1\u6d41\u91cf\u56de\u62a5\u7387(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_3 = models.CharField(db_column='\u7ecf\u8425\u73b0\u91d1\u51c0\u6d41\u91cf\u4e0e\u51c0\u5229\u6da6\u7684\u6bd4\u7387(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_4 = models.CharField(db_column='\u7ecf\u8425\u73b0\u91d1\u51c0\u6d41\u91cf\u5bf9\u8d1f\u503a\u6bd4\u7387(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_5 = models.CharField(db_column='\u73b0\u91d1\u6d41\u91cf\u6bd4\u7387(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'cashflow'


class Debtpaying(models.Model):
    year = models.CharField(max_length=20, blank=True, null=True)
    quarter = models.CharField(max_length=20, blank=True, null=True)
    field_field = models.CharField(db_column='\u80a1\u7968\u4ee3\u7801', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_0 = models.CharField(db_column='\u80a1\u7968\u540d\u79f0', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_1 = models.CharField(db_column='\u6d41\u52a8\u6bd4\u7387(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_2 = models.CharField(db_column='\u901f\u52a8\u6bd4\u7387(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_3 = models.CharField(db_column='\u73b0\u91d1\u6bd4\u7387(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_4 = models.CharField(db_column='\u5229\u606f\u652f\u4ed8\u500d\u6570', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_5 = models.CharField(db_column='\u80a1\u4e1c\u6743\u76ca\u6bd4\u7387(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_6 = models.CharField(db_column='\u8d44\u4ea7\u8d1f\u503a\u7387(%)\u2191', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'debtpaying'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Grow(models.Model):
    year = models.CharField(max_length=20, blank=True, null=True)
    quarter = models.CharField(max_length=20, blank=True, null=True)
    field_field = models.CharField(db_column='\u80a1\u7968\u4ee3\u7801', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_0 = models.CharField(db_column='\u80a1\u7968\u540d\u79f0', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_1 = models.CharField(db_column='\u4e3b\u8425\u4e1a\u52a1\u6536\u5165\u589e\u957f\u7387(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_2 = models.CharField(db_column='\u51c0\u5229\u6da6\u589e\u957f\u7387(%)\u2193', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_3 = models.CharField(db_column='\u51c0\u8d44\u4ea7\u589e\u957f\u7387(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_4 = models.CharField(db_column='\u603b\u8d44\u4ea7\u589e\u957f\u7387(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_5 = models.CharField(db_column='\u6bcf\u80a1\u6536\u76ca\u589e\u957f\u7387(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_6 = models.CharField(db_column='\u80a1\u4e1c\u6743\u76ca\u589e\u957f\u7387(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'grow'


class Main(models.Model):
    year = models.CharField(max_length=20, blank=True, null=True)
    quarter = models.CharField(max_length=20, blank=True, null=True)
    field_field = models.CharField(db_column='\u80a1\u7968\u4ee3\u7801', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_0 = models.CharField(db_column='\u80a1\u7968\u540d\u79f0', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_1 = models.CharField(db_column='\u6bcf\u80a1\u6536\u76ca(\u5143)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_2 = models.CharField(db_column='\u6bcf\u80a1\u6536\u76ca\u540c\u6bd4(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_3 = models.CharField(db_column='\u6bcf\u80a1\u51c0\u8d44\u4ea7(\u5143)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_4 = models.CharField(db_column='\u51c0\u8d44\u4ea7\u6536\u76ca\u7387(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_5 = models.CharField(db_column='\u6bcf\u80a1\u73b0\u91d1\u6d41\u91cf(\u5143)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_6 = models.CharField(db_column='\u51c0\u5229\u6da6(\u4e07\u5143)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_7 = models.CharField(db_column='\u51c0\u5229\u6da6\u540c\u6bd4(%)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_8 = models.CharField(db_column='\u5206\u914d\u65b9\u6848', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_9 = models.CharField(db_column='\u53d1\u5e03\u65e5\u671f\u2193', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_10 = models.CharField(db_column='\u8be6\u7ec6', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'main'


class Operation(models.Model):
    year = models.CharField(max_length=20, blank=True, null=True)
    quarter = models.CharField(max_length=20, blank=True, null=True)
    field_field = models.CharField(db_column='\u80a1\u7968\u4ee3\u7801', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_0 = models.CharField(db_column='\u80a1\u7968\u540d\u79f0', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_1 = models.CharField(db_column='\u5e94\u6536\u8d26\u6b3e\u5468\u8f6c\u7387(\u6b21)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_2 = models.CharField(db_column='\u5e94\u6536\u8d26\u6b3e\u5468\u8f6c\u5929\u6570(\u5929)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_3 = models.CharField(db_column='\u5b58\u8d27\u5468\u8f6c\u7387(\u6b21)\u2193', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_4 = models.CharField(db_column='\u5b58\u8d27\u5468\u8f6c\u5929\u6570(\u5929)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_5 = models.CharField(db_column='\u6d41\u52a8\u8d44\u4ea7\u5468\u8f6c\u7387(\u6b21)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_6 = models.CharField(db_column='\u6d41\u52a8\u8d44\u4ea7\u5468\u8f6c\u5929\u6570(\u5929)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'operation'


class Performance(models.Model):
    year = models.CharField(max_length=20, blank=True, null=True)
    quarter = models.CharField(max_length=20, blank=True, null=True)
    field_field = models.CharField(db_column='\u80a1\u7968\u4ee3\u7801', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_0 = models.CharField(db_column='\u80a1\u7968\u540d\u79f0', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_1 = models.CharField(db_column='\u7c7b\u578b', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_2 = models.CharField(db_column='\u516c\u544a\u65e5\u671f\u2193', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_3 = models.CharField(db_column='\u62a5\u544a\u671f', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_4 = models.CharField(db_column='\u4e1a\u7ee9\u9884\u544a\u6458\u8981', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_5 = models.CharField(db_column='\u4e0a\u5e74\u540c\u671f\u6bcf\u80a1\u6536\u76ca(\u5143)', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_6 = models.CharField(db_column='\u4e1a\u7ee9\u589e\u5e45', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_7 = models.CharField(db_column='\u660e\u7ec6', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'performance'


class Profit(models.Model):
    year = models.CharField(db_column='Year', max_length=20, blank=True, null=True)  # Field name made lowercase.
    quarter = models.CharField(db_column='Quarter', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stockcode = models.CharField(db_column='StockCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stockname = models.CharField(db_column='StockName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    roe = models.CharField(db_column='ROE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    netmargin = models.CharField(db_column='NetMargin', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grossmargin = models.CharField(db_column='GrossMargin', max_length=50, blank=True, null=True)  # Field name made lowercase.
    netprofit = models.CharField(db_column='NetProfit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eps = models.CharField(db_column='EPS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    revenue = models.CharField(db_column='Revenue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    incompershare = models.CharField(db_column='IncomPerShare', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profit'