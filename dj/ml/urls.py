from django.urls import path
from . import views


urlpatterns = [
    path('', views.inputdata, name='inputdata'),
    # 결과가 어떻게 나오게 하는지
    path('ml_result/', views.ml_result, name='ml_result'),
]
