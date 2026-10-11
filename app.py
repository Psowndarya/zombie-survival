
import streamlit as st
from exploration import LOCATIONS, explore_location

st.set_page_config(
    page_title="Zombie Survival",
    page_icon="🧟",
    layout="wide"
)

st.title("🧟 Zombie Survival")
st.subheader("City Exploration")

st.write(
    "Choose a location, check its danger level, "
    "and explore to search for supplies."
)

# Initialize survivor status
if "health" not in st.session_state:
    st.session_state.health = 100

if "food" not in st.session_state:
    st.session_state.food = 50

if "water" not in st.session_state:
    st.session_state.water = 50

if "inventory" not in st.session_state:
    st.session_state.inventory = []

if "explored" not in st.session_state:
    st.session_state.explored = []

if "last_result" not in st.session_state:
    st.session_state.last_result = ""

# Survivor dashboard
st.header("Survivor Status")

col1, col2, col3 = st.columns(3)

col1.metric("❤️ Health", st.session_state.health)
col2.metric("🍎 Food", st.session_state.food)
col3.metric("💧 Water", st.session_state.water)

# City exploration
st.header("Explore the City")

location_name = st.selectbox(
    "Choose a location",
    list(LOCATIONS.keys())
)

# Get details for the selected location
location = LOCATIONS[location_name]

st.write("**Description:**", location["description"])
st.write("**Danger Level:**", location["danger"])
st.write("**Possible supplies:**", ", ".join(location["supplies"]))

# Explore button
if st.button("Explore Location"):
    if st.session_state.health <= 0:
        st.error("Your survivor has no health left!")
    else:
        result = explore_location(location_name)
        messages = []

        if result["encounter"]:
            damage = result["damage"]

            st.session_state.health = max(
                0,
                st.session_state.health - damage
            )

            messages.append(
                f"🧟 Zombie encounter! You lost {damage} health."
            )
        else:
            messages.append(
                "✅ No zombie encounter this time!"
            )

        # Collect the supply
        supply = result["supply"]
        st.session_state.inventory.append(supply)

        # Apply supply benefits
        if supply == "Medicine":
            st.session_state.health = min(
                100, st.session_state.health + 10
            )
        elif supply == "First Aid Kit":
            st.session_state.health = min(
                100, st.session_state.health + 15
            )
        elif supply == "Food":
            st.session_state.food += 20
        elif supply == "Water":
            st.session_state.water += 20

        messages.append(f"🎒 You found: {supply}")

        if location_name not in st.session_state.explored:
            st.session_state.explored.append(location_name)

        st.session_state.last_result = "\n\n".join(messages)

# Show latest result
if st.session_state.last_result:
    st.subheader("Exploration Result")
    st.info(st.session_state.last_result)

# Show all locations
st.header("📍 Available Locations")

for name, details in LOCATIONS.items():
    with st.expander(name):
        st.write(details["description"])
        st.write("**Danger:**", details["danger"])
        st.write(
            "**Possible supplies:**",
            ", ".join(details["supplies"])
        )

        if name in st.session_state.explored:
            st.success("Explored")

# Inventory
st.header("🎒 Survivor Inventory")

if st.session_state.inventory:
    for item in st.session_state.inventory:
        st.write(f"- {item}")
else:
    st.write("Your inventory is empty.")

# Progress
st.write(
    f"Locations explored: "
    f"{len(st.session_state.explored)} / {len(LOCATIONS)}"
)

if len(st.session_state.explored) == len(LOCATIONS):
    st.success("You have explored every available location!")
