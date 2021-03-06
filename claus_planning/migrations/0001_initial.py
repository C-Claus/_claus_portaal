# Generated by Django 3.0.6 on 2021-02-08 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('claus_personen', '0003_auto_20210204_1945'),
        ('claus_projecten', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField()),
                ('begintijd', models.TimeField()),
                ('eindtijd', models.TimeField()),
                ('status', models.CharField(choices=[('Actief', 'Actief'), ('Inactief', 'Inactief')], max_length=100)),
                ('persoon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claus_personen.Personen')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claus_projecten.Projecten')),
            ],
            options={
                'verbose_name_plural': 'Planningen',
            },
        ),
    ]
