import streamlit as st
import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.models import DataTable, TableColumn, HTMLTemplateFormatter

df = pd.read_csv('category.csv')

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
        st.write("$ "+str(df.iloc[i,4]))
        st.image(df.iloc[i,2]+".jpg", use_column_width=True)
        st.write(df.iloc[i,3])