# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20150321_1425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlog',
            old_name='author',
            new_name='passwordLog',
        ),
        migrations.RenameField(
            model_name='userlog',
            old_name='password',
            new_name='usernameLog',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 14, 58, 53, 662725, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='set_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 21, 14, 58, 53, 662670, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
