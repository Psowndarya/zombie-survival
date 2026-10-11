import streamlit as st

st.set_page_config(
    page_title="LAST STAND | Zombie Survival",
    page_icon="🧟",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- THEME ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800&family=Inter:wght@400;500;700&display=swap');

.stApp {
    background: #080a0d;
    color: #f2f2f2;
    font-family: 'Inter', sans-serif;
}

header, footer {visibility: hidden;}
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1250px;
}

h1, h2, h3 {
    font-family: 'Orbitron', sans-serif !important;
}

.brand {
    font-family: 'Orbitron', sans-serif;
    font-size: 23px;
    font-weight: 800;
    letter-spacing: 3px;
    color: #f04444;
}

.status {
    color: #ff4c4c;
    font-size: 12px;
    letter-spacing: 3px;
    font-weight: bold;
}

.hero {
    background:
      linear-gradient(90deg, rgba(5,7,10,.97) 0%,
      rgba(5,7,10,.78) 52%, rgba(5,7,10,.35) 100%),
      linear-gradient(0deg, #080a0d 0%, transparent 50%),
      url('https://images.unsplash.com/photo-1519608487953-e999c86e7455?auto=format&fit=crop&w=1800&q=85');
    background-size: cover;
    background-position: center;
    min-height: 470px;
    border: 1px solid #292929;
    border-left: 4px solid #e53939;
    border-radius: 8px;
    padding: 55px 42px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.hero h1 {
    font-size: clamp(36px, 6vw, 76px);
    line-height: 1.05;
    letter-spacing: 2px;
    margin: 15px 0;
    color: #ffffff;
}

.hero h1 span { color: #f04444; }

.hero p {
    color: #c5c8ce;
    max-width: 570px;
    line-height: 1.8;
    font-size: 16px;
}

.stButton > button {
    background: #e53939;
    color: white;
    border: 1px solid #e53939;
    border-radius: 3px;
    min-height: 46px;
    font-family: 'Orbitron', sans-serif;
    font-weight: bold;
    letter-spacing: 1px;
    transition: .2s ease;
}

.stButton > button:hover {
    background: #ff5555;
    color: white;
    border-color: #ff5555;
    transform: translateY(-2px);
}

div[data-testid="stHorizontalBlock"] {
    gap: 12px;
}

.panel {
    background: linear-gradient(145deg, #15181e, #0d0f13);
    border: 1px solid #2a2d34;
    border-radius: 6px;
    padding: 22px;
    min-height: 155px;
    transition: .2s;
}

.panel h3 {
    color: #f04444;
    font-size: 17px;
}

.panel p {
    color: #a8adb7;
    line-height: 1.7;
    font-size: 14px;
}

.section-label {
    color: #f04444;
    letter-spacing: 3px;
    font-size: 11px;
    font-weight: bold;
}

.small {
    color: #9da3ad;
    font-size: 12px;
}

hr { border-color: #292d34; }

@media (max-width: 640px) {
    .hero { padding: 28px 20px; min-height: 370px; }
    .hero h1 { font-size: 38px; }
    .brand { font-size: 16px; letter-spacing: 1px; }
}
</style>
""", unsafe_allow_html=True)

# ---------- PAGE STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "HOME"

def navigate(page):
    st.session_state.page = page

# ---------- TOP NAVIGATION ----------
top1, top2 = st.columns([2, 3])

with top1:
    st.markdown(
        '<div class="brand">☣ LAST STAND</div>',
        unsafe_allow_html=True
    )

with top2:
    n1, n2, n3, n4 = st.columns(4)
    with n1:
        st.button("HOME", use_container_width=True,
                  on_click=navigate, args=("HOME",))
    with n2:
        st.button("SURVIVAL", use_container_width=True,
                  on_click=navigate, args=("SURVIVAL",))
    with n3:
        st.button("MISSIONS", use_container_width=True,
                  on_click=navigate, args=("MISSIONS",))
    with n4:
        st.button("EXPLORE", use_container_width=True,
                  on_click=navigate, args=("EXPLORE",))

st.markdown("<hr>", unsafe_allow_html=True)

# ---------- HOME PAGE ----------
if st.session_state.page == "HOME":

    st.markdown("""
    <div class="hero">
        <div class="status">⚠ EMERGENCY BROADCAST // DAY 047</div>
        <h1>THE WORLD<br>IS <span>DEAD.</span></h1>
        <p>
        The infection has consumed the cities. Civilization has fallen.
        The dead walk among us, and hope is running out.
        Every bullet counts. Every decision matters.
        How long will YOU survive?
        </p>
        <div class="small">
        LOCATION: UNKNOWN &nbsp; | &nbsp;
        THREAT LEVEL: CRITICAL &nbsp; | &nbsp;
        SURVIVORS: FEW
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    b1, b2, b3 = st.columns([1.3, 1, 2])

    with b1:
        st.button(
            "☠ START SURVIVAL",
            use_container_width=True,
            on_click=navigate,
            args=("SURVIVAL",)
        )

    with b2:
        st.button(
            "▸ VIEW MISSIONS",
            use_container_width=True,
            on_click=navigate,
            args=("MISSIONS",)
        )

    st.write("")
    st.markdown(
        '<div class="section-label">// YOUR FIGHT BEGINS HERE</div>',
        unsafe_allow_html=True
    )
    st.markdown("## SURVIVE THE COLLAPSE")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="panel">
        <h3>☣ SURVIVAL</h3>
        <p>Manage health, collect supplies, craft equipment
        and stay alive against the infected.</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("ENTER SURVIVAL →", key="surv_card",
                  use_container_width=True,
                  on_click=navigate, args=("SURVIVAL",))

    with c2:
        st.markdown("""
        <div class="panel">
        <h3>⚔ MISSIONS</h3>
        <p>Accept dangerous objectives, rescue survivors
        and uncover the truth behind the outbreak.</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("VIEW MISSIONS →", key="mission_card",
                  use_container_width=True,
                  on_click=navigate, args=("MISSIONS",))

    with c3:
        st.markdown("""
        <div class="panel">
        <h3>🌆 EXPLORE</h3>
        <p>Search abandoned cities, discover hidden
        resources and enter infected territories.</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("EXPLORE WORLD →", key="explore_card",
                  use_container_width=True,
                  on_click=navigate, args=("EXPLORE",))

    st.write("")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        '<div class="small">LAST STAND // NO RESCUE IS COMING. '
        'SURVIVE AT ALL COSTS.</div>',
        unsafe_allow_html=True
    )

# ---------- SURVIVAL PAGE ----------
elif st.session_state.page == "SURVIVAL":
    st.markdown(
        '<div class="section-label">// PLAYER STATUS</div>',
        unsafe_allow_html=True
    )
    st.title("SURVIVAL CENTER")
    st.write("You are alive. For now. Check your supplies.")

    a, b, c = st.columns(3)
    a.metric("❤️ HEALTH", "100 / 100")
    b.metric("🔋 STAMINA", "85 / 100")
    c.metric("🍖 FOOD", "3 DAYS")

    st.markdown("### FIELD ACTIONS")
    x, y = st.columns(2)

    with x:
        if st.button("🔍 Search for supplies",
                     use_container_width=True):
            st.success("You found 2 cans of food and clean water!")

    with y:
        if st.button("🩹 Rest and recover",
                     use_container_width=True):
            st.info("You rested safely. Health restored!")

    st.button("← BACK HOME", on_click=navigate,
              args=("HOME",))

# ---------- MISSIONS PAGE ----------
elif st.session_state.page == "MISSIONS":
    st.markdown(
        '<div class="section-label">// ACTIVE OPERATIONS</div>',
        unsafe_allow_html=True
    )
    st.title("MISSION BOARD")

    missions = [
        ("01", "THE LAST SUPPLY",
         "Search the abandoned supermarket for food.",
         "REWARD: 50 XP"),
        ("02", "SILENT DISTRESS",
         "Investigate a radio signal from the old hospital.",
         "REWARD: 100 XP"),
        ("03", "CITY OF THE DEAD",
         "Reach the safe zone through an infected district.",
         "REWARD: 200 XP")
    ]

    for number, title, description, reward in missions:
        st.markdown(f"""
        <div class="panel">
        <div class="section-label">MISSION {number}</div>
        <h3>{title}</h3>
        <p>{description}</p>
        <div class="small">{reward}</div>
        </div>
        """, unsafe_allow_html=True)
        st.write("")

    st.button("← BACK HOME", on_click=navigate,
              args=("HOME",))

# ---------- EXPLORE PAGE ----------
elif st.session_state.page == "EXPLORE":
    st.markdown(
        '<div class="section-label">// UNKNOWN TERRITORIES</div>',
        unsafe_allow_html=True
    )
    st.title("EXPLORE THE WASTELAND")

    places = {
        "Abandoned City": "High danger. Valuable supplies.",
        "Dark Forest": "Medium danger. Wildlife and shelter.",
        "Old Hospital": "Extreme danger. Medical resources."
    }

    choice = st.selectbox("Choose your destination",
                          list(places.keys()))

    st.info(places[choice])

    if st.button("SCOUT LOCATION", use_container_width=True):
        st.success(f"Scouting started: {choice}")

    st.button("← BACK HOME", on_click=navigate,
              args=("HOME",))
