import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from dash.dependencies import Input, Output
from datetime import datetime
from datetime import date
import dash_table
import plotly.graph_objects as go

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css 5", 
                        'https://codepen.io/amyoshino/pen/jzXypZ.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#imports
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

#importamos el dataset a trabajar
df = pd.read_csv("dataset_base_dash.csv").drop("Unnamed: 0", axis=1)

path = df[["disciplina_titulo_grado_id","disciplina_maximo_grado_academico_id", "disciplina_experticia_id"]]
path = path.dropna()
to_keep = path["disciplina_experticia_id"].value_counts().index[:20]
path = path[path[["disciplina_titulo_grado_id","disciplina_maximo_grado_academico_id", "disciplina_experticia_id"]].isin(to_keep)].dropna()

cat_edad = df[["categoria_conicet_id","edad"]]

map_cat = {'Becario doctoral':1,
       'Becario postdoctoral':2,
       'Investigador asistente':3, 
       'Investigador adjunto':4,
       'Investigador independiente':5, 
       'Investigador principal':6,
       'Investigador superior':7 
        }
cat_edad["categoria_conicet_id"] = cat_edad["categoria_conicet_id"].map(map_cat)
cat_edad = cat_edad.dropna()
df["año_2018"] = df["producciones_ult_anio"]
cat_edad_sexo = pd.concat([cat_edad, df[df["año_2018"] != -1]["año_2018"]],axis=1).dropna()

fig_scatter_3d = px.scatter_3d(cat_edad_sexo, x="año_2018", y='edad', z='categoria_conicet_id',
              color='categoria_conicet_id')

fig_scatter_3d.update_traces(marker=dict(size=2),
                  selector=dict(mode='markers'))


app.layout = html.Div([
    html.Div([
        html.H1(
            children='Análisis Personas en Ciencia y técnica',
            className='twelve columns',
            style={
                'textAlign': 'center',
                
        })

    
    ]),


    html.Div([dcc.Graph(id = "paralel", figure = px.parallel_categories(path))]),




    html.Div([
        html.Div([
        dcc.Graph(
                id='fig_scatter_3d',
                figure = fig_scatter_3d ), 
    ],
    className="six columns",
    style = {"margin-top": "5px", "margin-bottom": "10px"}
    ),


 #   html.Div([
 #       dcc.Dropdown(
  #              id='meses',
   #             options=[{'label': i, 'value': i} for i in month],
    #            style={'position':'relative', 'zIndex':'999'},
     #           value= ["mes1", "mes2"],
      #          multi= True)
   # ],
   # className="six columns",
   # style={"margin-top": "5px", "margin-bottom": "10px"},

 #   ),

    ], className="row"
    ),

    
 
 ])




if __name__ == '__main__':
    app.run_server(debug=False)