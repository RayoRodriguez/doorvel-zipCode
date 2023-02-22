# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AreaType(models.Model):
    idarea_type = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_type'


class Areas(models.Model):
    idareas = models.AutoField(primary_key=True)
    zip_code = models.ForeignKey('ZipCode', models.DO_NOTHING, db_column='zip_code')
    name = models.CharField(max_length=100)
    idareatype = models.ForeignKey(AreaType, models.DO_NOTHING, db_column='idareaType')  # Field name made lowercase.
    d_cp = models.CharField(db_column='d_CP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    c_office = models.CharField(max_length=10, blank=True, null=True)
    empty_field = models.CharField(max_length=10, blank=True, null=True)
    id_area_cpcons = models.CharField(max_length=10, blank=True, null=True)
    idzonetype = models.ForeignKey('ZoneType', models.DO_NOTHING, db_column='idzoneType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'areas'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class City(models.Model):
    idcity = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    code = models.CharField(max_length=45, blank=True, null=True)
    idtownship = models.ForeignKey('Township', models.DO_NOTHING, db_column='idtownship')

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    idcountry = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'country'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
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


class State(models.Model):
    idstate = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=45)
    idcountry = models.ForeignKey(Country, models.DO_NOTHING, db_column='idcountry')

    class Meta:
        managed = False
        db_table = 'state'


class Township(models.Model):
    idtownship = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=45)
    idstate = models.ForeignKey(State, models.DO_NOTHING, db_column='idstate')

    class Meta:
        managed = False
        db_table = 'township'


class ZipCode(models.Model):
    zip_code = models.CharField(primary_key=True, max_length=10)
    idtownship = models.ForeignKey(Township, models.DO_NOTHING, db_column='idtownship', blank=True, null=True)
    idcity = models.ForeignKey(City, models.DO_NOTHING, db_column='idcity', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_code'


class ZoneType(models.Model):
    idzone_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'zone_type'
