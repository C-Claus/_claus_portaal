# Generated by Django 3.0.6 on 2021-03-23 19:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('claus_administratie', '0001_initial'),
        ('claus_projecttaken', '0001_initial'),
        ('claus_kostencodes', '0001_initial'),
        ('claus_projecten', '0001_initial'),
        ('claus_personen', '0004_personen_persoon_guid'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrenRegistratie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField(default=django.utils.timezone.now)),
                ('aantal_uur', models.FloatField()),
                ('opmerking', models.CharField(blank=True, max_length=500)),
                ('registratie_status', models.CharField(choices=[('Ingevoerd', 'Ingevoerd'), ('Bevestigd', 'Bevestigd'), ('Goedgekeurd', 'Goedgekeurd'), ('Afgekeurd', 'Afgekeurd'), ('Verwerkt', 'Verwerkt')], max_length=50)),
                ('bedrijfsadministratie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='claus_administratie.BedrijfsAdministratie')),
                ('geaccordeerd_door', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='urenregistratie_geaccordeerd_door', to='claus_personen.Personen')),
                ('ingevoerd_door', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urenregistratie_ingevoerd_door', to='claus_personen.Personen')),
                ('kostencode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claus_kostencodes.KostenCode')),
                ('persoonnr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claus_personen.Personen')),
                ('projectnr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='claus_projecten.Projecten')),
                ('projecttaaknummer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='claus_projecttaken.ProjectTaak')),
            ],
            options={
                'verbose_name_plural': 'UrenRegistratie',
            },
        ),
    ]
