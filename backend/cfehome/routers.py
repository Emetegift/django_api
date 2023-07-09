from rest_framework.routers import DefaultRouter

from products.viewset import ProuductViewSet

router=DefaultRouter()
router.register('product', ProuductViewSet, basename='products')

urlpatterns=router.urls
