# Generated by Django 3.2.8 on 2021-10-31 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monhoc',
            name='NhomMH',
            field=models.CharField(choices=[('DC', 'Môn học đại cương'), ('CSNN', 'Cơ sở nhóm ngành'), ('CSN', 'Cơ sở ngành'), ('MCN', 'Môn chuyên ngành'), ('K', 'Khác')], default='DC', max_length=10),
        ),
    ]