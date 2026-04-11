# computational-chemistry-project
# 🔬 Gibbs Free Energy Analyzer

An interactive **Streamlit-based thermodynamics visualization tool** to analyze reaction spontaneity using **Gibbs Free Energy (ΔG)**. This application helps users explore how temperature and entropy affect reaction feasibility with dynamic graphs and insights.

## 🚀 Features

i)✅ Core Functionality

* Calculate **Gibbs Free Energy (ΔG = ΔH − TΔS)**
* Determine reaction nature:

  * Spontaneous
  * Non-spontaneous
  * Equilibrium

  ii)📊 Visualization

* **ΔG vs Temperature graph**
* Highlighted regions:

  * Spontaneous (ΔG < 0)
  * Non-spontaneous (ΔG > 0)
* Real-time plotting based on user inputs

iii) 🌡️ Equilibrium Analysis

* Detects approximate **equilibrium temperature**
* Displays whether current state is above/below equilibrium

iv) 🧠 Smart Insights

* Predicts behavior based on thermodynamic conditions
* Provides intuitive explanations for reaction feasibility

v) 🔥 Advanced Feature (WOW Factor)

* **Spontaneity Phase Map (Heatmap)**

  * Shows ΔG across a range of temperatures and entropy values
  * Clearly visualizes regions of spontaneity

## 🧮 Thermodynamic Background

The application is based on the Gibbs Free Energy equation:

[
Delta G = Delta H - T Delta S
]

Where:

* **ΔH** = Enthalpy change
* **ΔS** = Entropy change
* **T** = Temperature (Kelvin)

### Interpretation:

* ΔG < 0 → Spontaneous reaction
* ΔG > 0 → Non-spontaneous reaction
* ΔG = 0 → Equilibrium

## 🛠️ Tech Stack

* Python
* Streamlit (UI & interactivity)
* NumPy (numerical computation)
* Matplotlib (data visualization)

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gibbs-analyzer.git
cd gibbs-analyzer
```

### 2. Install dependencies

```bash
pip install streamlit numpy matplotlib
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 🎯 Usage

1. Enter:

   * ΔH (Enthalpy)
   * ΔS (Entropy)
   * Temperature (Slider)

2. Click **"Run Analysis"**

3. Explore:

   * ΔG result
   * Reaction condition
   * Graphs and phase map
   * Equilibrium insights

---

## 📌 Example

| Parameter | Value |
| --------- | ----- |
| ΔH        | 50    |
| ΔS        | 0.2   |
| T         | 300K  |

➡️ Output:

* ΔG = -10 → **Spontaneous Reaction**

---

## 🎨 UI Highlights

* Gradient dark theme
* Interactive sidebar inputs
* Metric cards for quick insights
* Clean and modern visualization

---

## ⚠️ Limitations

* Assumes constant ΔH and ΔS
* No pressure dependency included
* Approximate equilibrium detection (graph-based)

---

## 💡 Future Improvements

* Add pressure-based analysis
* Include real chemical reaction datasets
* Export results as PDF/CSV
* Deploy online (Streamlit Cloud)

---

## 👩‍💻 Author
* Developed by-
1.Saanya Mittal-25BCE10570
2.Anshika Singh 25BCE10770
3.Mahi Gupta 25MIP10061
4.Nivedita Jain 25MIM10038
