# Generated by Django 3.2.6 on 2022-03-01 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_class_suggesstion_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_suggesstion',
            name='date',
            field=models.DateField(),
        ),
    ]