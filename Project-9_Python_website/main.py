import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Website Title
st.set_page_config(page_title="My Streamlit Website", layout="wide")
st.title("Welcome to My First Streamlit Website")

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page:", ["Home", "User Info", "Sample Data", "Visualization", "File Upload"])

# Home Page
if page == "Home":
    st.header("Welcome to the Streamlit Web App!")
    st.write("""
    This is a simple web app built with Python and Streamlit in just 15 minutes. 
    You can interact with different sections like User Info, Data Tables, and Visualizations. 
    The app also lets you upload files and perform some basic operations.
    """)
    st.image("https://www.streamlit.io/images/brand/streamlit-logo-dark.png", width=500)

# User Info Page
elif page == "User Info":
    st.header("Tell Us About Yourself")

    name = st.text_input("What is your name?")
    age = st.number_input("How old are you?", min_value=1, max_value=100, step=1)

    if st.button("Submit"):
        st.write(f"Hello {name}, you are {age} years old! 👋")

# Sample Data Page
elif page == "Sample Data":
    st.header("Sample Data Table")

    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    }

    df = pd.DataFrame(data)
    st.write("Here is a sample data table:")
    st.dataframe(df)

# Visualization Page
elif page == "Visualization":
    st.header("Data Visualization with Matplotlib")

    # Generating random data for plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, label="Sine Wave", color='orange')
    ax.set_title("Sine Wave Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.legend()

    st.pyplot(fig)

# File Upload Page
elif page == "File Upload":
    st.header("Upload Your File")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df_uploaded = pd.read_csv(uploaded_file)
        st.write("Here is the uploaded file:")
        st.dataframe(df_uploaded)

# Footer Section
st.markdown("""
    ---
    **Thank you for visiting my website!**  
    Built with 💙 using [Streamlit](https://streamlit.io).
            © 2025 Shanyal Siddiqui. All rights reserved
""")