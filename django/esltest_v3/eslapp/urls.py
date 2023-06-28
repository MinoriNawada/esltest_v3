from django.urls import path

from .views import views, mobile, setitem

urlpatterns = [
    path("", views.top,
         name="top"),
    path("add/", views.add_product,
         name="add_product"),
    path("add/success/", views.add_success,
         name="add_success"),
    path("<int:pd_id>/", views.productdetail,
         name="detail"),
    path("<int:pd_id>/edit/", views.productedit,
         name="product_edit"),
    path("<int:pd_id>/rundelete/", views.product_delete,
         name="product_delete"),
    path("<int:pd_id>/delete/", views.product_delete_caution,
         name="product_delete_caution"),
    path("batch_delete/", views.batch_delete,
         name="batch_delete"),
    path("batch_delete/caution/", views.batch_delete_caution,
         name="batch_delete_caution"),
    path("test/", views.test,
         name="test"),
    path("add_device/", views.add_device,
         name="add_device"),
    path("add_template/", views.add_template,
         name="add_template"),
    path("change_esl/<int:pd_id>", views.change_esl,
         name="change_esl"),
    # ==============================================================
    # Set Device to Item
    path("<int:pd_id>/setdevice/", views.set_device,
         name="set_device"),

    # views.setimtem.py
    # ==============================================================
    # Set Item to Device
    path("<str:device_id>/set/", setitem.set_item,
         name="set_item"),

    # モバイルアプリへのリンク
    # ==============================================================
    path("jump/", views.JumpMobile,
         name="jumpmobile"),
    # モバイルアプリ
    # ==============================================================
    path("mobile/", mobile.Mobile,
         name="Mobile"),
    path("mobile/<str:device_id>/set/", mobile.set_item,
         name="set_item_mobile"),
]
