import streamlit as st
import random

st.set_page_config(page_title="Fortune Lab - Dragon & Potion", layout="wide")

st.title("🐉 Fortune Lab 🧪")
st.subheader("Pet Dragon & Potion Maker")

page = st.sidebar.radio("Choose an activity", ["🐉 Pet Dragon", "🧪 Potion Maker", "Home"])

if "dragon_name" not in st.session_state:
    st.session_state.dragon_name = None
    st.session_state.dragon_color = None
    st.session_state.dragon_power = None
    st.session_state.dragon_health = 100
    st.session_state.dragon_happiness = 100

if "potion_ingredient" not in st.session_state:
    st.session_state.potion_ingredient = None
    st.session_state.potion_effect = None

dragon_names = [
    "Flamewing", "Shadowclaw", "Mochi", "Sparkletoes", "Bubbles",
    "Whiskerflame", "Frostbite", "Toothless", "Emberstorm", "Luna",
]

dragon_colors = [
    "Crimson Red", "Midnight Black", "Pink", "Golden Yellow", "Sky Blue",
    "Emerald Green", "Silver", "Violet", "Orange", "White",
]

dragon_powers = [
    "Fire Breath", "Invisibility", "Water Manipulation", "Makes unlimited pancakes",
    "Lightning Strike", "Ice Shards", "Earthquake", "Controls the weather",
    "Telekinesis", "Time Manipulation",
]

potion_ingredients = [
    "misty dust", "crystal shard", "moonflower petal", "sunstone fragment",
    "glimmering dew", "whispering wind essence", "glittery water droplet",
    "sparkling stardust",
]

potion_effects = [
    "grants temporary invisibility", "enhances magical abilities",
    "boosts energy and vitality", "induces a state of euphoria",
    "provides protection against dark forces", "allows communication with mystical creatures",
    "increases luck and fortune", "heals minor wounds and ailments",
]

if page == "Home":
    st.write("Welcome to Fortune Lab! Choose an activity from the sidebar:")
    col1, col2 = st.columns(2)

    with col1:
        st.info("### 🐉 Pet Dragon\nCreate and care for your own magical dragon!")

    with col2:
        st.info("### 🧪 Potion Maker\nBrew magical potions with mystical ingredients!")

elif page == "🐉 Pet Dragon":
    st.header("🐉 Your Pet Dragon")

    st.subheader("Summon Your Dragon")

    if st.button("🎲 Create New Dragon", key="new_dragon"):
        st.session_state.dragon_name = random.choice(dragon_names)
        st.session_state.dragon_color = random.choice(dragon_colors)
        st.session_state.dragon_power = random.choice(dragon_powers)
        st.session_state.dragon_health = 100
        st.session_state.dragon_happiness = 100
        st.success("Your dragon has arrived!!!")

    if st.session_state.dragon_name:
        st.divider()
        st.subheader("Dragon Stats")

        col_stats1, col_stats2 = st.columns(2)
        with col_stats1:
            st.metric("Name", st.session_state.dragon_name)
            st.metric("Color", st.session_state.dragon_color)
        with col_stats2:
            st.metric("Power", st.session_state.dragon_power)

        st.divider()
        st.subheader("Care for Your Dragon")

        col_action1, col_action2, col_action3 = st.columns(3)

        with col_action1:
            if st.button("🍖 Feed"):
                st.session_state.dragon_health = min(100, st.session_state.dragon_health + 15)
                st.session_state.dragon_happiness = min(100, st.session_state.dragon_happiness + 10)
                st.success(f"{st.session_state.dragon_name} is happy!")

        with col_action2:
            if st.button("🎮 Play"):
                st.session_state.dragon_happiness = min(100, st.session_state.dragon_happiness + 20)
                st.session_state.dragon_health = max(0, st.session_state.dragon_health - 5)
                st.success(f"{st.session_state.dragon_name} is having fun!")

        with col_action3:
            if st.button("💤 Rest"):
                st.session_state.dragon_health = min(100, st.session_state.dragon_health + 30)
                st.session_state.dragon_happiness = max(0, st.session_state.dragon_happiness - 5)
                st.success(f"{st.session_state.dragon_name} is rested!")

        st.divider()
        st.subheader("Health & Happiness")

        st.progress(st.session_state.dragon_health / 100, text=f"Health: {st.session_state.dragon_health}%")
        st.progress(st.session_state.dragon_happiness / 100, text=f"Happiness: {st.session_state.dragon_happiness}%")

        if st.session_state.dragon_happiness >= 80:
            st.success("✨ Your dragon is ecstatic!")
        elif st.session_state.dragon_happiness >= 50:
            st.info("😊 Your dragon is content")
        else:
            st.warning("😢 Your dragon needs more love!")

elif page == "🧪 Potion Maker":
    st.header("🧪 Magic Potion Lab")

    st.subheader("Brew Your Potion")

    if st.button("🎲 Mix Potion", key="brew_potion"):
        st.session_state.potion_ingredient = random.choice(potion_ingredients)
        st.session_state.potion_effect = random.choice(potion_effects)
        st.success("✨ Your potion is ready!")

    if st.session_state.potion_ingredient:
        st.divider()
        st.subheader("Your Potion Recipe")

        col_pot1, col_pot2 = st.columns(2)

        with col_pot1:
            st.info(f"**Main Ingredient:** {st.session_state.potion_ingredient}")

        with col_pot2:
            st.success(f"**Effect:** This potion {st.session_state.potion_effect}")

    st.divider()
    st.subheader("Available Ingredients")

    ingredient = st.selectbox("Choose your main ingredient:", potion_ingredients)
    effect = st.selectbox("Select the effect you want:", potion_effects)

    if st.button("📝 Custom Brew"):
        st.session_state.potion_ingredient = ingredient
        st.session_state.potion_effect = effect
        st.success("✨ Custom potion created!")
