import psycopg2
import plotly
import plotly.graph_objs as go
import pandas as pd

db_connection=psycopg2.connect(database="postgis_24_sample", user="postgres", password="postgres", host="127.0.0.1", port="5432")
query="select imoname, port, datetimes from pythonvalues"
df=pd.read_sql(query,con=db_connection)
print(df)
df.info()

for index, row in df.iterrows():
	t=row.imoname
	data = [go.Scatter(
		x=row.datetimes,
		y=[int(item) for item in row.port],
#		x=row.datetimes.values.tolist()[0],
#		y=row.port.values.tolist()[0],
		hovertemplate="%{x|%Y/%m/%d %H:%M:%S.%L} port: %{y}<extra></extra>",
		marker=dict(color='red', size=10),
		line=dict(color='black', width=3),
	)]
	layout = go.Layout(
		)
	fig = go.Figure(data=data, layout=layout)
	fig.update_traces(mode='lines+markers')
	fig.update_layout(title=t)
#	fig.show()
	filenombre="%s.html" %t
#	plotly.offline.plot(fig,filename=filenombre,config={'displayModeBar': False}, auto_open=False)
	plotly.offline.plot(fig,filename=filenombre, auto_open=False)