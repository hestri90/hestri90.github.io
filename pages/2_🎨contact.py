import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Contact", 
    page_icon=":rocket:", 
    layout="wide"
)

# ---- LOAD ASSETS ---
img_hestri =  Image.open("images/hestri.jpg")
img_enung = Image.open("images/enung.jpg")
#img_sarah = Image.open("images/sarah.jpg")

# ---- HEADER ----
with st.container():
    st.snow()
    st.title(":book: ABOUT US")
    st.write("---")
    st.header("Halo, Kami dari kelompok Lavender :wave:")
    st.write("---")
    image_column, text_column = st.columns((1,2))

# ---- Hestri ----
    with image_column:
        st.image(img_hestri, caption='Hestri', use_column_width='auto' )
    with text_column:
        st.subheader("Hestriyanah")
        st.write("---")
        st.markdown(
            """
            Saya adalah lulus AMIK BSI Jurusan Manajemen Informatika.
            Saya suka mempelajari hal baru, termasuk teknologi baru.
            """
        )
    st.write("---")
    st.write("\n")

# ---- Enung ----
    image_column, text_column = st.columns((1,2))   
    with image_column:
        st.image(img_enung, caption='Enung Nurjanah', use_column_width='auto' )
    with text_column:
        st.subheader("Enung Nurjanah")
        st.write("---")
        st.markdown(
            """
            Saya adalah lulusan Teknik Informatika UIN Sunan Gunung Djati Bandung.


            """
        )
    st.write("---")
    st.write("\n")

# ---- Sarah ----
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_hestri, caption='Sarah Suwarno', use_column_width='auto' )
    with text_column:
        st.subheader("Sarah Suwarno")
        st.write("---")
        st.markdown(
            """
            
            """
        )
    st.write("---")

