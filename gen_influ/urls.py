from django.urls import path
from gen_influ.views import index
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('add_influencer/', views.add_influencer, name='add_influencer'),
    path('edit_influencer/', views.edit_influencer, name='edit_influencer'),
    path('delete_influencer/<int:id>/', views.delete_influencer, name='delete_influencer'),
]