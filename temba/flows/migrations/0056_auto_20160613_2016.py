# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0055_populate_step_broadcasts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruleset',
            name='ruleset_type',
            field=models.CharField(help_text='The type of ruleset', max_length=16, null=True, choices=[('wait_message', 'Wait for message'), ('wait_recording', 'Wait for recording'), ('wait_digit', 'Wait for digit'), ('wait_digits', 'Wait for digits'), ('webhook', 'Webhook'), ('resthook', 'Zapier'), ('flow_field', 'Split on flow field'), ('contact_field', 'Split on contact field'), ('expression', 'Split by expression')]),
        ),
    ]
