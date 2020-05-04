# -*- coding: utf-8 -*-
#Import librairie

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import numpy as np
import pandas as pd
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt
import chart_studio.plotly as py
import plotly.graph_objs as go
import math

#Import des donnés

path_setRaw = "Data/set_bans.csv"
path_setRework = "Data/set_bansRework.csv"
path_monstre = "Data/set_monsters.csv"
path_date = "Data/set_addressDate.csv"
path_info = "Data/set_matchInfo.csv"
path_kills = "Data/set_killsClassChamp.csv"
path_fullKills = "Data/set_kills.csv"
path_structure = "Data/set_structures.csv"


df_bans_raw = pd.read_csv(path_setRaw)
df_bans_rework = pd.read_csv(path_setRework)
df_bans_rework.Date = pd.to_datetime(df_bans_rework.Date)
df_monstre = pd.read_csv(path_monstre)
df_date = pd.read_csv(path_date)
df_info = pd.read_csv(path_info)
df_kills = pd.read_csv(path_kills)
df_struct = pd.read_csv(path_structure)
df_fullkill = pd.read_csv(path_fullKills)


df_fullkill = df_fullkill.drop(columns="Unnamed: 0")

#Add date to structure
#df_monstre = df_monstre.merge(right=df_info[['rResult','Address']], right_on="Address",left_on="Address",how="left")
df_monstre = df_monstre.merge(right=df_date, right_on="Address", left_on="Address", how="left")

# Set the datetime columns
df_monstre.Date = pd.to_datetime(df_monstre.Date)
df_kills.Date = pd.to_datetime(df_kills.Date)


#-----------------------Preparation des données---------------------------
#Graph 1
test = pd.DataFrame(df_bans_rework.Champions.value_counts())
tt = test.sort_values(by="Champions", ascending=False).head(10)

#Graph 2 kde
df_kills_temp = df_kills.drop(df_kills[df_kills.Time.isna()].index)
time_kills = df_kills_temp.Time
time_kills = time_kills.round(0)

#graph 2.5
df_struct_temp = df_struct.drop(df_struct[df_struct.Time.isna()].index)

df_tour_mid = df_struct_temp[df_struct_temp.Lane == "MID_LANE"]
tt_tepms = df_tour_mid.copy()
tt_tepms.Time = tt_tepms.Time.round(0)
tt_tepms = pd.pivot_table(tt_tepms, index="Time",aggfunc="count")
tt_tepms = tt_tepms.reset_index()


df_tour_top = df_struct_temp[df_struct_temp.Lane == "TOP_LANE"]
df_tour_bot = df_struct_temp[df_struct_temp.Lane == "BOT_LANE"]



ttKills = df_kills_temp[(df_kills_temp.Time > -1)&(df_kills_temp.Time <= 50)].Time
ttx = np.arange(0,51,1)

#Graph monstre
df1 = df_monstre[['Type',"Time"]]
df_dragon = df1.query('Type=="DRAGON"')
df_nashor = df1.query('Type=="BARON_NASHOR"')
df_herald = df1.query('Type=="RIFT_HERALD"')

df_dragonE_feu = df1.query('Type=="FIRE_DRAGON"')
df_dragonE_eau = df1.query('Type=="WATER_DRAGON"')
df_dragonE_terre = df1.query('Type=="EARTH_DRAGON"')
df_dragonE_air = df1.query('Type=="AIR_DRAGON"')
df_dragonE_vieu = df1.query('Type=="ELDER_DRAGON"')

#-----------------------Preparation des données---------------------------

#Graph killsScatter

df_fullkill["Date"] = pd.to_datetime(df_fullkill["Date"])

df_fullkill = df_fullkill.drop(index = df_fullkill[df_fullkill.x_pos == 'TooEarly'].index)
df_fullkill = df_fullkill.drop(index = df_fullkill[df_fullkill.x_pos.isna()].index)

df_fullkill.x_pos = df_fullkill['x_pos'].astype('int64')
df_fullkill.y_pos = df_fullkill['y_pos'].astype('int64')

df_position = df_fullkill[["Team","Time","x_pos","y_pos"]]
red_team = df_position.query("Team == 'rKills'")
blue_team = df_position.query("Team == 'bKills'")

#/------------------------------------------------------------/#
#graph 2.5
df_struct_temp = df_struct.drop(df_struct[df_struct.Time.isna()].index)

df_tour_mid = df_struct_temp[df_struct_temp.Lane == "MID_LANE"]
tt_tepms = df_tour_mid.copy()
tt_tepms.Time = tt_tepms.Time.round(0)
tt_tepms = pd.pivot_table(tt_tepms, index="Time",aggfunc="count")
tt_tepms = tt_tepms.reset_index()

df_tour_top = df_struct_temp[df_struct_temp.Lane == "TOP_LANE"]
tt_tepms2 = df_tour_top.copy()
tt_tepms2.Time = tt_tepms2.Time.round(0)
tt_tepms2 = pd.pivot_table(tt_tepms2, index="Time",aggfunc="count")
tt_tepms2 = tt_tepms2.reset_index()

df_tour_bot = df_struct_temp[df_struct_temp.Lane == "BOT_LANE"]
tt_tepms3 = df_tour_bot.copy()
tt_tepms3.Time = tt_tepms3.Time.round(0)
tt_tepms3 = pd.pivot_table(tt_tepms3, index="Time",aggfunc="count")
tt_tepms3 = tt_tepms3.reset_index()

df_kills_temp = df_kills.drop(df_kills[df_kills.Time.isna()].index)
time_kills = df_kills_temp.Time
time_kills = time_kills.round(0)
ttKills = df_kills_temp[(df_kills_temp.Time > -1)&(df_kills_temp.Time <= 50)].Time
ttx = np.arange(0,51,1)


df_kills_herald = df_monstre[df_monstre.Type =="RIFT_HERALD"]
tt_tepms5 = df_kills_herald.copy()
tt_tepms5.Time = tt_tepms5.Time.round(0)
tt_tepms5 = pd.pivot_table(tt_tepms5, index="Time",aggfunc="count")
tt_tepms5 = tt_tepms5.reset_index()

df_kills_drakeFeu = df_monstre[df_monstre.Type =="FIRE_DRAGON"]
tt_tepms6 = df_kills_drakeFeu.copy()
tt_tepms6.Time = tt_tepms6.Time.round(0)
tt_tepms6 = pd.pivot_table(tt_tepms6, index="Time",aggfunc="count")
tt_tepms6 = tt_tepms6.reset_index()

df_kills_drakeTerre = df_monstre[df_monstre.Type =="EARTH_DRAGON"]
tt_tepms7 = df_kills_drakeTerre.copy()
tt_tepms7.Time = tt_tepms7.Time.round(0)
tt_tepms7 = pd.pivot_table(tt_tepms7, index="Time",aggfunc="count")
tt_tepms7 = tt_tepms7.reset_index()

df_kills_drakeEau = df_monstre[df_monstre.Type =="WATER_DRAGON"]
tt_tepms8 = df_kills_drakeEau.copy()
tt_tepms8.Time = tt_tepms8.Time.round(0)
tt_tepms8 = pd.pivot_table(tt_tepms8, index="Time",aggfunc="count")
tt_tepms8 = tt_tepms8.reset_index()

df_kills_drakeAire = df_monstre[df_monstre.Type =="AIR_DRAGON"]
tt_tepms9 = df_kills_drakeAire.copy()
tt_tepms9.Time = tt_tepms9.Time.round(0)
tt_tepms9 = pd.pivot_table(tt_tepms9, index="Time",aggfunc="count")
tt_tepms9 = tt_tepms9.reset_index()


#----------------------Dashboard---------------------------------------------------

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#external_stylesheets = ['../css/style.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#Graph 1
app.layout = html.Div(children=[
    html.H1(children='Rapport sur les matchs pro League of legends'),
    html.H2(children='Partie 1: Visualisation dynamique des données de base'),

    html.Div(children='''
        Ici nous avons projeter quelque set de données pour les observers de facon un peut plus dynamique, principalement l'évolution des kills dans le temps de jeu
    '''),

    #GraphDensityKills
    dcc.Graph(
        id='projectNb-kills',
        figure={
            'data': [
                {'x': ttx, 'y': ttKills, 'name': 'Nombre de kills'},
            ],
            'layout': dict(
                title="Evolution du nombre de victimes dans le temps (en jeu)",
                xaxis={'title': 'Temps dans la partie'},
                yaxis={'title': 'Nombre de victime'},
            )
        }
    ),

    #GraphTourDestruMid
    dcc.Graph(
        id='projecttourMid',
        figure={
            'data': [
                {'x': tt_tepms.Time, 'y': tt_tepms.Address, 'name': 'tourMid'},
            ],
            'layout': dict(
                title="Evolution du nombre de structures detruite dans le temps (en jeu)",
                xaxis={'title': 'Temps dans la partie'},
                yaxis={'title': 'Nombre de Structure'},
            )
        }
    ),

    #GraphHistNashor
    dcc.Graph(
        id='nashor-hist',
        figure={
            'data': [
                {'x': df_nashor.Time, 'type': 'histogram', 'name': 'Baron Nashor'},
                {'x': df_herald.Time, 'type': 'histogram', 'name': 'Hérault de la faille'}
            ],
            'layout': dict(
                title="Histogramme du nombre de défaite des monstres neutre (Baron Nashor & Héraut de la faille)",
                xaxis={'title': 'Temps dans la partie'},
                yaxis={'title': 'Nombre de créatures défaite'},
                legend={'x':0,'y':1}
            )
        }
    ),

    #GraphHsitDragon
    dcc.Graph(
        id='dragon-hist',
        figure={
            'data': [
                {'x': df_dragonE_feu.Time, 'type': 'histogram', 'name': 'Dragon de feu', 'color':'#ffc0c0'},
                {'x': df_dragonE_eau.Time, 'type': 'histogram', 'name': "Dragon d'eau", 'color':'#9BB7D4'},
                {'x': df_dragonE_terre.Time, 'type': 'histogram', 'name': 'Dragon de terre', 'color':'#BCDEBB'},
                {'x': df_dragonE_air.Time, 'type': 'histogram', 'name': "Dragon d'air", 'color':'#53B0AE'},
                {'x': df_dragonE_vieu.Time, 'type': 'histogram', 'name': 'Ancien dragon', 'color':'#C74375'}

            ],
            'layout': dict(
                title="Histogramme du nombre de défaite des dragons",
                xaxis={'title': 'Temps dans la partie'},
                yaxis={'title': 'Nombre de dragon défaite'},
                legend={'x': 0.5, 'y': 1},
                height=700

            )
        }
    ),

    #GraphBanSlider
    dcc.Graph(id='ban-slider'),
    dcc.Slider(
        id='year-slider',
        min=df_bans_rework.Date.dt.year.min(),
        max=df_bans_rework.Date.dt.year.max(),
        value=df_bans_rework.Date.dt.year.min(),
        marks={str(year): str(year) for year in df_bans_rework.Date.dt.year.unique()},
        step=None
    ),

    dcc.Graph(id='graph-kills-slider'),
    dcc.Slider(
        id='slider-kill',
        min=0,
        max=90,
        value=5,
        marks={str(Time): str(Time) for Time in np.arange(0,90,5)},
        step=None
    ),

    html.H2(children='Partie 2 :Que ce passe-t-il à 10min?'),

    html.Div(children='''
        Graphique utile pour comprendre ce qui ce passe a 10 minutes de jeu
    '''),

    #GraphTourDestruMid
    dcc.Graph(
        id='projecttourMid2',
        figure={
            'data': [
                {'x': tt_tepms.Time, 'y': tt_tepms.Address, 'name': 'tourMid'},
            ],
            'layout': dict(
                title="Evolution du nombre de tours (Mid) detruite dans le temps (en jeu)",
                xaxis={'title': 'Temps dans la partie'},
                yaxis={'title': 'Nombre de tours'},
            )
        }
    ),

    #GraphTourDestruTop
    dcc.Graph(
        id='projecttourTop',
        figure={
            'data': [
                {'x': tt_tepms2.Time, 'y': tt_tepms2.Address, 'name': 'tourTop'},
            ],
            'layout': dict(
                title="Evolution du nombre de tours (Top) détuite dans le temps (en jeu)",
                xaxis={'title': 'Temps dans la partie'},
                yaxis={'title': 'Nombre de tours'},
            )
        }
    ),

    #GraphTourDestruBot
    dcc.Graph(
        id='projecttourBot',
        figure={
            'data': [
                {'x': tt_tepms3.Time, 'y': tt_tepms3.Address, 'name': 'tourBot'},
            ],
            'layout': dict(
                title="Evolution du nombre de tours (Bot) détruite dans le temps (en jeu)",
                xaxis={'title': 'Temps dans la partie'},
                yaxis={'title': 'Nombre de tours'},
            )
        }
    ),

    #GraphKillsHeral
    dcc.Graph(
        id='projectNb-Herald',
        figure={
            'data': [
                {'x': tt_tepms5.Time, 'y': tt_tepms5.Address, 'name': 'Nombre de herault tuer'},
            ],
            'layout': dict(
                title="Evolution du nombre d'héraut tués dans le temps (en jeu)",
                xaxis={'title': 'Temps dans la partie'},
                yaxis={'title': 'Nombre de victime'},
            )
        }
    ),

    #GraphKillsDragon
    dcc.Graph(
        id='projectNb-drake',
        figure={
            'data': [
                {'x': tt_tepms6.Time, 'y': tt_tepms6.Address, 'name': 'Dragon de feu'},
                {'x': tt_tepms7.Time, 'y': tt_tepms7.Address, 'name': 'Dragon de Terre'},
                {'x': tt_tepms8.Time, 'y': tt_tepms8.Address, 'name': "Dragon d'eau"},
                {'x': tt_tepms9.Time, 'y': tt_tepms9.Address, 'name': "Dragon d'aire"},

            ],
            'layout': dict(
                title="Evolution du nombre de dragons tués dans le temps (en jeu)",
                xaxis={'title': 'Temps dans la partie'},
                yaxis={'title': 'Nombre de victime'},
            )
        }
    ),

])

#App d'update
@app.callback(
    Output(component_id='ban-slider', component_property='figure'),
    [Input(component_id='year-slider', component_property='value')]
)
def update_figure(selected_year):
    test3 = pd.DataFrame(df_bans_rework[df_bans_rework.Date.dt.year == selected_year].Champions.value_counts())

    traces = []

    tt3 = test3.sort_values(by="Champions", ascending=False).head(10)

    traces.append(dict(
        x=tt3.index,
        y=tt3.Champions,
        type='bar',
        name='Ban'
    ))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'title': 'Champions'},
            yaxis={'title': 'Nombre de fois exclus'},
            transition = {'duration': 500}
        )
    }

@app.callback(
    Output(component_id='graph-kills-slider', component_property='figure'),
    [Input(component_id='slider-kill', component_property='value')]
)
def update_figure(selected_time):

    tempAEnlever = 5 #Si changer, penser a changer le slider
    tt4 = df_position[(df_position.Time >= selected_time - tempAEnlever)&(df_position.Time <=selected_time)]

    traces = []


    traces.append(dict(
            x=tt4.x_pos,
            y=tt4.y_pos,

            mode='markers',
            opacity=0.8 ,
            color="#21282c",
            marker={
                'size': 1
                }
    ))

    return {
        'data': traces,
        'layout': dict(
            title="visualisation des victimes des combats",
            xaxis={'title': 'Position x'},
            yaxis={'title': 'Position y'},
            hovermode='closest',
            height= 800,  # px
            width= 800,  # px
            transition = {'duration': 500}
        )
    }
#*--------------------------------Todo liste-------------------------------------------------------*#

# >>> trouver comment ajouter une fiche css sinon passer en html

#---------------------------------------------------------------------------


if __name__ == '__main__':
    app.run_server(debug=True)
