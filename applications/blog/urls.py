from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import QuestionCreateView, QuestionListView, QuestionUpdateView, QuestionDeleteView, AnswerViewSet

router = DefaultRouter()
router.register('answers', AnswerViewSet)

urlpatterns = [
    path('question-create/', QuestionCreateView.as_view()),
    path('questions-list/', QuestionListView.as_view()),
    path('question-update/<int:pk>/', QuestionUpdateView.as_view()),
    path('question-delete/<int:pk>/', QuestionDeleteView.as_view()),
    path('answer/', include(router.urls)),
]
