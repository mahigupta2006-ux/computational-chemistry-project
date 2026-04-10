import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Title */
h1 {
    text-align: center;
    color: #00ffd5;
}

/* Cards */
.css-1d391kg {
    background-color: rgba(255, 255, 255, 0.05);
    border-radius: 15px;
    padding: 10px;
}

/* Buttons */
.stButton>button {
    background-color: #00ffd5;
    color: black;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}

/* Metrics */
[data-testid="stMetric"] {
    background-color: rgba(255,255,255,0.05);
    padding: 10px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# functions
# -----------------------------
def calc_gibbs(h, s, t):
    return h - t * s

def check_result(g):
    if g < 0:
        return "Spontaneous"
    elif g > 0:
        return "Not Spontaneous"
    else:
        return "Equilibrium"

def condition_analysis(h, s):
    if h < 0 and s > 0:
        return "Always spontaneous"
    elif h > 0 and s < 0:
        return "Never spontaneous"
    elif h < 0 and s < 0:
        return "Spontaneous at low temperature"
    elif h > 0 and s > 0:
        return "Spontaneous at high temperature"
    else:
        return "Special case"

# -----------------------------
# page setup
# -----------------------------
st.markdown("<h1> Gibbs Free Energy Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Advanced Thermodynamic Visualization Tool</p>", unsafe_allow_html=True)

# -----------------------------
# sidebar inputs
# -----------------------------
st.sidebar.header("Input Parameters")

h = st.sidebar.number_input("ΔH (Enthalpy)", value=50.0)
s = st.sidebar.number_input("ΔS (Entropy)", value=0.2)
t = st.sidebar.slider("Temperature (K)", 200, 1000, 300)

run = st.sidebar.button("Run Analysis")

# -----------------------------
# main content
# -----------------------------
if run:

    # =========================
    # RESULT SECTION
    # =========================
    st.markdown("## Analysis Section")

    g = calc_gibbs(h, s, t)

    col1, col2, col3 = st.columns(3)

    col1.metric("ΔG Value", round(g, 2))
    col2.metric("Temperature (K)", t)
    col3.metric("Condition", "See below")

    st.markdown("### 🧾 Detailed Condition")
    st.info(condition_analysis(h, s))

    result = check_result(g)

    if result == "Spontaneous":
        st.success("Reaction is Spontaneous (ΔG < 0)")
    elif result == "Not Spontaneous":
        st.error("Reaction is Not Spontaneous (ΔG > 0)")
    else:
        st.info("System is at Equilibrium")

    st.markdown("---")

    # =========================
    # GRAPH SECTION
    # =========================
    temps = list(range(200, 1000, 10))
    values = [calc_gibbs(h, s, temp) for temp in temps]

    fig, ax = plt.subplots()

    ax.plot(temps, values, linewidth=2)
    ax.axhline(0, linestyle="--")

    ax.fill_between(temps, values, 0, where=[v < 0 for v in values], alpha=0.3)
    ax.fill_between(temps, values, 0, where=[v > 0 for v in values], alpha=0.3)

    ax.scatter(t, g, s=100)

    ax.set_facecolor("#111111")
    fig.patch.set_facecolor("#111111")

    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("ΔG")
    ax.set_title("ΔG vs Temperature")

    st.pyplot(fig)

    # =========================
    # EQUILIBRIUM
    # =========================
    st.markdown("## Equilibrium Analysis")

    eq_found = False

    for i in range(1, len(values)):
        if values[i-1] * values[i] < 0:
            st.info(f"Equilibrium occurs near {temps[i]} K")
            eq_found = True
            break

    if not eq_found:
        st.warning("No equilibrium point in this range")

    st.markdown("---")

    # =========================
    # SMART INSIGHT
    # =========================
    st.markdown("## Smart Insight")

    if s != 0:
        eq_temp = h / s

        if eq_temp > 0:
            st.info(f"Equilibrium Temperature ≈ {round(eq_temp, 2)} K")

            if t < eq_temp:
                st.write("Currently below equilibrium → behavior may change at higher temperature.")
            else:
                st.write("Currently above equilibrium → reaction behavior already shifted.")

    st.markdown("---")

    # =========================
    # PHASE MAP (WOW PART)
    # =========================
    st.markdown("## Spontaneity Phase Map")

    temp_range = np.linspace(200, 1000, 60)
    entropy_range = np.linspace(-1, 1, 60)

    G = []

    for s_val in entropy_range:
        row = []
        for t_val in temp_range:
            row.append(calc_gibbs(h, s_val, t_val))
        G.append(row)

    G = np.array(G)

    fig2, ax2 = plt.subplots()

    heatmap = ax2.imshow(
        G,
        extent=[200, 1000, -1, 1],
        aspect='auto'
    )

    ax2.set_xlabel("Temperature (K)")
    ax2.set_ylabel("Entropy (ΔS)")
    ax2.set_title("Spontaneity Regions")

    plt.colorbar(heatmap, label="ΔG")

    st.pyplot(fig2)

    st.markdown("---")

    # =========================
    # INTERPRETATION
    # =========================
    st.markdown("## Interpretation")

    st.write("• Negative ΔG → Spontaneous region")
    st.write("• Positive ΔG → Non-spontaneous region")
    st.write("• The boundary between them represents equilibrium")
