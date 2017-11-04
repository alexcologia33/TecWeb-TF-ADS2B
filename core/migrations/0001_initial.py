# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('sigla', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'Curso',
            },
        ),
        migrations.CreateModel(
            name='GradeCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.SmallIntegerField()),
                ('semestre', models.CharField(max_length=1)),
                ('sigla_curso', models.ForeignKey(db_column='sigla_curso', on_delete=django.db.models.deletion.CASCADE, to='core.Curso')),
            ],
            options={
                'db_table': 'GradeCurricular',
            },
        ),
        migrations.AlterUniqueTogether(
            name='gradecurricular',
            unique_together=set([('sigla_curso', 'ano', 'semestre')]),
        ),
    ]
