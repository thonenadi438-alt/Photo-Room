import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My Private Gallery",
    page_icon="",
    layout="centered"
)

# Custom CSS for Background Image & Floating Hearts Vibe UI
st.markdown("""
    <style>
    .main {
        background-color: #090d16;
        color: #ffffff;
    }
    .stApp {
        background-color: #090d16;
    }
    
    /* Vibe UI with Beautiful Background Image and Overlay */
    .vibe-container {
        position: relative;
        width: 100%;
        min-height: 500px;
        background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.7)), 
                          url('https://images.unsplash.com/photo-1534447677768-be436bb09401');
        background-size: cover;
        background-position: center;
        border-radius: 20px;
        padding: 40px 20px;
        text-align: center;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .vibe-title {
        font-size: 32px;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 0 2px 10px rgba(0,0,0,0.8);
        margin-bottom: 15px;
    }

    .vibe-text {
        font-size: 16px;
        color: #f1f5f9;
        text-shadow: 0 1px 5px rgba(0,0,0,0.8);
        margin-bottom: 30px;
    }

    /* Floating Hearts Animation */
    @keyframes floatUpHearts {
        0% {
            transform: translateY(0px) scale(0.5);
            opacity: 0;
        }
        50% {
            opacity: 1;
        }
        100% {
            transform: translateY(-350px) scale(1.3);
            opacity: 0;
        }
    }

    .heart-float {
        position: absolute;
        bottom: 10px;
        color: #ff4d6d;
        font-size: 28px;
        animation: floatUpHearts 3.5s infinite ease-in-out;
        z-index: 5;
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
        st.info(" ဓာတ်ပုံအသစ်တင်ရန် ဘယ်ဘက် ဘေးဘောင် (Sidebar) တွင် Admin Password ထည့်ပါ။")

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

# --- PAGE 2: NEW VIBE UI WITH BACKGROUND IMAGE & FLOATING HEARTS ---
elif st.session_state.page == 'new_ui':
    st.markdown("""
        <div class="vibe-container">
            <div class="heart-float h1"></div>
            <div class="heart-float h2"></div>
            <div class="heart-float h3"></div>
            <div class="heart-float h4"></div>
            <div class="heart-float h5"></div>
            
            <div class="vibe-title"> Special Vibe UI </div>
            <div class="vibe-text">နောက်ခံပုံစံအလန်းစားပေါ်တွင် အသည်းနှလုံးလေးများ မိုးပေါ်သို့ အလှပဆုံး ပျံတက်နေပါပြီ...</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button(" ပင်မစာမျက်နှာသို့ ပြန်ရန်", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
