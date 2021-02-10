from rest_framework.routers import SimpleRouter
from .views import ArtworkViewset

router = SimpleRouter()
router.register('', ArtworkViewset, basename='artwork')

urlpatterns = router.urls
