# Generated by Django 2.2 on 2021-02-16 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210216_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Company'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Country'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='objective',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Objective'),
        ),
    ]