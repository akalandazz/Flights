# Generated by Django 3.0.3 on 2020-02-29 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_app', '0005_auto_20200229_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='reisi',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='hello_app.Flight'),
        ),
    ]