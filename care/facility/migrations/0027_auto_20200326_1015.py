# Generated by Django 2.2.11 on 2020-03-26 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0026_map_to_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='local_body',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.LocalBody'),
        ),
        migrations.AlterField(
            model_name='facility',
            name='new_district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.District'),
        ),
    ]
