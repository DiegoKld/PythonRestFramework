# Generated by Django 4.0.2 on 2022-05-03 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['first_name'], 'verbose_name': 'Personal de la empresa', 'verbose_name_plural': 'Personal'},
        ),
        migrations.AlterField(
            model_name='empleado',
            name='job',
            field=models.CharField(choices=[('0', 'Contador'), ('1', 'Administrador'), ('2', 'Economista'), ('3', 'Operaciones'), ('4', 'Proyectos'), ('5', 'Otro')], max_length=50, verbose_name='Trabajo'),
        ),
        migrations.AlterUniqueTogether(
            name='empleado',
            unique_together={('first_name', 'last_name')},
        ),
    ]
