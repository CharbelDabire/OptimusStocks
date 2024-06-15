from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StockViewSet, UserViewSet, PortfolioViewSet, QuestionViewSet, AnswerViewSet, PredictionViewSet, UnderstandingLevelViewSet

router = DefaultRouter()
router.register(r'stocks', StockViewSet)
router.register(r'users', UserViewSet)
router.register(r'portfolios', PortfolioViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'predictions', PredictionViewSet)
router.register(r'understandingLvl', UnderstandingLevelViewSet)

# URLConf
urlpatterns = [
    path('', include(router.urls)),
]
