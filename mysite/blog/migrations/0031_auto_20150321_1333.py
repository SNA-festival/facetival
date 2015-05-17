# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20150114_1526'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LoginM',
            new_name='Userlog',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 12, 33, 17, 83983, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='set_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 21, 12, 33, 17, 83939, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
