# Generated by Django 2.2.9 on 2020-08-19 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Psicologo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numCRP', models.IntegerField(verbose_name='CRP')),
                ('formacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formacao.Formacao')),
            ],
        ),
    ]