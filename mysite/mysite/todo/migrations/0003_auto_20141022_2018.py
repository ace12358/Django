# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20141022_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default=b'\xe6\x8c\x87\xe5\xae\x9a\xe3\x81\xaa\xe3\x81\x97', unique=True, max_length=200),
        ),
    ]
