import streamlit as st
import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.models import DataTable, TableColumn, HTMLTemplateFormatter

df = pd.read_csv('category.csv')

Price = st.sidebar.slider('您的預算?', 0, 9999, 9999)
st.sidebar.write("預算是$", str(Price), '以下')
df = df[df.Price <=Price]

genre=st.sidebar.radio(
    "Whats your favorite category?",
    ('All','OverDrive', 'Distortion', 'Delay','Reverb','Chorus','Flanger','Phaser','EQ','Noise Reduce','音量踏板/表情踏板','娃娃踏板','特殊','Looper','Bass','Amplug','綜合','Tuner','其他')
    )
if genre is not 'All' :
    df=df[df["Category"]==genre]

Maker=st.sidebar.radio(
    "Whats your favorite maker?",
    ('All','Boss', 'TC Electronic', 'MXR','Korg','Effect Bakery','Arion','Ibanez','Zoom','Digitech','Mooer','EBS','Vox','Hotone','Electro-Harmonix')
    )
if Maker is not 'All' :
    df=df[df["Maker"]==Maker]


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