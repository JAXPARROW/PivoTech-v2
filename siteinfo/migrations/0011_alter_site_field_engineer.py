# Generated by Django 3.2.12 on 2022-03-13 19:58

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0010_alter_site_field_engineer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='field_engineer',
            field=smart_selects.db_fields.GroupedForeignKey(group_field='Clster', null=True, on_delete=django.db.models.deletion.CASCADE, to='siteinfo.fe'),
        ),
    ]
