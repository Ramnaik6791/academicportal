# Generated by Django 3.2.7 on 2021-10-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0003_termin_course_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='planning',
            name='course_no',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
