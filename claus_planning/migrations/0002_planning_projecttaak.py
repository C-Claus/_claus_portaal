# Generated by Django 3.0.6 on 2021-02-08 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('claus_projecttaken', '0001_initial'),
        ('claus_planning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planning',
            name='projecttaak',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='claus_projecttaken.ProjectTaak'),
            preserve_default=False,
        ),
    ]
