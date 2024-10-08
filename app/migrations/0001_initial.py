# Generated by Django 5.0.7 on 2024-10-04 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=100)),
                ('dloc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SalGrade',
            fields=[
                ('grade', models.IntegerField(primary_key=True, serialize=False)),
                ('losal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hisal', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('ename', models.CharField(max_length=100)),
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('job', models.CharField(max_length=100)),
                ('hiredate', models.DateField(auto_now_add=True)),
                ('sal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comm', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
                ('mgr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.emp')),
            ],
        ),
    ]
