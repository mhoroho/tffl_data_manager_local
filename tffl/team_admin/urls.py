from django.urls import path

from . import views
from django.conf.urls import url
urlpatterns = [
    path('', views.index, name='index'),
    path('super',views.admin_page,name='super'),
    url('Team/(?P<team_id>\d+)/',views.team,name='team'),
    url('unassign_player/(?P<team_id>\d+)/(?P<pid>\d+)/',views.unassign_user,name='unassign_player'),
    url('add_player/(?P<team_id>\d+)/',views.add_player,name='add_player'),
    url('reassign_pick/(?P<team_id>\d+)/',views.reassign_draft_pick,name='reassign_draft_pick'),
    url('create_player/(?P<team_id>\d+)/',views.create_player,name='create_player'),
]