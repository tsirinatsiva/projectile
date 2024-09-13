import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
import math 

st.set_page_config(
    # ENTITLED
    page_title='ROCKET SIMULATION',
    layout='wide',
    initial_sidebar_state='expanded')

alt.themes.enable('dark')

g=9.81



#CREATING SIDEBAR
with st.sidebar:
    st.title(' :green[BULLET] ⛱️')
    v0=st.number_input(' :blue[INITIAL VELOCITY (m/s)]', step=0.1, value = 1.0)
    alpha =st.number_input(' :blue[LAUNCHING ANGLE (degree)]', min_value= 0.0, max_value = 90.0, step=0.1, value = 1.0)


alpha_rad = alpha *(355/(113*180))
b= v0*math.sin(alpha_rad)
tfin=(2*b)/g

t=0.01
temps=[0]
xt=[]
yt=[]

while t<=tfin:
     
     xt.append(v0*math.cos(alpha_rad)*t)
     yt.append(-0.5*g*(t)**2 + b*t )
     temps.append(t)
     t=t+0.01
     
data = pd.DataFrame(list(zip(xt,yt,temps)),columns=['x','y','temps'])


#DEFINE COLUMN
col=st.columns((2,10),gap='small')

with col[0]:
    st.markdown('### :green[TARGET POSITION]')
    x_target=[]
    y_target=[]


    x_cible = st.number_input(' :blue[X target (m)]', min_value= 0.0,  step=1.0, value = 1.0)
    y_cible = st.number_input(' :blue[Y target (m)]', min_value= 0.0, step=1.0, value=1.0)

x_target.append(float(x_cible))
y_target.append(float(y_cible))




with col[1]:
    st.markdown('### :green[ROCKET CURVE]')
    fig=px.scatter(data,x='x',y='y', animation_frame='temps',
                   range_x=[0,max(data['x'])], range_y=[0,max(data['y'])]
                   )
    fig.update_traces(marker=dict(color='orange'))

    fig.add_scatter( x=x_target,y=y_target, mode='markers', marker=dict(size=15, color='red'))

    st.plotly_chart(fig,theme='streamlit')





