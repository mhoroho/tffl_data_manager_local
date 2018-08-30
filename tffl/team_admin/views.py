from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Teams, Players, Draft_Picks

@login_required(login_url='/login')
def index(request):
    d = Teams.objects.all()
    t = {
        "d": d
    }
    return render_to_response('team_admin/index.html',t)

@login_required(login_url='/login')
def team(request,team_id):
    x = team_id

    t = Players.objects.filter(team_id=x).order_by('position_id')
    u = Players.objects.filter(team_id=0)
    pick_query = '''select b.team_name as team, a.year,a.round,c.team_name as owner,a.id
                        from draft_picks a join (select team_id, team_name from teams) b
                        on a.team_id = b.team_id
                        join (select team_id, team_name from teams) c
                        on a.owner_id = c.team_id
                        where a.team_id = ''' + x + ' order by 2,3'

    other_picks_query = '''select b.team_name as team, a.year,a.round,c.team_name as owner,a.id
                        from draft_picks a join (select team_id, team_name from teams) b
                        on a.team_id = b.team_id
                        join (select team_id, team_name from teams) c
                        on a.owner_id = c.team_id
                        where a.team_id <> ''' + x + ' and a.owner_id =  ' + x + ' order by 2,3'

    picks = Draft_Picks.objects.raw(pick_query)
    other_picks = Draft_Picks.objects.raw(other_picks_query)
    teams = Teams.objects.all()

    y = {
        "t": t,
        "u":u,
        "x":x,
        "picks":picks,
        "teams":teams,
        "other_picks":other_picks,

    }
    return render(request,'team_admin/team.html',y)

@login_required(login_url='/login')
@user_passes_test(lambda u: u.is_superuser,login_url='/teams')

def admin_page(request):
    return HttpResponse("You're Super!")


def unassign_user(request,team_id,pid):
    Players.objects.filter(player_id=pid).update(team_id=0)
    re_dir_url = '/teams/Team/' + team_id
    #re_dir_url = 'goolge.com'

    return redirect(re_dir_url)

def add_player(request,team_id):
    x = team_id
    player = request.POST['player']
    Players.objects.filter(player_id=player).update(team_id=x)

    re_dir_url = '/teams/Team/' + x
    return redirect(re_dir_url)

def reassign_draft_pick(request,team_id):
    x = team_id
    pick = request.POST['pick']
    new_team = request.POST['team']
    Draft_Picks.objects.filter(id=pick).update(owner_id=new_team)
    re_dir_url = '/teams/Team/' + x
    return redirect(re_dir_url)

def create_player(request,team_id):
    x = team_id
    postion_ids = {'QB': 1,'RB':2,'WR':3,'TE':4,'K':5,'DEF':6}
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    position = request.POST['position']

    new_player = Players()
    new_player.first_name = first_name
    new_player.last_name = last_name
    new_player.position = position
    new_player.team_id = 0
    new_player.position_id = postion_ids[position]
    new_player.save()
    re_dir_url = '/teams/Team/' + x

    return redirect(re_dir_url)