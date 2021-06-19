import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from IPython.display import HTML
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models import DataTable, TableColumn, HTMLTemplateFormatter, NumberFormatter
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import get_as_dataframe, set_with_dataframe
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
c = ServiceAccountCredentials.from_json_keyfile_name('my-project-test-316903-48eb13e795b1.json', scope)
gs = gspread.authorize(c)
SPREADSHEET_KEY = '11xBHbPnTTexkH0OWKIEAlmUOYvHujyz1PVSYfJkmv5o'
workbook = gs.open_by_key(SPREADSHEET_KEY)
worksheet2 = workbook.worksheet('category')

#list_data = worksheet2.get_('A1:D10')
data = worksheet2.get_all_values()
df = pd.DataFrame(data[1:],columns=data[0])
genre=st.sidebar.radio(
    "Whats your favorite pedal?",
    ('Low gain', 'Over Drive', 'Distortion','High Gain Metal','Delay','Reverb','Phaser','Flanger','Chorus','Tuner')
    )

df=df[df["Category"]==genre]

cds = ColumnDataSource(df)
columns = [
TableColumn(field="Category", title="Category"),
TableColumn(field="Maker", title="Maker"),
TableColumn(field="pedal", title="pedal"),
TableColumn(field="URL", title="URL", formatter=HTMLTemplateFormatter(template='<a href="<%= URL %>"target="_blank"><%= value %></a>')),
]
p = DataTable(source=cds, columns=columns, css_classes=["my_table"])
#st.sidebar.bokeh_chart(p)
j=len(df)

col= st.beta_columns(3)
for i in list(range(0,j)):
    with col[i%3]:
        st.write(df.iloc[i,1]+" / "+df.iloc[i,2])
        st.write('$'+df.iloc[i,4]+' NTD')
        st.image(df.iloc[i,2]+".jpg", use_column_width=True)
        st.write("[https://www.youtube.com/watch?v=x8VYWazR5mE](https://www.youtube.com/watch?v=x8VYWazR5mE)")



#st.dataframe(df2.style.highlight_max(axis=0),width=5000,height=500)
#if genre == 'Low gain':
 #    st.write('You selected Low gain.')
  #   st.dataframe(df.style.highlight_max(axis=0),width=5000,height=500)