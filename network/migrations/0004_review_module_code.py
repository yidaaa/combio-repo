# Generated by Django 3.1 on 2020-12-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_module_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='module_code',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
