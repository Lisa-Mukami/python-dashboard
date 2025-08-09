import dash
import dash import dcc , html
import dash , dependencies import Input , Output
import pandas as pd
import plotyly.express as px

#Initialize the dash app
app=das.Dash(name)

#sample data
data=pd.DataFrame({
    "City":["NY","LA","Chicago","Houston"],
    "Fruits":["Apples","Bananas","Oranges","Apples"],
    "Sales":[120,80,150,100]
    })

#App layout
app.layout=html.Div([
    html.H1("Fruit sales Dashdoards"),
    dcc.Dropdown(
        id='fruit.filter',
        options[{'label':fruit,'value':fruit}for fruit in data['Fruit'].unique()],
        value='Apple',
        Clearable=False
        ),
    dcc.Graph(id='sales.grph')
    ])

#callback to update the graph
@app.callback(
    Output('sales-graph','figure'),
    Input('fruit-filter','value')
    )

def update_graph(selected_fruit):
    filtered=data[data['Fruit']==selected_fruit]
    fig=px.bar(filtered, x="City" , y="Sales" , colour="Fruit" , title=f"Sales for {selected_fruit}")
    return fig 
if_name_=='_main_'
app.run(debug=True)
