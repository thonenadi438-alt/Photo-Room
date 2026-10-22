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

if 'page' not in st.session_state:
    st.session_state.page = 'home'

if 'my_photos' not in st.session_state:
    st.session_state.my_photos = []

if st.session_state.page == 'home':
    st.markdown('<div class="gallery-header"> My Private Photo Gallery</div>', unsafe_allow_html=True)

    col_skip1, col_skip2, col_skip3 = st.columns([1, 2, 1])
    with col_skip2:
        if st.button(" ကျော်ရန် (Vibe UI သို့သွားမည်)", use_container_width=True):
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

elif st.session_state.page == 'new_ui':
    st.markdown("""
        <div class="new-ui-bg">
            <div class="heart"></div>
            <div class="heart"></div>
            <div class="heart"></div>
            <div class="heart"></div>
            <div class="heart"></div>
            <h2 style="color: #ffffff; margin-bottom: 10px;"> Special Vibe UI </h2>
            <p style="color: #cbd5e1; font-size: 16px;">နောက်ခံပုံစံ ရေးရေးလေးနှင့် အသည်းနှလုံးလေးများ မိုးပေါ်ပျံတက်နေသော ပုံစံလေးဖြစ်ပါသည်...</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button(" ပင်မစာမျက်နှာသို့ ပြန်ရန်", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
