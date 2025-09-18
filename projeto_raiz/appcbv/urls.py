from django.urls import path
from .views import HelloView, CachorroListView

urlpatterns = [
    path("hello/",HelloView.as_view(),name='index'),
    path("",CachorroListView.as_view(),name='listar_cachorros'),
]