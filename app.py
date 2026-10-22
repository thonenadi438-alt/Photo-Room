import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My Private Gallery",
    page_icon="",
    layout="centered"
)

# Custom CSS for Pure Black Background & Floating Hearts Animation
st.markdown("""
    <style>
    .main {
        background-color: #000000;
        color: #ffffff;
    }
    .stApp {
        background-color: #000000;
    }
    
    .vibe-box {
        position: relative;
        background-color: #0b0f19;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        overflow: hidden;
        box-shadow: 0 10px 25px rgba(0,0,0,0.8);
        margin-bottom: 20px;
    }

    .vibe-title {
        font-size: 28px;
        font-weight: bold;
        color: #ec4899;
        margin-bottom: 15px;
    }

    @keyframes flyUp {
        0% {
            transform: translateY(0px) scale(0.6);
            opacity: 0;
        }
        50% {
            opacity: 1;
        }
        100% {
            transform: translateY(-300px) scale(1.2);
            opacity: 0;
        }
    }

    .heart-anim {
        position: absolute;
        bottom: 20px;
        color: #ff4d6d;
        font-size: 26px;
        animation: flyUp 3.5s infinite ease-in-out;
        z-index: 10;
    }
    .h1 { left: 15%; animation-delay: 0s; }
    .h2 { left: 35%; animation-delay: 1s; }
    .h3 { left: 55%; animation-delay: 0.4s; }
    .h4 { left: 75%; animation-delay: 1.8s; }
    .h5 { left: 85%; animation-delay: 0.8s; }

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
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

if 'my_photos' not in st.session_state:
    st.session_state.my_photos = []

# --- PAGE 1: HOME & GALLERY ---
if st.session_state.page == 'home':
    st.markdown('<div class="gallery-header"> My Private Photo Gallery</div>', unsafe_allow_html=True)

    col_skip1, col_skip2, col_skip3 = st.columns([1, 2, 1])
    with col_skip2:
        if st.button(" ကျော်ရန် (UI အသစ်သို့ သွားမည်)", use_container_width=True):
            st.session_state.page = 'new_ui'
            st.rerun()

    st.sidebar.markdown("###  Admin Control")
    admin_password = st.sidebar.text_input("Admin Password ထည့်ပါ", type="password")

    is_admin = False
    if admin_password == "1234":
        is_admin = True
        st.sidebar.success("Admin အဖြစ် ဝင်ရောက်ပြီးပါပြီ ")
    elif admin_password != "":
        st.sidebar.error("Password မှားယွင်းနေပါသည်။")

    if is_admin:
        st.markdown("---")
        st.markdown("###  ဓာတ်ပုံအသစ် တင်ရန် (Admin Only)")
        uploaded_file = st.file_uploader("ဓာတ်ပုံရွေးချယ်ပါ", type=["jpg", "png", "jpeg"])
        photo_caption = st.text_input("ဓာတ်ပုံအမည် သို့မဟုတ် မှတ်ချက်")
        
        if st.button("Upload လုပ်မည်"):
            if uploaded_file is not None:
                st.session_state.my_photos.append({"file": uploaded_file, "title": photo_caption if photo_caption else "Untitled"})
                st.success("ဓာတ်ပုံ အောင်မြင်စွာ တင်ပြီးပါပြီ!")
            else:
                st.warning("ကျေးဇူးပြု၍ ဓာတ်ပုံအရင် ရွေးချယ်ပါ။")
    else:
        st.info("ဓာတ်ပုံအသစ်တင်ရန် ဘယ်ဘက် ဘေးဘောင်တွင် Admin Password ထည့်ပါ။")

    st.markdown("---")
    st.markdown("###  တင်ထားသော ဓာတ်ပုံများ")

    if len(st.session_state.my_photos) == 0:
        st.markdown("<p style='text-align: center; color: #64748b;'>လောလောဆယ် ဓာတ်ပုံ မရှိသေးပါ။</p>", unsafe_allow_html=True)
    else:
        col1, col2 = st.columns(2)
        for i, item in enumerate(st.session_state.my_photos):
            target_col = col1 if i % 2 == 0 else col2
            with target_col:
                st.markdown('<div class="photo-card">', unsafe_allow_html=True)
                st.image(item["file"], use_container_width=True)
                st.markdown(f'<div class="photo-title">{item["title"]}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 2: NEW VIBE UI (BLACK BG, IMAGE & FLOATING HEARTS) ---
elif st.session_state.page == 'new_ui':
    st.markdown("""
        <div class="vibe-box">
            <div class="heart-anim h1"></div>
            <div class="heart-anim h2"></div>
            <div class="heart-anim h3"></div>
            <div class="heart-anim h4"></div>
            <div class="heart-anim h5"></div>
            <div class="vibe-title"> Special Vibe UI </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1534447677768-be436bb09401", use_container_width=True, caption=" My Special Vibe Photo")
    
    st.write("")
    if st.button(" ပင်မစာမျက်နှာသို့ ပြန်ရန်", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
