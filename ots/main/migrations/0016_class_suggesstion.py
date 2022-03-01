# Generated by Django 3.2.6 on 2022-03-01 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20220218_0257'),
    ]

    operations = [
        migrations.CreateModel(
            name='class_suggesstion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.IntegerField(choices=[(1, 'Class One'), (2, 'Class Two'), (3, 'Class Three'), (4, 'Class Four'), (5, 'Class Five'), (6, 'Class Six'), (7, 'Class Seven'), (8, 'Class Eight'), (9, 'Class Nine'), (10, 'Class Ten')], default=None, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('suggesstion', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]