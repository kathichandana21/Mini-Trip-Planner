import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Mini Trip Planner",
    page_icon="🧳",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
}

.trip-card {
    padding: 20px;
    border-radius: 15px;
    background-color: #ffffff;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: gray;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# DESTINATION DATA
# =========================================================

trip_data = {

    "Hyderabad": {
        "image": "https://images.unsplash.com/photo-1572425948041-a3e7f6b5b9b6",
        "places": [
            "Charminar",
            "Golconda Fort",
            "Hussain Sagar",
            "Ramoji Film City",
            "Salar Jung Museum"
        ],
        "food": [
            "Hyderabadi Biryani",
            "Haleem",
            "Irani Chai"
        ],
        "lat": 17.3850,
        "lon": 78.4867,
        "tip": "Try authentic Hyderabadi Biryani and visit Charminar in the evening."
    },

    "Goa": {
        "image": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2",
        "places": [
            "Baga Beach",
            "Calangute Beach",
            "Fort Aguada",
            "Dudhsagar Falls",
            "Basilica of Bom Jesus"
        ],
        "food": [
            "Goan Fish Curry",
            "Prawn Curry",
            "Bebinca"
        ],
        "lat": 15.2993,
        "lon": 74.1240,
        "tip": "Enjoy the beaches during sunset and explore local Goan food."
    },

    "Bangalore": {
        "image": "https://images.unsplash.com/photo-1596176530529-78163a4f8902",
        "places": [
            "Lalbagh Botanical Garden",
            "Cubbon Park",
            "Bangalore Palace",
            "ISKCON Temple",
            "Vidhana Soudha"
        ],
        "food": [
            "Masala Dosa",
            "Idli Vada",
            "Filter Coffee"
        ],
        "lat": 12.9716,
        "lon": 77.5946,
        "tip": "Visit Lalbagh and enjoy traditional South Indian breakfast."
    },

    "Chennai": {
        "image": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220",
        "places": [
            "Marina Beach",
            "Kapaleeshwarar Temple",
            "Fort St. George",
            "Government Museum",
            "Santhome Church"
        ],
        "food": [
            "Dosa",
            "Idli",
            "Sambar Rice"
        ],
        "lat": 13.0827,
        "lon": 80.2707,
        "tip": "Visit Marina Beach early morning and try traditional Tamil food."
    },

    "Ooty": {
        "image": "https://images.unsplash.com/photo-1593693397690-362cb9666fc2",
        "places": [
            "Ooty Lake",
            "Botanical Garden",
            "Doddabetta Peak",
            "Rose Garden",
            "Tea Museum"
        ],
        "food": [
            "Ooty Chocolate",
            "South Indian Meals",
            "Fresh Tea"
        ],
        "lat": 11.4064,
        "lon": 76.6932,
        "tip": "Carry warm clothes and don't miss the beautiful Nilgiri tea."
    },

    "Manali": {
        "image": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23",
        "places": [
            "Solang Valley",
            "Rohtang Pass",
            "Hadimba Temple",
            "Mall Road",
            "Manu Temple"
        ],
        "food": [
            "Momos",
            "Thukpa",
            "Siddu"
        ],
        "lat": 32.2396,
        "lon": 77.1887,
        "tip": "Carry warm clothes and check weather conditions before travelling."
    }
}


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">🧳 Mini Trip Planner</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Plan • Explore • Enjoy 🌍</div>',
    unsafe_allow_html=True
)

st.write("")


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("⚙️ Trip Settings")

st.sidebar.write("Enter your trip details")

destination = st.sidebar.selectbox(
    "📍 Destination",
    list(trip_data.keys())
)

days = st.sidebar.number_input(
    "📅 Number of Days",
    min_value=1,
    max_value=15,
    value=3
)

people = st.sidebar.number_input(
    "👥 Number of People",
    min_value=1,
    max_value=20,
    value=2
)

budget = st.sidebar.number_input(
    "💰 Total Budget (₹)",
    min_value=1000,
    value=10000,
    step=1000
)

travel_type = st.sidebar.selectbox(
    "🧳 Travel Type",
    ["Solo", "Friends", "Family", "Couple"]
)

accommodation = st.sidebar.selectbox(
    "🏨 Accommodation",
    [
        "Budget Hotel",
        "Standard Hotel",
        "Premium Hotel"
    ]
)

plan_button = st.sidebar.button(
    "✨ Plan My Trip"
)


# =========================================================
# DESTINATION INTRODUCTION
# =========================================================

data = trip_data[destination]

st.image(
    data["image"],
    caption=f"🌍 Explore {destination}",
    use_container_width=True
)

st.markdown(
    f"""
    <div class="trip-card">
    <h2>🌍 Welcome to {destination}!</h2>
    <p>
    Discover amazing places, delicious food and unforgettable
    experiences with your personalized trip plan.
    </p>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PLAN BUTTON
# =========================================================

if plan_button:

    # =====================================================
    # TRIP SUMMARY
    # =====================================================

    st.success("🎉 Your personalized trip plan is ready!")

    st.header("📋 Trip Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📍 Destination",
            destination
        )

    with col2:
        st.metric(
            "📅 Duration",
            f"{days} Days"
        )

    with col3:
        st.metric(
            "👥 Travellers",
            people
        )

    with col4:
        st.metric(
            "💰 Budget",
            f"₹{budget:,}"
        )


    # =====================================================
    # TRAVEL DETAILS
    # =====================================================

    st.subheader("🧳 Travel Details")

    detail1, detail2 = st.columns(2)

    with detail1:
        st.info(f"**Travel Type:** {travel_type}")

    with detail2:
        st.info(f"**Accommodation:** {accommodation}")


    # =====================================================
    # PLACES TO VISIT
    # =====================================================

    st.divider()

    st.header("📸 Top Places to Visit")

    places = data["places"]

    place_columns = st.columns(3)

    for index, place in enumerate(places):

        with place_columns[index % 3]:

            st.markdown(
                f"""
                <div class="trip-card">
                <h3>📍 {place}</h3>
                <p>⭐ Recommended place to visit</p>
                </div>
                """,
                unsafe_allow_html=True
            )


    # =====================================================
    # DAY-WISE ITINERARY
    # =====================================================

    st.divider()

    st.header("📅 Day-wise Itinerary")

    for day in range(1, days + 1):

        place = places[(day - 1) % len(places)]

        with st.expander(
            f"🌅 Day {day} - {place}"
        ):

            st.write(
                f"📍 **Morning:** Visit {place}"
            )

            st.write(
                "🍴 **Afternoon:** Enjoy local food and explore nearby areas."
            )

            st.write(
                "🌆 **Evening:** Relax, take photos and explore the local surroundings."
            )

            st.write(
                "🌙 **Night:** Return to hotel and rest."
            )


    # =====================================================
    # FOOD
    # =====================================================

    st.divider()

    st.header("🍴 Local Food You Should Try")

    food_columns = st.columns(3)

    for index, food in enumerate(data["food"]):

        with food_columns[index]:

            st.success(
                f"🍽️ {food}"
            )


    # =====================================================
    # BUDGET CALCULATION
    # =====================================================

    st.divider()

    st.header("💰 Estimated Budget")

    travel_cost = budget * 0.25
    hotel_cost = budget * 0.30
    food_cost = budget * 0.20
    activity_cost = budget * 0.15
    emergency_cost = budget * 0.10

    budget_data = pd.DataFrame({
        "Category": [
            "Travel",
            "Hotel",
            "Food",
            "Activities",
            "Emergency"
        ],

        "Cost": [
            travel_cost,
            hotel_cost,
            food_cost,
            activity_cost,
            emergency_cost
        ]
    })


    budget_col1, budget_col2 = st.columns(2)

    with budget_col1:

        st.dataframe(
            budget_data,
            use_container_width=True,
            hide_index=True
        )

        st.metric(
            "💵 Estimated Total Cost",
            f"₹{budget_data['Cost'].sum():,.0f}"
        )


    with budget_col2:

        fig, ax = plt.subplots()

        ax.pie(
            budget_data["Cost"],
            labels=budget_data["Category"],
            autopct="%1.1f%%"
        )

        ax.set_title(
            "Trip Budget Distribution"
        )

        st.pyplot(fig)


    # =====================================================
    # BUDGET STATUS
    # =====================================================

    total_cost = budget_data["Cost"].sum()

    if total_cost <= budget:

        st.success(
            f"✅ Great! Your estimated cost of ₹{total_cost:,.0f} "
            f"is within your budget."
        )

    else:

        st.warning(
            f"⚠️ Your estimated cost is ₹{total_cost:,.0f}. "
            f"Consider increasing your budget."
        )


    # =====================================================
    # MAP
    # =====================================================

    st.divider()

    st.header("🗺️ Destination Location")

    map_data = pd.DataFrame({
        "latitude": [data["lat"]],
        "longitude": [data["lon"]]
    })

    st.map(
        map_data,
        zoom=7
    )


    # =====================================================
    # TRAVEL TIP
    # =====================================================

    st.divider()

    st.header("💡 Travel Tip")

    st.info(
        data["tip"]
    )


    # =====================================================
    # FINAL MESSAGE
    # =====================================================

    st.divider()

    st.markdown(
        f"""
        <div class="trip-card">

        <h2>🎉 Have a Wonderful Trip!</h2>

        <p>
        Your <b>{days}-day trip</b> to <b>{destination}</b>
        for <b>{people} people</b> has been successfully planned.
        </p>

        <p>
        Pack your bags, explore new places and create
        beautiful memories! 🌍❤️
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.balloons()

else:

    st.info(
        "👈 Enter your trip details in the sidebar and "
        "click **✨ Plan My Trip** to generate your trip plan."
    )