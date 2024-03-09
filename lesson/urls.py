from django.urls import path
from lesson.apps import LessonConfig
from lesson.views import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = LessonConfig.name

urlpatterns = [
    path('create/', LessonCreateAPIView.as_view(), name='create'),
    path('list/', LessonListAPIView.as_view(), name='list'),
    path('view/<int:pk>/', LessonRetrieveAPIView.as_view(), name='view'),
    path('update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete'),
]
