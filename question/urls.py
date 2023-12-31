from django.urls import include, path
from rest_framework import routers
from .views import QuestionViewSet

router = routers.DefaultRouter()
router.register(r'', QuestionViewSet)
urlpatterns = router.urls
