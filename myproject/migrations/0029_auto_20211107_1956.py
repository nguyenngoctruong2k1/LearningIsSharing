# Generated by Django 3.2.8 on 2021-11-07 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0028_auto_20211107_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tailieu',
            name='LuotTai',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='tailieu',
            name='LuotXem',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]