from django.core.paginator import Paginator

from eslapp.models import ProductList
from eslapp.forms import ProductSearchForm

def db_page(request):
    # READ DB
    products = ProductList.objects.order_by("-created_at")
    # READ SEARCH FORM
    search_form = ProductSearchForm(request.GET)

    # 検索機能の実装
    if search_form.is_valid():
        product_name = search_form.cleaned_data.get("product_name")
        product_cd = search_form.cleaned_data.get("product_cd")
        jan_cd = search_form.cleaned_data.get("jan_cd")
        if product_name:
            products = products.filter(product_name__contains=product_name)
        if product_cd:
            products = products.filter(product_cd__contains=product_cd)
        if jan_cd:
            products = products.filter(jan_cd__contains=jan_cd)

    # ページ送り機能の実装
    paginator = Paginator(products, 20)
    page = request.GET.get("page", 1)
    products = paginator.page(page)

    return products