# Generated by Django 3.2.8 on 2021-12-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0047_auto_20211205_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='Path',
            field=models.CharField(max_length=130, primary_key=True, serialize=False),
        ),
    ]
