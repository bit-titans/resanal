# Generated by Django 2.1.5 on 2019-03-14 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resanal', '0013_auto_20181007_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fetch',
            name='usn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maping', to='resanal.Result'),
        ),
    ]