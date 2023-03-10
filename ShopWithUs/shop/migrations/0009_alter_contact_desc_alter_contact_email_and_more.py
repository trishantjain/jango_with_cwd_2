# Generated by Django 4.1.2 on 2023-02-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0008_alter_contact_desc_alter_contact_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="desc",
            field=models.CharField(default="", max_length=700),
        ),
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.CharField(default="", max_length=70),
        ),
        migrations.AlterField(
            model_name="contact",
            name="name",
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name="contact",
            name="phone",
            field=models.CharField(default="", max_length=70),
        ),
        migrations.AlterField(
            model_name="order",
            name="address",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="order",
            name="city",
            field=models.CharField(default="", max_length=70),
        ),
        migrations.AlterField(
            model_name="order",
            name="email",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="order",
            name="item_json",
            field=models.CharField(default="", max_length=70),
        ),
        migrations.AlterField(
            model_name="order",
            name="name",
            field=models.CharField(default="", max_length=70),
        ),
        migrations.AlterField(
            model_name="order",
            name="phone",
            field=models.CharField(default="", max_length=70),
        ),
        migrations.AlterField(
            model_name="order",
            name="state",
            field=models.CharField(default="", max_length=70),
        ),
        migrations.AlterField(
            model_name="order",
            name="zip_code",
            field=models.CharField(default="", max_length=70),
        ),
        migrations.AlterField(
            model_name="orderupdate",
            name="update_desc",
            field=models.CharField(default="", max_length=5000),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_name",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="product",
            name="subcategory",
            field=models.CharField(default="", max_length=50),
        ),
    ]
