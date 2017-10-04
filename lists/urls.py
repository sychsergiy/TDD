from django.conf.urls import url

from . import views as lists_views

urlpatterns = [
    url(r'^(?P<list_id>\d+)/$', lists_views.view_list, name='view_list'),
    url(r'^(\d+)/add_item$', lists_views.add_item, name='add_item'),
    url(r'^new$', lists_views.new_list, name='new_list'),
]
