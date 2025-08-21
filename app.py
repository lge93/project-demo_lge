import streamlit as st
from utils import plot_gaussian_dist, plot_uniform_dist
import pandas as pd
import numpy as np


st.title("Histogram Plotter")

selected_distribution = st.selectbox("Select a distribution", options=["Normal Distribution", "Uniform Dist"], index=0, key="dist")

bins = st.slider("Number of bins", min_value=10, max_value=500, value=100, step=1, key="bins")
N = st.slider("Number samples", min_value=10, max_value=100_000, value=10000, step=1, key="samples")

if selected_distribution == 'Normal Distribution':
    fig = plot_gaussian_dist(mean=0, std=1, bins=bins, N=N)
else:
    fig = plot_uniform_dist(a=0, b=1, bins=bins, N=N)

df = pd.DataFrame(np.random.randn(1000, 3), columns=['A', 'B', 'C'])

st.pyplot(fig)

st.dataframe(df.describe())