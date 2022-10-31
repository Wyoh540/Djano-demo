from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'polls'

router = routers.DefaultRouter()
router.register(r'question', views.ViewQuestion)
# router.register(r'test', views.test_apt, basename='test')

urlpatterns = [
    # ex: /polls/
    path('', include(router.urls)),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('test/', views.test_apt, name='test')
    # api
    # path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
