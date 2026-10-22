import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My Private Gallery",
    page_icon="",
    layout="centered"
)

# Custom CSS for Modern Dark Vibe, Background Image & Heart Animation
st.markdown("""
    <style>
    .main {
        background-color: #090d16;
        color: #ffffff;
    }
    .stApp {
        background-color: #090d16;
    }
    
    /* Background style for the new UI with subtle overlay */
    .new-ui-bg {
        background: linear-gradient(rgba(9, 13, 22, 0.85), rgba(9, 13, 22, 0.85)), 
                    url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23');
        background-size: cover;
        background-position: center;
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(5px);
        text-align: center;
        position: relative;
        overflow: hidden;
    }

    .gallery-header {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }
    .photo-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 10px;
        text-align: center;
        margin-bottom: 15px;
    }
    .photo-title {
        color: #e2e8f0;
        font-size: 14px;
        margin-top: 10px;
    }

    /* Floating Hearts Animation CSS */
    @keyframes floatUp {
        0% {
            transform: translateY(0px) scale(0.6);
            opacity: 0;
        }
        50% {
            opacity: 0.8;
        }
        100% {
            transform: translateY(-250px) scale(1.2);
            opacity: 0;
        }
    }
    .heart {
        position: absolute;
        color: #ec4899;
        font-size: 24px;
        animation: floatUp 4s infinite ease-in-out;
        z-index: 10;
    }
    .heart:nth-child(1) { left: 10%; animation-delay: 0s; }
    .heart:nth-child(2) { left: 30%; animation-delay: 1.2s; }
    .heart:nth-child(3) { left: 50%; animation-delay: 0.5s; }
    .heart:nth-child(4) { left: 70%; animation-delay: 2s; }
    .heart:nth-child(5) { left: 90%; animation-delay: 1s; }
    </style>
""", unsafe_allow_html=True)

# Session state to track navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

if 'my_photos' not in st.session_state:
    st.session_state.my_photos = []

# --- PAGE 1: HOME & GALLERY PAGE ---
if st.session_state.page == 'home':
    st.markdown('<div class="gallery-header"> My Private Photo Gallery</div>', unsafe_allow_html=True)

    # Skip / Jump Button to New UI
    col_skip1, col_skip2, col_skip3 = st.columns([1, 2, 1])
    with col_skip2:
        if st.button(" ကျော်ရန် (Vibe UI သို့သွားမည်)", use_container_width=True):
            st.session_state.page = 'new_ui'
            st.rerun()

    # Sidebar for Admin Authentication
    st.sidebar.markdown("###  Admin Control")
    admin_password = st.sidebar.text_input("Admin Password ထည့်ပါ", type="password")

    is_admin = False
    if admin_password == "1234":
        is_admin = True
        st.sidebar.success("Admin အဖြစ် ဝင်ရောက်ပြီးပါပြီ ")
    elif admin_password != "":
        st.sidebar.error("Password မှားယွင်းနေပါသည်။")

    # Show Upload section ONLY IF admin is logged in
    if is_admin:
        st.markdown("---")
        st.markdown("###  ဓာတ်ပုံအသစ် တင်ရန် (Admin Only)")
        uploaded_file = st.file_uploader("ဓာတ်
