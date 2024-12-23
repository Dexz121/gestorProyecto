# Generated by Django 5.0.9 on 2024-11-22 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Entregable",
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
                ("asunto", models.CharField(max_length=255)),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("Descartado", "Descartado"),
                            ("Bloqueado", "Bloqueado"),
                            ("En análisis", "En análisis"),
                            ("Pendiente", "Pendiente"),
                            ("En proceso", "En proceso"),
                            ("En pruebas", "En pruebas"),
                            ("Concluido", "Concluido"),
                        ],
                        max_length=50,
                    ),
                ),
                ("proyecto", models.CharField(max_length=255)),
                ("horas_estimadas", models.IntegerField()),
                ("horas_abarcadas", models.IntegerField()),
                ("fecha_inicio", models.DateField()),
                ("fecha_entrega", models.DateField(blank=True, null=True)),
                ("fecha_finalizacion", models.DateField()),
                ("descripcion", models.TextField()),
                ("comentarios", models.TextField()),
                ("persona_asignada", models.IntegerField()),
            ],
        ),
    ]
