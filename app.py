import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np

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


