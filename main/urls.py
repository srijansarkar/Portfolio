from django.urls import path
from main import views
urlpatterns=[
    path('projects/',views.projects,name='projects' ),
    path('language/',views.language,name='language'),
    path('',views.index,name='index')
]