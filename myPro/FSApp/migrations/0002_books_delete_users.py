# Generated by Django 4.1.2 on 2022-10-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FSApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Books",
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
                ("title", models.CharField(max_length=20)),
                ("author", models.CharField(max_length=20)),
                ("Desc", models.TextField()),
                ("img", models.CharField(max_length=20)),
                ("price", models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(name="Users",),
    ]
