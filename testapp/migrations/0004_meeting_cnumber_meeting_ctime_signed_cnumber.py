# Generated by Django 4.2.1 on 2023-05-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_meeting_remove_signed_cauther_remove_signed_cdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='cNumber',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='meeting',
            name='cTime',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='signed',
            name='cNumber',
            field=models.CharField(default='', max_length=50),
        ),
    ]