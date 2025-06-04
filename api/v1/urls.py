from rest_framework.routers import SimpleRouter
from apps.filterApp.api.v1.views import MemberViewSet

router = SimpleRouter()
router.register("members", MemberViewSet)

urlpatterns = [] + router.urls
