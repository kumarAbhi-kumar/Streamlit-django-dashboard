import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import altair as alt 
import pandas as pd
import requests

# Endpoints
swapi_endpoint = 'https://swapi.dev/api/people/1/'
api_url = 'http://127.0.0.1:8000/api/customers/'

# Functions

def fetch_data(endpoint):
    response = requests.get(endpoint)
    data = response.json()
    return data

def send_data(name, gender, age, favorite_number):
    gender_value = "0" if gender == "Female" else "1"
    data = {
        "name": name,
        "gender": gender_value,
        "age": age,
        "favorite_number": favorite_number
    }
    response = requests.post(api_url, json=data)
    return response

st.title("Analytics Dashboard")
st.write("v.0.0.1")

# Layout Customization
col1, col2 = st.columns(2)

with col1:
    st.header('Column 1')
    st.write('Some Content')

    with st.expander('Click to Choose something'):
        st.write('Option 1')
        st.write('Option 2')


with col2:
    # Test Chart
    categories = ['A', 'B', 'C', 'D']
    values = np.random.randint(10, 100, size=(4,))

    fig, ax = plt.subplots()
    ax.bar(categories, values, color = 'cyan')
    ax.set_xlabel('categories')
    ax.set_ylabel('values')
    ax.set_title('Bar Chart')

    st.pyplot(fig)

# Session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# increment btn
if st.button('increment'):
    st.session_state.counter +=1

st.write(f"Counter Value: {st.session_state.counter}")

# data from SWAPI API
swapi_data = fetch_data(swapi_endpoint) # hold the json data returned by the endpoint

st.write('Data From the Swapi API')
st.json(swapi_data)

# Fetch Data from our Custom API
data = fetch_data(api_url)

if data:
    # Creating a tabular view for the file
    df = pd.DataFrame(data)
    st.dataframe(df)

    # Adding the scatterplot.
    scatter_chart = alt.Chart(df).mark_circle().encode(
        x = 'age',
        y = 'favorite_number'
    )

    st.altair_chart(scatter_chart, use_container_width=True)

# Form to collect Customer Data
name = st.text_input("Your Name")
gender = st.radio("Select your Gender", {"Male", "Female"})
age = st.slider("Select your Age", 1, 100, 18)
favorite_number = st.number_input("Enter your Favorite Number", step = 1)

if st.button("Submit"):
    response = send_data(name, gender, age, favorite_number)
    if response.status_code == 201:
        st.success("New Customer Data created")
        st.rerun()
    else:
        st.error("Something went wrong..!")