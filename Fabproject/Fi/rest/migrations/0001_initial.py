# Generated by Django 2.2.5 on 2019-10-07 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fn', models.CharField(max_length=10)),
                ('ln', models.CharField(max_length=10)),
                ('emp_id', models.IntegerField()),
            ],
        ),
    ]