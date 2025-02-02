# Generated by Django 5.1.4 on 2025-01-22 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Table",
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
                ("number", models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name="order",
            name="all_price",
        ),
        migrations.AddField(
            model_name="orderdetail",
            name="price",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="orderdetail",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="details",
                to="order.order",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="table",
            field=models.ForeignKey(
                default=0, on_delete=django.db.models.deletion.CASCADE, to="order.table"
            ),
            preserve_default=False,
        ),
    ]
