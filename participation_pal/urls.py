from django.contrib import admin
from django.urls import path

from participation_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('student/<slug:pk>', views.StudentView.as_view(), name='student'),
    path('chosen', views.ChosenView.as_view(), name='chosen'),
]
