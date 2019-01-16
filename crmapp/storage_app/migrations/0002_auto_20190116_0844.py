# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemstorage',
            options={'ordering': ('-name',), 'verbose_name_plural': 'storage'},
        ),
        migrations.AlterUniqueTogether(
            name='itemstorage',
            unique_together=set([('name', 'item_type')]),
        ),
    ]
