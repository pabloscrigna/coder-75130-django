# Generated by Django 5.1.4 on 2025-01-07 22:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appCoder", "0002_curso_creado_alter_curso_nombre"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profesor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=20)),
                ("apellido", models.CharField(max_length=20)),
                ("edad", models.IntegerField()),
                ("creado", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
