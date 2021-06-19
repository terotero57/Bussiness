import streamlit as st
import pandas as pd

df = pd.read_csv('category.csv')

genre=st.sidebar.radio(
    "Whats your favorite pedal?",
    ('Low gain', 'Over Drive', 'Distortion','High Gain Metal','Delay','Reverb','Phaser','Flanger','Chorus','Tuner')
    )

df=df[df["Category"]==genre]

#st.sidebar.bokeh_chart(p)
j=len(df)

col= st.beta_columns(3)
for i in list(range(0,j)):
    with col[i%3]:
        st.write(df.iloc[i,1]+" / "+df.iloc[i,2])
        st.write(df.iloc[i,4])
        st.image(df.iloc[i,2]+".jpg", use_column_width=True)
