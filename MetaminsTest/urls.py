from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from client.views import ClientViewSet
from transaction.views import TransactionViewSet
from django.conf.urls import include, url

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'Transactions', TransactionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
]
