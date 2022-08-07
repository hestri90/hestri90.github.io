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
img_sarah = Image.open("images/Plush.png")
img_linkedin = Image.open("images/Linkedin.png")
img_github = Image.open("images/Github.png")

# ---- HEADER ----
with st.container():
    st.snow()
    st.title(":book: ABOUT US")
    st.write("---")
    st.header("Halo, Kami dari kelompok Lavender :wave:")
    st.write("---")
    image_column, text_column = st.columns((1,3))

# ---- Hestri ----
    with image_column:
        st.image(img_hestri, caption='Hestri', width=150 )
    with text_column:
        st.subheader("Hestriyanah")
        st.write("---")
        st.markdown(
            """
            Saya adalah lulus AMIK BSI Jurusan Manajemen Informatika.
            Saya suka mempelajari hal baru, termasuk teknologi baru. \n \n
            """
        )
        st.image(img_linkedin, width = 30) 
        st.write(" [hestri yanah](https://www.linkedin.com/in/hestri-yanah-14285a246)")
        st.image(img_github, width = 30) 
        st.write(" [hestri90](https://github.com/hestri90)")
    st.write("---")
    st.write("\n")

# ---- Enung ----
    image_column, text_column = st.columns((1,3))   
    with image_column:
        st.image(img_enung, caption='Enung Nurjanah', width=150 )
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
    image_column, text_column = st.columns((1,3))
    with image_column:
        st.image(img_sarah, caption='Sarah Suwarno', width=150 )
    with text_column:
        st.subheader("Sarah Suwarno")
        st.write("---")
        st.markdown(
            """
            Saya adalah mahasiswa S1 yang tertarik dengan bidang teknologi
            informasi. Saya masih belajar dan terbuka dengan semua informasi baru.
            """
        )
    st.write("---")

