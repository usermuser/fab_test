from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PollsView

router = DefaultRouter()
router.register(r'')

app_name = 'poll_app'
urlpatterns = router.urls
# todo get rid of unused code
# urlpatterns = [
#     path('v1/polls/<int:pk>', ),
#     path('v1/polls/', ),
# ]

