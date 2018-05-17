from django.conf.urls import url
from simple_app import views

app_name = 'simple_app'

urlpatterns = [
    url(r'^$',views.SchoolListView.as_view(),name='list'),
    url(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='detail')
]