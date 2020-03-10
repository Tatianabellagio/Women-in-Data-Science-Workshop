# las aplicaciones de dash estan compuestas de dos partes:
# - layout : ¿Cómo se ve la aplicación?
# - 
# además dash posee librerías para disferentes componentes visuales
# en python, que son los dcc y los html
import dash

import dash_html_components as html
# la librería html posee un componente por cada tipo de objeto en html
# por ej html.H1() es equivalente a <h1> </h1>

import dash_core_components as dcc
#por otros lado los dcc son componentes de alto nivel, interactivos y generados con 
# JS, HTML, CSS a través de React.js

# esta librería tendrá el componentes:
#     - dropdowns
#     - graphs
#     - markdowns blocks y más

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# el layoout consiste en un arbol de componentes como los html.Div y los dcc.Graph


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

# debug = True generará que cada cambio guardado en tu editor de código 
# automáticamente será plasmado en el servidor corriendo, 


# y algo importantísimo!!!
# help!!
help(dcc.Dropdown)
