import streamlit as st 
from bokeh.plotting import figure, show
 
graph = figure(title = "Bokeh Line Graph")
 
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
 
graph.line(x, y)
 
st.bokeh_chart(graph)