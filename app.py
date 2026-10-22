import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My Private Gallery",
    page_icon="",
    layout="centered"
)

# Session state initialization
if 'page' not in st.session_state:
    st.session_state.page = 'home'

if 'my_photos' not in st.session_state:
    st.session_state.my_photos = []

# --- PAGE 1: HOME & GALLERY ---
if st.session_state.page == 'home':
    st.markdown("<h2 style='text-align: center;'> My Private Photo Gallery</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
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
        st.info("လောလောဆယ် ဓာတ်ပုံ မရှိသေးပါ။")
    else:
        col_a, col_b = st.columns(2)
        for i, item in enumerate(st.session_state.my_photos):
            target_col = col_a if i % 2 == 0 else col_b
            with target_col:
                st.image(item["file"], use_container_width=True)
                st.write(f"**{item['title']}**")

# --- PAGE 2: NEW VIBE UI WITH BACKGROUND IMAGE & HEARTS ---
elif st.session_state.page == 'new_ui':
    # Background Image using Streamlit image container
    st.image("https://images.unsplash.com/photo-1518709268805-4e9042af9f23", use_container_width=True)
    
    st.markdown("<h2 style='text-align: center; color: #ff4d6d;'> Special Vibe UI </h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #cbd5e1;'>နောက်ခံပုံစံအလန်းစားနှင့် လှပသော UI အသစ်ဖြစ်ပါသည်။</p>", unsafe_allow_html=True)
    
    st.write("")
    if st.button(" ပင်မစာမျက်နှာသို့ ပြန်ရန်", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
