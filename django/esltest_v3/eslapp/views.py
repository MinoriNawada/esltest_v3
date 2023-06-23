import os

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.decorators.http import require_POST

from eslapp.models import ProductList, DeviceList
from eslapp.forms import ProductAddForm, ProductEditForm, ProductSearchForm, SortForm, DeviceAddForm
import eslapp.forms

import eslapp.views_modules.makeESLimg as makeESLimg
from eslapp.views_modules.mqttESLGateway import mqttESLGateway
from eslapp.views_modules.mqttESLGateway_run import mqttESLGateway_run
from eslapp.views_modules import module

def top(request):      
    products = ProductList.objects.order_by("-created_at")
    # READ SEARCH FORM
    search_form = ProductSearchForm(request.GET)
    # READ SortForm
    sort_form = SortForm(request.GET)

    if sort_form.is_valid():
        selected_choice = sort_form.cleaned_data.get("sort_choice")
        if selected_choice:
            products = ProductList.objects.order_by(selected_choice)

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

    # RETURN ITEMS
    send = {"products": products,
            "search_form": search_form,
            "sort_form": sort_form
            }
    
    return TemplateResponse(request, "eslapp/top.html", send)


def add_product(request):
    # 商品データの追加と保存
    if request.method == "POST":
        form = ProductAddForm(request.POST)
        print("るん1")
        if form.is_valid():
            form.save()
            print("るん2")
        # 画像の生成と保存
        img = makeESLimg.make213_01_01(request.POST["product_cd"],
                           request.POST["jan_cd"],
                           request.POST["product_name"],
                           request.POST["price_ex"],
                           request.POST["price_in"]
                           )
        img.save("eslapp/static/images/"+request.POST["product_cd"]+".png")

        send = {"product_cd": request.POST["product_cd"],
                "product_name": request.POST["product_name"],
                "page_name_1": "商品の追加 /",
                "page_name_2": "成功"}
        return TemplateResponse(request, "eslapp/add_success.html", send)
        # return  HttpResponse(ProductAddForm(request.POST))

    else:
        form = ProductAddForm()
    print("るん3")
    # RETURN ITEMS
    send = {"form": form,
            "page_name_1": "商品の追加",
            }
    return TemplateResponse(request, "eslapp/add.html", send)



def add_success(request, pd_id):
    try:
        product = ProductList.objects.get(product_cd=pd_id)
    except ProductList.DoesNotExist:
        raise Http404
    
    # RETURN ITEMS
    send = {"product": product,
            "page_name_1": "商品の追加 /",
            "page_name_2": "追加成功 /",
            }
    

def productdetail(request, pd_id):
    try:
        product = ProductList.objects.get(product_cd=pd_id)
    except ProductList.DoesNotExist:
        raise Http404
    send ={"product": product,
            "page_name_1": "商品詳細",
            }
    return TemplateResponse(request, "eslapp/detail.html", send)


def productedit(request, pd_id):
    try:
        product = ProductList.objects.get(product_cd=pd_id)
    except ProductList.DoesNotExist:
        raise Http404
    if request.method == "POST":
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        img = makeESLimg.make213_01_01(product.product_cd, request.POST["jan_cd"], 
                            request.POST["product_name"],
                            request.POST["price_ex"],request.POST["price_in"])
        img.save(f"eslapp/static/images/{product.product_cd}.png")
        return HttpResponseRedirect(reverse("detail",
                                            args=(product.product_cd,)))
    else:
        form = ProductEditForm(instance=product)
    
    send = {"form": form,
            "product": product,
            "page_name_1": "商品詳細 /",
            "page_name_2": "商品編集",
            }
    return TemplateResponse(request, "eslapp/edit.html", send)


def product_delete(request, pd_id):
    try:
        product = ProductList.objects.get(product_cd=pd_id)
    except ProductList.DoesNotExist:
        raise Http404
    os.remove(f"eslapp/images/{product.product_cd}.png")
    product.delete()
    return HttpResponseRedirect(reverse("top"))


def product_delete_caution(request, pd_id):
    try:
        product = ProductList.objects.get(product_cd=pd_id)
    except ProductList.DoesNotExist:
        raise Http404
    send = {"product": product,
            "page_name_1": "商品詳細 /",
            "page_name_2": "商品削除",
            }
    return TemplateResponse(request, "eslapp/delete_caution.html", send)

def batch_delete(request):
    if request.method == "POST":
        post_pks = request.POST.getlist("batch_delete")
        ProductList.objects.filter(product_cd__in=post_pks).delete()
        return HttpResponseRedirect(reverse("top"))
    
    send = {"products": ProductList.objects.order_by("-created_at"),
            "page_name_1": "一括削除",}
    return TemplateResponse(request, "eslapp/batch_delete.html", send)

def batch_delete_caution(request, post_pks):
    if request.method == "POST":
        ProductList.objects.filter(product_cd__in=post_pks).delete()
        return HttpResponseRedirect(reverse("top"))


def test(request):
    form = SortForm()
    send = {"form": form,
            "page_name_1": "一括削除",
            }
    return TemplateResponse(request, "eslapp/html_test.html", send)

def add_device(request):
    # 商品データの追加と保存
    if request.method == "POST":
        form = DeviceAddForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("top"))
    else:
        form = DeviceAddForm()
        
    # RETURN ITEMS
    send = {"form": form,
            "page_name_1": "デバイスの追加",
            }
    return TemplateResponse(request, "eslapp/add_device.html", send)

def change_esl(request, pd_id):
    try:
        product = ProductList.objects.get(product_cd=pd_id)
    except ProductList.DoesNotExist:
        raise Http404
    mqttESLGateway(pd_id)
    return HttpResponseRedirect(reverse("top"))


def set_device(request, pd_id):
    try:
        product = ProductList.objects.get(product_cd=pd_id)
    except ProductList.DoesNotExist:
        raise Http404
    
    devices = DeviceList.objects.order_by("device_cd")
    form = eslapp.forms.DeviceChoiceForm(request.GET)
        
    if request.method == "POST":
        choiced_device = request.POST["device_choiced"]
        device = DeviceList.objects.get(device_cd=choiced_device)
        send = {
            "product": product,
            "device": device,
        }
        mqttESLGateway_run(product.product_cd, device.device_cd, device.device_mac)
        return HttpResponseRedirect(reverse("top"))
        
    
    # RETURN ITEMS
    send = {
        "product": product,
        "devices": devices,
        "form": form,}
    return TemplateResponse(request, "eslapp/set_device.html", send)


