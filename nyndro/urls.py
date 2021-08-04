from django.urls import path
from . import views
from nyndro.views import PracticeListView, PracticeHistoryListView

app_name = 'nyndro'
urlpatterns = [
    path('', PracticeListView.as_view(), name='practice_list'),
    path('<int:practice_id>/', views.practice_detail, name='practice_detail'),
    path('<int:practice_id>/practice_history/', PracticeHistoryListView.as_view(), name='practice_history_list'),
]