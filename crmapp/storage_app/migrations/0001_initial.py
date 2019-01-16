# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemStorage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField(max_length=100)),
                ('item_type', models.PositiveSmallIntegerField(choices=[(1, b'Rings'), (2, b'Necklace'), (3, b'Other')])),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'storage',
            },
            bases=(models.Model,),
        ),
    ]
