# Generated by Django 2.2 on 2021-02-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210216_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='objective',
            field=models.CharField(choices=[('complaint', 'Complaint'), ('suggestion', 'Suggestion')], max_length=50),
        ),
    ]