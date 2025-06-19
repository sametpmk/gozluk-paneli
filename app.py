
import streamlit as st

# Şifreli giriş
def login():
    st.title("🔐 Giriş Paneli")
    username = st.text_input("Kullanıcı Adı")
    password = st.text_input("Şifre", type="password")
    if st.button("Giriş Yap"):
        if username == "admin" and password == "gözlük123":
            st.session_state["giris"] = True
        else:
            st.error("❌ Hatalı giriş!")

# Ana panel (giriş sonrası)
def main_panel():
    st.sidebar.success("✅ Giriş Başarılı")
    secim = st.sidebar.radio("Sayfa Seç", ["📋 Siparişler", "👷 Evde Çalışanlar", "💼 Giderler", "👥 Ortak Ödemeleri", "📊 Raporlar"])
    st.title(secim)

    if secim == "📋 Siparişler":
        st.write("Buraya sipariş formu gelecek...")
    elif secim == "👷 Evde Çalışanlar":
        st.write("Buraya çalışan girişi gelecek...")
    elif secim == "💼 Giderler":
        st.write("Buraya gider girişi gelecek...")
    elif secim == "👥 Ortak Ödemeleri":
        st.write("Buraya ortak ödeme girişi gelecek...")
    elif secim == "📊 Raporlar":
        st.write("Buraya raporlar gelecek...")

if "giris" not in st.session_state:
    login()
else:
    main_panel()
