from django.urls import path

from . import views

app_name = "item"

urlpatterns = [
    path("<int:item_id>/", views.detail, name="detail"),
    path("new/", views.new_item, name="new_item"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("edit/<int:pk>/", views.edit, name="edit"),
]
