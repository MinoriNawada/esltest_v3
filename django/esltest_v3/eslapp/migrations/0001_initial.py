# Generated by Django 4.2.1 on 2023-06-22 06:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DeviceList",
            fields=[
                (
                    "device_cd",
                    models.CharField(max_length=8, primary_key=True, serialize=False),
                ),
                ("device_mac", models.CharField(max_length=16)),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="デバイス追加日"
                    ),
                ),
            ],
            options={
                "db_table": "DeviceList",
            },
        ),
        migrations.CreateModel(
            name="ProductList",
            fields=[
                (
                    "product_cd",
                    models.IntegerField(
                        default=111111,
                        primary_key=True,
                        serialize=False,
                        verbose_name="商品コード",
                    ),
                ),
                (
                    "jan_cd",
                    models.IntegerField(
                        blank=True,
                        default=4973007525936,
                        null=True,
                        verbose_name="JANコード",
                    ),
                ),
                (
                    "product_name",
                    models.CharField(
                        blank=True,
                        default="商品名るん",
                        max_length=100,
                        null=True,
                        verbose_name="商品名",
                    ),
                ),
                (
                    "display_name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="表示名"
                    ),
                ),
                (
                    "price_ex",
                    models.IntegerField(
                        blank=True, default=1000, null=True, verbose_name="税抜き価格"
                    ),
                ),
                (
                    "price_in",
                    models.IntegerField(
                        blank=True, default=1100, null=True, verbose_name="税込み価格"
                    ),
                ),
                (
                    "retail_ex",
                    models.FloatField(blank=True, null=True, verbose_name="税抜き店舗売価"),
                ),
                (
                    "retail_in",
                    models.IntegerField(blank=True, null=True, verbose_name="税込み店舗売価"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="商品説明"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="データ追加日"
                    ),
                ),
            ],
            options={
                "db_table": "ProductList",
            },
        ),
    ]