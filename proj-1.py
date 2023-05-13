from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

key = pd.read_csv('DataScientistNaukri.csv')

app = Dash()

df = dcc.Dropdown(options=key['title'],
                            value='Sr. Data Scientist')

app.layout = html.Div(children=[
    html.H1(children='data scientist key skills'),
    df
    #dcc.Graph(id='price-graph')
])

@app.callback(
    Output(component_id='title', component_property='tagsAndSkills'),
    Input(component_id=df, component_property='title')
)
def update_graph(selected_geography):
    filtered_avocado = avocado[DataScientistNaukri['title'] == selected_geography]
    # line_fig = px.line(filtered_avocado,
    #                    x='date', y='average_price',
    #                    color='type',
    #                    title=f'Avocado Prices in {selected_geography}')
    # return line_fig

if __name__ == '__main__':
    app.run_server(debug=True)