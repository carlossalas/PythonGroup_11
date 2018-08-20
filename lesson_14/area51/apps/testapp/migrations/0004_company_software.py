# Generated by Django 2.1 on 2018-08-18 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testapp', '0003_auto_20180817_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('website', models.URLField()),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('version', models.PositiveSmallIntegerField()),
                ('repository', models.URLField(blank=True, max_length=100, null=True)),
                ('deploy_date', models.DateField()),
            ],
        ),
    ]
