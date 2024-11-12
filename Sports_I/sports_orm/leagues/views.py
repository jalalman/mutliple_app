from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):
	context = {
		
		"baseLeague":League.objects.filter(sport="Baseball"),
		"womenLeague":League.objects.filter(name__icontains='Womens'),
		"hockeyleague":League.objects.filter(sport__icontains='Hockey'),
		"league_exclude_football":League.objects.exclude(sport__icontains='football'),
		"conference_leagues": League.objects.filter(name__icontains="Conference"),
		"althanic_regoin":League.objects.filter(name__icontains="atlantic"),
		"dallas_teams":Team.objects.filter(location__icontains='Dallas'),
		"raptors_teams":Team.objects.filter(team_name__icontains='Raptors'),
		"city_teams":Team.objects.filter(location__icontains="City"),
		"T_teams":Team.objects.filter(team_name__startswith='T'),
		"teams_ordered_location":Team.objects.all().order_by("location"),
		"name_reverse_ordered_teams": Team.objects.all().order_by("-team_name"),
		"cooper_player": Player.objects.filter(last_name__icontains="Cooper"),
		"Joshua_player": Player.objects.filter(first_name__icontains="Joshua"),
		"cooper_joshua_players": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		'alexander_wyatt_players': Player.objects.filter( Q(first_name="Alexander") | Q(first_name="Wyatt"))

	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")