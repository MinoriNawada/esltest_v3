from django.db import models
from django.utils.timezone import now


class ProductList(models.Model):
    # product_cd = models.IntegerField("商品コード", primary_key=True, default=111111)
    product_cd = models.CharField("商品コード", max_length=100, primary_key=True, default=111111)
    # jan_cd = models.IntegerField("JANコード", null=True, blank=True, default=4973007525936)
    jan_cd = models.CharField("JANコード", max_length=100, null=True, blank=True, default=4973007525936)
    product_name = models.CharField("商品名", max_length=100, null=True, blank=True, default="商品名るん")
    display_name = models.CharField("表示名", max_length=100, null=True, blank=True)
    price_ex = models.IntegerField("税抜き価格", null=True, blank=True, default=1000)
    price_in = models.IntegerField("税込み価格", null=True, blank=True, default=1100)
    retail_ex = models.FloatField("税抜き店舗売価", null=True, blank=True)
    retail_in = models.IntegerField("税込み店舗売価", null=True, blank=True)
    description = models.TextField("商品説明", null=True, blank=True)
    created_at = models.DateTimeField("データ追加日", default=now)

    class Meta:
        db_table = "ProductList"


class DeviceList(models.Model):
    device_cd = models.CharField(primary_key=True, max_length=8)
    device_mac = models.CharField(max_length=16)
    created_at = models.DateTimeField("デバイス追加日", default=now)

    class Meta:
        db_table = "DeviceList"

class TemplateList(models.Model):
    inch = models.CharField(max_length=8)
    module_name = models.CharField(primary_key=True, max_length=50)
    readable_name = models.CharField(max_length=50)

    class Meta:
        db_table = "TemplateList"