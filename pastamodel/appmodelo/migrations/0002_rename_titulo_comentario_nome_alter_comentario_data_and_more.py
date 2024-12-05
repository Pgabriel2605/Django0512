# Generated by Django 5.1.4 on 2024-12-05 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmodelo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='titulo',
            new_name='nome',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='data',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='hora',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
