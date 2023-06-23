from django.urls import path

from . import views

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
    path("change_esl/<int:pd_id>", views.change_esl,
         name="change_esl"),
    path("<int:pd_id>/setdevice/", views.set_device,
         name="set_device"),
]
