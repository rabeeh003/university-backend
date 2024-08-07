# Generated by Django 5.0.7 on 2024-07-18 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='courses/')),
                ('description', models.TextField()),
                ('qualification', models.TextField()),
                ('duration', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.course')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.department')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.semester')),
            ],
        ),
    ]
