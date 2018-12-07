# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-12-04 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('username', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.IntegerField()),
                ('c_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'conference',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_id', models.IntegerField()),
                ('d_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'division',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('action_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_id', models.IntegerField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Locations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Matchup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.IntegerField()),
                ('m_teama_id', models.DecimalField(db_column='m_teamA_ID', decimal_places=5, max_digits=10)),
                ('m_teama_name', models.TextField(db_column='m_teamA_Name')),
                ('m_teamb_name', models.TextField(db_column='m_teamB_Name')),
                ('m_teama_result', models.TextField(db_column='m_teamA_result')),
                ('m_teamb_result', models.TextField(db_column='m_teamB_result')),
                ('m_date', models.TextField()),
            ],
            options={
                'db_table': 'matchup',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.DecimalField(decimal_places=5, max_digits=10, unique=True)),
                ('p_pname', models.CharField(max_length=30)),
                ('p_age', models.DecimalField(decimal_places=5, max_digits=10)),
                ('p_points', models.TextField()),
                ('p_assists', models.TextField()),
                ('p_fgp', models.TextField()),
                ('p_3pp', models.TextField()),
                ('p_minutes', models.DecimalField(decimal_places=0, max_digits=30)),
                ('p_rebounds', models.TextField()),
                ('p_abr', models.TextField()),
            ],
            options={
                'db_table': 'player',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Playoffs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_id', models.IntegerField()),
                ('po_teamid', models.CharField(db_column='po_teamID', max_length=30)),
                ('po_wins', models.DecimalField(decimal_places=5, max_digits=10)),
                ('po_loss', models.DecimalField(decimal_places=5, max_digits=10)),
                ('po_wonchampionship', models.BooleanField(db_column='po_wonChampionship')),
            ],
            options={
                'db_table': 'playoffs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_id', models.IntegerField()),
                ('t_name', models.CharField(max_length=30)),
                ('t_wins', models.TextField()),
                ('t_loss', models.TextField()),
                ('t_ratio', models.TextField()),
                ('t_fgp', models.TextField()),
                ('t_3pp', models.TextField()),
                ('t_confid', models.IntegerField()),
                ('t_divisionid', models.IntegerField()),
                ('t_abr', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'team',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teamlocations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tl_id', models.IntegerField(blank=True, null=True)),
                ('loc_id', models.DecimalField(decimal_places=5, max_digits=10)),
                ('t_id', models.DecimalField(decimal_places=5, max_digits=10)),
                ('fromyear', models.TextField(blank=True, db_column='fromYear', null=True)),
                ('toyear', models.TextField(blank=True, db_column='toYear', null=True)),
            ],
            options={
                'db_table': 'teamLocations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teammatchup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tm_id', models.IntegerField(blank=True, null=True)),
                ('t_id', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('teamb_name', models.TextField(blank=True, db_column='teamB_Name', null=True)),
            ],
            options={
                'db_table': 'teamMatchup',
                'managed': False,
            },
        ),
    ]
