# Generated by Django 2.2.7 on 2020-04-02 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ref', models.CharField(max_length=30)),
                ('diaplay_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('ref', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levels', models.PositiveIntegerField()),
                ('supplies_left', models.CharField(choices=[('1', '1 day'), ('2', '2 days'), ('2-3', '2-3 days'), ('>3', '3 or more days')], max_length=3)),
                ('other', models.CharField(blank=True, max_length=255, null=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Stock')),
            ],
        ),
    ]