from django.urls import URLPattern, path 
from . import views
urlpatterns = [
    path('django', views.showCourseOne),
    path('python', views.showCourseTwo),
]