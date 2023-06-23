from django import forms
from .models import ProductList, DeviceList

# 商品追加用FORM
class ProductAddForm(forms.ModelForm):
    class Meta:
        model = ProductList # 参照するTABLE_NAME
        fields = ("product_cd", "jan_cd", "product_name", "price_ex", "price_in")
        """
        fields = (
            "product_cd", "jan_cd", "product_name", "display_name",
            "price_ex", "price_in", "retail_ex", "retail_in", "description")
        """

# 商品編集用FORM
class ProductEditForm(forms.ModelForm):
    class Meta:
        model = ProductList # 参照するTABLE_NAME
        fields = ("jan_cd", "product_name", "price_ex", "price_in")

# 検索用FORM
class ProductSearchForm(forms.Form):
    product_name = forms.CharField(label="商品名", required=False, widget=forms.TextInput(attrs={'class': "search-form"}))
    product_cd = forms.IntegerField(label="商品CD", required=False)
    jan_cd = forms.IntegerField(label="JAN-CD", required=False)

# ソート用FORM
class SortForm(forms.Form):
    terms_list = [
        ("product_cd", "商品CD"),
        ("jan_cd", "JAN-CD"),
        ("product_name", "商品名"),
        ("price_in", "税込価格"),
        ]
    sort_choice = forms.ChoiceField(label="ソート条件", choices=terms_list, widget=forms.widgets.RadioSelect)

# デバイス追加用FORM
class DeviceAddForm(forms.ModelForm):
    class Meta:
        model = DeviceList
        fields = ("device_cd", "device_mac")

# デバイス選択用FORM
class DeviceChoiceForm(forms.Form):
    device_list = [
        (i.device_cd, i.device_cd) for i in DeviceList.objects.all()]
    device_choiced = forms.MultipleChoiceField(choices=device_list, widget=forms.widgets.SelectMultiple)