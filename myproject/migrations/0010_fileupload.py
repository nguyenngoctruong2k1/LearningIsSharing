# Generated by Django 3.2.8 on 2021-11-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0009_alter_tailieu_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaTL', models.CharField(help_text='username người đăng', max_length=30)),
                ('filename', models.CharField(help_text='username người đăng', max_length=30)),
                ('Path', models.CharField(help_text='username người đăng', max_length=30)),
                ('FileUL', models.FileField(upload_to='')),
            ],
        ),
    ]
