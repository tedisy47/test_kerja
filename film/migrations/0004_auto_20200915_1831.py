# Generated by Django 3.1.1 on 2020-09-15 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0003_auto_20200915_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geenre',
            old_name='geenre_title',
            new_name='geenre',
        ),
    ]