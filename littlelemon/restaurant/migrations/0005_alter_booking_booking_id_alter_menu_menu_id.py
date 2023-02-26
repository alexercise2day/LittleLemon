# Generated by Django 4.1.7 on 2023-02-26 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0004_remove_booking_id_remove_menu_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="booking_id",
            field=models.IntegerField(
                db_column="booking_id",
                default=None,
                primary_key=True,
                serialize=False,
                verbose_name=11,
            ),
        ),
        migrations.AlterField(
            model_name="menu",
            name="menu_id",
            field=models.IntegerField(
                db_column="menu_id",
                default=None,
                primary_key=True,
                serialize=False,
                verbose_name=5,
            ),
        ),
    ]