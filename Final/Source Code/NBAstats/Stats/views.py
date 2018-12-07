# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse
from .models import Player
from .models import Team
from .models import Matchup
from .models import Locations
from .models import Teamlocations
from .models import Playoffs
def index(request):
    return render(request, 'Stats/index.html')
    #return HttpResponse(x)
# Create your views here.
def teamsNBA(request):
    return render(request, 'Stats/nbaTeams.html')
def login(request):
    return render(request,'Stats/login.html')

def register(request):
    return render(request,'Stats/register.html')

def badPage(request):
    return render(request,'Stats/404.html')

def blank(request):
    return render(request,'Stats/blank.html')

def charts(request):
    return render(request,'Stats/charts.html')
def Champions(request):
    query = "SELECT 1 id,t_name FROM TEAM INNER JOIN PLAYOFFS ON po_teamID = t_id WHERE po_wonChampionship = 'TRUE'"
    champ = []
    for c in Team.objects.raw(query):
        champ.append(c)

    args = {'champion': champ}
    return render(request, 'Stats/Champions.html', args)
def forgot(request):
    return render(request,'Stats/forgot-password.html')
def playoffs(request):
    query = "SELECT 1 id, t_name, po_wins, po_loss, po_wonChampionship FROM PLAYOFFS INNER JOIN TEAM ON t_id = po_teamID"
    play = []
    for p in Playoffs.objects.raw(query):
        play.append(p)
    args = {'playoffTeams': play}
    return render(request,'Stats/Playoff.html', args)
def tables(request):
    all_players = Player.objects.all()
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds, p_abr FROM PLAYER"
    q = []

    for p in Player.objects.raw(query):
        q.append(p)

    args = {'playerList' : q}
    return render(request,'Stats/tables.html', args)

def teamtables(request):
    all_teams = Team.objects.all()
    query = "SELECT 1 id, t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/teamtables.html', args)

def limitEntriestoTenforTeam(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team LIMIT 10"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/10Entry', args)
def limitEntriesto25forTeam(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team LIMIT 25"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/25Entry', args)

def limitEntriesto50forTeam(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team LIMIT 50"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/50Entry', args)

def sortByTeamNameASC(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team ORDER BY t_name ASC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}


    return render(request, 'Stats/orderByName', args)

def sortByTeamNameDESC(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team ORDER BY t_name DESC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}


    return render(request, 'Stats/orderByName', args)

def sortByTeamWinsASC(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team ORDER BY t_wins ASC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}


    return render(request, 'Stats/orderByWins', args)

def sortByTeamWinsDESC(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team ORDER BY t_wins DESC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}


    return render(request, 'Stats/orderByWins', args)

def sortByTeamLossesDESC(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team ORDER BY t_loss DESC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}


    return render(request, 'Stats/orderByLosses', args)

def sortByTeamLossesASC(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team ORDER BY t_loss ASC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}


    return render(request, 'Stats/orderByLosses', args)

def sortByTeamRatioASC(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team ORDER BY t_ratio ASC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}


    return render(request, 'Stats/orderByRatio', args)

def sortByTeamRatioDESC(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team ORDER BY t_ratio DESC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}


    return render(request, 'Stats/orderByRatio', args)

def sortByTeamFieldGoalDESC(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team ORDER BY t_fgp DESC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}


    return render(request, 'Stats/orderByFGP', args)

def sortByTeamFieldGoalASC(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team ORDER BY t_fgp ASC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}


    return render(request, 'Stats/orderByFGP', args)


def sortByTeam3PPDESC(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team ORDER BY t_3pp DESC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}


    return render(request, 'Stats/orderBy3pp', args)

def sortByTeam3PPASC(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team ORDER BY t_3pp ASC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}


    return render(request, 'Stats/orderBy3pp', args)

def sortByTeamABRDESC(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team ORDER BY t_abr DESC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}


    return render(request, 'Stats/orderByABR', args)

def sortByTeamABRASC(request):
    query = "SELECT 1 id,t_name, t_wins, t_loss, t_ratio, t_fgp, t_3pp, t_abr FROM team ORDER BY t_abr ASC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}


    return render(request, 'Stats/orderByABR', args)

def limitEntriestoTenforPlayers(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER LIMIT 10"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/10Entry', args)
def limitEntriesto25forPlayers(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER LIMIT 25"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/25Entry', args)

def limitEntriesto50forPlayers(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER LIMIT 50"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/50Entry', args)

def limitEntriesto100forPlayers(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER LIMIT 100"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/100Entry', args)

def sortByPlayerNameASC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER ORDER BY p_pname ASC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortByName', args)

def sortByPlayerNameDESC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER ORDER BY p_pname DESC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortByName', args)
def sortByPlayerPointsASC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER ORDER BY p_points ASC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortByPoints', args)
def sortByPlayerPointsDESC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER ORDER BY p_points DESC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortByPoints', args)
def sortByPlayerAGEASC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER ORDER BY p_age ASC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortByAge', args)

def sortByPlayerAgeDESC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER ORDER BY p_age DESC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortByAge', args)
def sortByPlayerAssistsDESC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER ORDER BY p_assists DESC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortByAssists', args)

def sortByPlayerAssistsASC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER ORDER BY p_assists ASC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortByAssists', args)

def sortByPlayerfppASC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER ORDER BY p_fgp ASC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortByfgp', args)
def sortByPlayerfppDESC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER ORDER BY p_fgp DESC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortByfgp', args)


def sortByPlayer3ppASC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER ORDER BY p_3pp ASC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortBy3fgp', args)

def sortByPlayer3ppDESC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER ORDER BY p_3pp DESC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortBy3fgp', args)

def sortByPlayerReboundsASC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER ORDER BY p_rebounds ASC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortByRB', args)

def sortByPlayerReboundsDESC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER ORDER BY p_rebounds DESC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortByRB', args)

def sortByPlayerteamASC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds,p_abr FROM PLAYER ORDER BY p_abr ASC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortByabr', args)

def sortByPlayerteamDESC(request):
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds,p_abr FROM PLAYER ORDER BY p_abr DESC"
    q = []

    for t in Team.objects.raw(query):
        q.append(t)

    args = {'teamList':q}
    return render(request, 'Stats/sortByabr', args)


def GoldenState(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Golden State Warriors'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Golden State Warriors'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Golden State Warriors')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_abr = 'GSW'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/GoldenState.html', args)

def Atlanta(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Atlanta Hawks'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Atlanta Hawks'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Atlanta Hawks')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Atlanta Hawks'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Atlanta.html', args)

def Boston(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Boston Celtics'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Boston Celtics'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Boston Celtics')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Boston Celtics'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Boston.html', args)

def Brooklyn(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Brooklyn Nets'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Brooklyn Nets'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Brooklyn Nets')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Brooklyn Nets'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Brooklyn.html', args)

def Charlotte(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Charlotte Hornets'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Charlotte Hornets'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Charlotte Hornets')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Charlotte Hornets'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Charlotte.html', args)

def Chicago(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Chicago Bulls'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Chicago Bulls'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Chicago Bulls')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Chicago Bulls'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Chicago.html', args)

def Cleveland(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Cleveland Cavaliers'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Cleveland Cavaliers'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Cleveland Cavaliers')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Cleveland Cavaliers'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Cleveland.html', args)

def Dallas(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Dallas Mavericks'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Dallas Mavericks'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Dallas Mavericks')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Dallas Mavericks'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Dallas.html', args)

def Denver(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Denver Nuggets'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Denver Nuggets'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Denver Nuggets')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Denver Nuggets'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Denver.html', args)

def Detroit(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Detroit Piston'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Detroit Piston'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Detroit Piston')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Detroit Piston'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Detroit.html', args)

def Houston(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Houston Rockets'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Houston Rockets'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Houston Rockets')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Houston Rockets'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Houston.html', args)

def Indiana(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Indiana Pacers'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Indiana Pacers'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Indiana Pacers')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Indiana Pacers'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Indiana.html', args)

def LAC(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Los Angeles Clippers'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Los Angeles Clippers'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Los Angeles Clippers')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Los Angeles Clippers'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/LAC.html', args)


def LAL(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Los Angeles Lakers'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Los Angeles Lakers'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Los Angeles Lakers')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Los Angeles Lakers'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/LAL.html', args)

def Memphis(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Memphis Grizzlies'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Memphis Grizzlies'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Memphis Grizzlies')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Memphis Grizzlies'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Memphis.html', args)

def Miami(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Miami Heat'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Miami Heat'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Miami Heat')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Miami Heat'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Miami.html', args)

def Milwaukee(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Milwaukee Bucks'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Milwaukee Bucks'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Milwaukee Bucks')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Milwaukee Bucks'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Milwaukee.html', args)

def Minnesota(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Minnesota Timber Wolves'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Minnesota Timber Wolves'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Minnesota Timber Wolves')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Minnesota Timber Wolves'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Minnesota.html', args)

def NOP(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'New Orleans Pelicans'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'New Orleans Pelicans'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'New Orleans Pelicans')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'New Orleans Pelicans'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/NOP.html', args)

def NY(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'New York Knicks'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'New York Knicks'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'New York Knicks')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'New York Knicks'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/NY.html', args)

def OKC(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Oklahoma City Thunder'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Oklahoma City Thunder'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Oklahoma City Thunder')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Oklahoma City Thunder'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/OKC.html', args)


def Orlando(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Orlando Magic'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Orlando Magic'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Orlando Magic')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Orlando Magic'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Orlando.html', args)

def PHILA(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Philadelphia 76ers'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Philadelphia 76ers'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Philadelphia 76ers')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Philadelphia 76ers'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/PHILA.html', args)

def SUNS(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Phoenix Suns'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Phoenix Suns'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Phoenix Suns')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Phoenix Suns'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/SUNS.html', args)
def Portland(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Portland Trail Blazers'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Portland Trail Blazers'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Portland Trail Blazers')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Portland Trail Blazers'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/Portland.html', args)


def SAC(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Sacramento Kings'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Sacramento Kings'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Sacramento Kings')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Sacramento Kings'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/SAC.html', args)

def SAS(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'San Antonio Spurs'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'San Antonio Spurs'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'San Antonio Spurs')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'San Antonio Spurs'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/SAS.html', args)

def TOR(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Toronto Raptors'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Toronto Raptors'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Toronto Raptors')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Toronto Raptors'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/TOR.html', args)

def UTAH(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Utah Jazz'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Utah Jazz'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Utah Jazz')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Utah Jazz'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/UTAH.html', args)


def WASH(request):
    query = "SELECT 1 id, m_teamB_Name, m_teamA_result, m_date FROM MATCHUP WHERE m_teamA_Name = 'Washington Wizards'"
    queryForPlayers = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp, p_minutes, p_rebounds FROM PLAYER INNER JOIN TEAM ON p_abr = t_abr WHERE t_name = 'Washington Wizards'"
    queryForLocations = "SELECT 1 id, state FROM LOCATIONS INNER JOIN (SELECT 1 id, loc_id FROM teamLocations WHERE (id,t_id) IN (SELECT 1 id, t_id FROM TEAM WHERE t_name = 'Washington Wizards')) AS table1 ON table1.loc_id = l_id"
    queryForRecord = "SELECT 1 id, t_wins, t_loss FROM TEAM WHERE t_name = 'Washington Wizards'"
    matchups = []
    players = []
    locations = []

    for m in Matchup.objects.raw(query):
        matchups.append(m)

    for p in Player.objects.raw(queryForPlayers):
        players.append(p)

    for l in Locations.objects.raw(queryForLocations):
        locations.append(l)
    team = []
    for t in Team.objects.raw(queryForRecord):
        team.append(t)
    args = {'matchups': matchups, 'playerList': players, 'locations' : locations, 'team': team}


    return render(request, 'Stats/WASH.html', args)

