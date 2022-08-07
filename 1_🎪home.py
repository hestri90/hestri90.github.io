import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

# ---- DATA LINE CHART ----
data_serangan = pd.DataFrame({
    "jumlah_serangan":  [59316206, 44901308,50402748,115898735, 186202637, 164446175, 120593162, 146950765, 123645909, 186985509, 196563700, 242066168],
    "Date": ["2021-1-31", "2021-2-28", "2021-3-31", "2021-4-30", "2021-5-31", "2021-6-30", "2021-7-31", "2021-8-31", "2021-9-30", "2021-10-30", "2021-11-30", "2021-12-31"]
})
 
line_chart = alt.Chart(data_serangan).mark_line().encode(
        y=  alt.Y('jumlah_serangan', title='Jumlah Serangan'),
        x=  alt.X( 'month(Date)', title='Bulan')
    ).properties(
        height=400, width=700,
        title="Jumlah Anomali Nasional pada 2021"
    ).configure_title(
        fontSize=16
    )

# ---- DATA BAR CHART ----
kasus_ransomware = pd.DataFrame({
        'jumlah_kasus': [1300000, 886874, 192652, 137366, 136636,25093, 20219, 7353, 6118, 257],
        'negara': ['Indonesia', 'Vietnam', 'Thailand', 'Filipina', 'Malaysia', 'Laos', 'Myanmar', 'Kamboja', 'Singapura', 'Brunei Darussalam']
     })
 
bar_chart = alt.Chart(kasus_ransomware).mark_bar().encode(
        y= alt.Y('jumlah_kasus', title='Jumlah Kasus'),
        x= alt.X('negara', title='Negara Asia Tenggara')
    ).properties(
        height=400, width=700,
        title="Kasus Serangan Ransomware di Asia Tenggara (Jan-Sep 2020)"
    ).configure_title(
        fontSize=16
    )
 
    



# find emojis here https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="My Web", 
    page_icon=":maple_leaf:", 
    layout="wide"
) 

# ---- HEADER ----
with st.container():
    st.balloons()
    st.header("Halo, Kami dari kelompok Lavender :wave:")
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.altair_chart(bar_chart, use_container_width=True)
    with right_column:
        st.subheader(
            """
            Indonesia Menempati Urutan pertama negara dengan serangan ransomware terbanyak di Asia Tenggara pada tahun 2020.
            Data tersebut diambil dari _Interpol Cyber Assesment Report 2021_. 
            """
        )
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.video('https://www.youtube.com/watch?v=-KL9APUjj3E',  format="video/mp4", start_time=0)
    with right_column:
        st.subheader(
            """
            Kami akan menjelaskan mengenai Ransomware, berikut merupakan video singkat penjelasan tentang ransomware. Silahkan disimak!
            """
        )
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.altair_chart(line_chart, use_container_width=True)

    with right_column:
        st.markdown(
            """
            Grafik disamping merupakan grafik serangan siber yang terjadi setiap bulannya di Indonesia sepanjang tahun 2021. 
            Data tersebut diambil dari Laporan Tahunan bertajuk "Monitoring Keamanan Siber" untuk tahun 2021. 
            Laporan ini sudah dipublikasikan di situs resmi Id-SIRTII/CC (Indonesia Security Incident Response Team on Internet Infrastucture/Coordination Center)
            yang berada dibawah Direktori Operasi Keaman Siber BSSN.
            """
        )

    st.write("---")
