import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Content", 
    page_icon=":computer:", 
    layout="wide"
)

# ---- LOAD ASSETS ----
img_ransomware = Image.open("images/ransomware.png")


# ---- isi content ransomware ----
def content_1():
    st.header("Ransomware")
    st.write("---")
    st.subheader("Apa itu _Ransomware_?")
    st.markdown(
        """
        \n
        Ransomware adalah jenis _malicious software_ atau _malware_ yang digunakan peretas untuk
mencuri informasi/data pribadi korban dan membatasi akses korban pada data tersebut
(enkripsi). Para peretas kemudian akan meminta tebusan kepada korban untuk mengembalikan
data yang dicuri. Biasanya tebusan diminta dalam bentuk **_Cryptocurrency_** agar tidak terlacak. \n \n
Seseorang dapat terkena _ransomware_ ketika menginstall _malware_ yang berkamuflase lewat
email-email spam maupun _software-software_ yang kelihatannya legal. Kemudian, jika terunduh,
_ransomware_ akan mencari celah pada pertahanan komputer atau _operation system_. Ketika
sudah masuk ke komputer korban, ransomware akan mengenkripsi data dengan tipe seperti
foto, dokumen, database, dan lainnya. Setelah file-file tersebut terenkripsi, maka peretas akan
menggunakan _ransomware_ untuk meminta tebusan kepada korban.
        \n \n \n
        """
    )
    st.image(img_ransomware, caption='Contoh serangan ransomware', use_column_width='auto' )
    st.write("\n")
    st.write("sumber: https://diskominfo.mojokertokab.go.id/artikel/mengenal-wannacry-ransomware-yang-serang-dunia-1558612102")
    

# ---- isi content jenis-jenis ransomware ----
def content_2():
    st.header("Jenis-Jenis _Ransomware_")
    st.write("---")
    st.subheader("a. _Crypto Ransomware_")
    st.markdown(
        """
        _Ransomware_ ini tidak mengenkripsi semua tipe data di komputer korban. Ia hanya
mengenkripsi tipe data yang dianggapnya penting seperti foto, video, atau
dokumen-dokumen. \n \n
        """
    )
    st.subheader("b. _Locker Ransomware_")
    st.markdown(
        """
        Jenis _ransomware_ ini mengenkripsi semua file yang ada di komputer korban. Korban
tidak akan bisa mengakses apapun selama komputer tersebut terkunci.
        """
    )
    st.subheader("c. _Doxware_")
    st.markdown(
        """
        Jenis _ransomware_ ini merupakan yang paling berbahaya karena ia bukan hanya
membatasi akses ke data korban namun juga mengancam untuk menyebarkan data
korban.
        """
    )

# ---- isi content Apa yang harus dilakukan ketika terkena Ransomware ----
def content_3():
    st.header("Apa yang harus dilakukan ketika terkena _Ransomware_?")
    st.write("---")
    st.markdown(
        """
        Sebetulnya, kecil kemungkinan data korban akan kembali tanpa membayar tebusan.
Namun kita dapat meminimalisir dampak dari _ransomware_ tersebut. \n \n
**Pertama**, putuskan sambungan ke jaringan dari komputer anda untuk menghindari
terinfeksinya komputer lain di jaringan tersebut.\n \n
**Kedua,** cari kunci dekripsi online. Biasanya terdapat komunitas besar berisi ahli
keamanan dunia maya yang berusaha untuk memecahkan jenis-jenis ransomware. Cari
tahu jenis _ransomware_ yang menginfeksi komputer anda lalu jelajahi situs seperti _“No
More Ransom”_ apakah kunci dekripsinya sudah dibuat. \n \n
**Ketiga,** hubungi profesional. Biasanya terdapat komunitas ahli atau toko reparasi lokal
yang sekiranya berpengalaman dalam mengatasi ransomware. Jangan lupa untuk
melaporkan serangan _ransomware_ ke penegak hukum setempat.
        """
    )

# ---- Apa yang harus dilakukan untuk mencegah terkena Ransomware ----
def content_4():
    st.header("Apa yang harus dilakukan untuk mencegah terkena _Ransomware_")
    st.write("---")
    st.markdown(
        """
        **Pertama,** jangan asal menginstall _software_ kecuali dari _marketplace_ resmi dan
terpercaya. Biasanya _ransomware_ berkamuflase menjadi _software_ gratis yang terkesan
legal. Software gratis ini dapat ditemui di situs web bajakan. \n \n
**Kedua,** jangan mengunduh file terlampir dari email yang tidak anda kenal. Biasanya file
dilampirkan dalam bentuk _.zip_. Anda dapat menemukan email seperti ini di bagian _spam_
maupun _inbox_ biasa.\n \n
**Ketiga,** hindari situs web yang terlihat mencurigakan. Jangan klik apapun jika anda
mengunjungi situs web yang mencurigakan. Jangan memberikan akses cookies pada
situs web tersebut.
        """
    )


function = {
    "Ransomware" : content_1,
    "Jenis-Jenis Ransomware" : content_2,
    "Apa yang harus dilakukan ketika terkena Ransomware" : content_3,
    "Apa yang harus dilakukan untuk mencegah terkena Ransomware" : content_4
}

selected_page = st.sidebar.selectbox("Daftar isi :", function.keys())
function[selected_page]()