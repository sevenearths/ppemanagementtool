# Generated by Django 2.2.7 on 2020-04-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_inventory_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='supplies_left',
            field=models.CharField(choices=[('?', 'Unknown'), ('1', '1 day'), ('2', '2 days'), ('2-3', '2-3 days'), ('>3', '3 or more days')], max_length=3),
        ),
    ]