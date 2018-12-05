# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Locations(models.Model):
    l_id = models.IntegerField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Locations'


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


class Conference(models.Model):
    c_id = models.IntegerField()
    c_name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'conference'


class Division(models.Model):
    d_id = models.IntegerField()
    d_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'division'


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


class Matchup(models.Model):
    m_id = models.IntegerField()
    m_teama_id = models.DecimalField(db_column='m_teamA_ID', max_digits=10, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    m_teama_name = models.TextField(db_column='m_teamA_Name')  # Field name made lowercase. This field type is a guess.
    m_teamb_name = models.TextField(db_column='m_teamB_Name')  # Field name made lowercase. This field type is a guess.
    m_teama_result = models.TextField(db_column='m_teamA_result')  # Field name made lowercase. This field type is a guess.
    m_teamb_result = models.TextField(db_column='m_teamB_result')  # Field name made lowercase. This field type is a guess.
    m_date = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'matchup'


class Player(models.Model):
    p_id = models.DecimalField(unique=True, max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    p_pname = models.CharField(max_length=30)
    p_age = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    p_points = models.TextField()  # This field type is a guess.
    p_assists = models.TextField()  # This field type is a guess.
    p_fgp = models.TextField()  # This field type is a guess.
    p_3pp = models.TextField()  # This field type is a guess.
    p_minutes = models.TextField()
    p_rebounds = models.TextField()  # This field type is a guess.
    p_abr = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'player'


class Playoffs(models.Model):
    po_id = models.IntegerField()
    po_teamid = models.CharField(db_column='po_teamID', max_length=30)  # Field name made lowercase.
    po_wins = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    po_loss = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    po_wonchampionship = models.BooleanField(db_column='po_wonChampionship')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playoffs'


class Team(models.Model):
    t_id = models.IntegerField()
    t_name = models.CharField(max_length=30)
    t_wins = models.TextField()  # This field type is a guess.
    t_loss = models.TextField()  # This field type is a guess.
    t_ratio = models.TextField()  # This field type is a guess.
    t_fgp = models.TextField()  # This field type is a guess.
    t_3pp = models.TextField()  # This field type is a guess.
    t_confid = models.IntegerField()
    t_divisionid = models.IntegerField()
    t_abr = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'team'


class Teamlocations(models.Model):
    tl_id = models.IntegerField(blank=True, null=True)
    loc_id = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    t_id = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    fromyear = models.TextField(db_column='fromYear', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    toyear = models.TextField(db_column='toYear', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'teamLocations'


class Teammatchup(models.Model):
    tm_id = models.IntegerField(blank=True, null=True)
    m = models.ForeignKey(Matchup, models.DO_NOTHING, blank=True, null=True)
    t_id = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    teamb_name = models.TextField(db_column='teamB_Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'teamMatchup'