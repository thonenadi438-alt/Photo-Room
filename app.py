import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My Private Gallery",
    page_icon="",
    layout="centered"
)

# Custom CSS for Modern Dark Vibe
st.markdown("""
    <style>
    .main {
        background-color: #090d16;
        color: #ffffff;
    }
    .stApp {
        background-color: #090d16;
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
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="gallery-header"> My Private Photo Gallery</div>', unsafe_allow_html=True)

# Sidebar for Admin Authentication
st.sidebar.markdown("###  Admin Control")
# လိုချင်သော Password ကို သတ်မှတ်နိုင်ပါသည် (ဥပမာ - 1234)
admin_password = st.sidebar.text_input("Admin Password ထည့်ပါ", type="password")

is_admin = False
if admin_password == "1234":  # <--- ဒီနေရာတွင် ကိုယ်ကြိုက်တဲ့ Password ပြောင်းနိုင်ပါတယ်
    is_admin = True
    st.sidebar.success("Admin အဖြစ် ဝင်ရောက်ပြီးပါပြီ ")
elif admin_password != "":
    st.sidebar.error("Password မှားယွင်းနေပါသည်။")

# Session state to store uploaded photos permanently during the session
if 'my_photos' not in st.session_state:
    st.session_state.my_photos = []

# Show Upload section ONLY IF admin is logged in
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

# Display Gallery Grid
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
