from rest_framework.routers import DefaultRouter

from applications.review.views import RatingViewSet

router = DefaultRouter()
router.register('', RatingViewSet)

urlpatterns = []
urlpatterns.extend(router.urls)
