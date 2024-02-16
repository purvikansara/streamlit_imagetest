# hello_streamlit.py
import streamlit as st

st.title('Hello, pk!')

# Explore title, headers, and subheaders
st.title(" Title")
st.header(" Header")
st.subheader(" Subheader")

# Basic text
st.write("This is standard text")
# Markdown-example shows bold and italics
st.markdown("This is markdown showing **bold** and *italics*")

# # Create a simple dataframe
# import pandas as pd
# df = pd.DataFrame({'A':[1,2,3],"B":[5,6,7]})
# # Display dataframe
# st.dataframe(df)

# # Get user name
# name = st.text_input("First Name")
# # Print message with user name
# st.write(f"Hello, World! My name is {name}!")

# # Get user name
# name = st.text_input("First Name", value = "Purvi")
# # Print message with user name
# st.write(f"Hello, World! My name is {name}!")

# # If the button is pressed, print the message
# if st.button("Say hello."):
#     st.write(f"Hello, World! My name is {name}.")

# # Get date information
# date = st.date_input(label="Date of Birth")

# # Updated date input with minimum and default values
# import datetime as dt
# date = st.date_input(label="Date of Birth", min_value=dt.date(1900,1,1), value=dt.date(2013,1,1))

# # Create the select box with all options
# season = st.selectbox("Favorite Season", ['Winter','Spring','Summer','Fall'])

# # Add slider, text to be displayed, min value, max value, and default value
# excitement = st.slider("How excited are you to learn Streamlit?? (1=Not at all; 10=Very!)",min_value=1, max_value=10,value=5)

import streamlit as st
import datetime as dt # moved all imports to the top
from PIL import Image

# st.image('app-banner.png')
image = Image.open('app-banner.png')
st.image(image, caption='prediction')


# Download the  image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
else:
    fix_image("./zebra.jpg")

st.title('Hello, Streamlit!')
# Get the name
name = st.text_input("First Name",value="Streamlit")
# Add Date Selection 
date = st.date_input(label="Date of Birth", min_value=dt.date(1900,1,1),value=dt.date(2013,1,1))
# Create the select box with all options
season = st.selectbox("Favorite Season", ['Winter','Spring','Summer', 'Fall'])
# Adding user excitment
excitement = st.slider("How excited are you to learn Streamlit?? (1=Not at all; 10=Very!)", min_value=1, max_value=10,value=5)
# If the button is pressed, print message
if st.button("Introduce me!"):
    st.markdown(f"""
    > #### ***Hello, World!*** My name is **{name}**.
    - I was born on **{date}**.
    - My favorite season is **{season}**.
    - My excitement for learning streamlit is... **{excitement}/10.**""")