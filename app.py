import streamlit as st
import time
import tracemalloc
import pandas as pd
import plotly.express as px

# ==========================================
# CONFIGURARE PAGINĂ & DESIGN ACCESIBIL (UDL)
# ==========================================
st.set_page_config(
    page_title="GreenCode & Adaptive Logic - RED Erasmus+",
    page_icon="🌱",
    layout="wide"
)

# CSS Custom pentru suport Dislexie și Contrast Înalt
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/opendyslexic');
    
    .dyslexia-font {
        font-family: 'OpenDyslexic', sans-serif !important;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #2e7d32;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# BARA LATERALĂ: SETĂRI & ADAPTAVILITATE
# ==========================================
st.sidebar.image("https://img.icons8.com/color/96/leaf.png", width=60)
st.sidebar.title("🌱 GreenCode RED")
st.sidebar.caption("Resursă Educațională Deschisă - Erasmus+")

# Switch Limba
lang = st.sidebar.radio("🌐 Limba / Language:", ["Română", "English"])

# Opțiuni de Accesibilitate (UDL)
st.sidebar.subheader("♿ Accesibilitate / UDL")
dyslexia_mode = st.sidebar.checkbox("Font OpenDyslexic (Suport Dislexie)")
high_contrast = st.sidebar.checkbox("Mod Contrast Înalt")

# Aplicare clasa CSS pentru font dacă e bifat
font_class = "dyslexia-font" if dyslexia_mode else ""

# Selecție Nivel Adaptiv
st.sidebar.subheader("🎯 Parcurs Adaptiv")
level = st.sidebar.selectbox(
    "Alege Nivelul de Învățare:",
    ["Level 1: Bază & Sprijin Vizual (Remediere)", 
     "Level 2: Consolidare & Debugging (Standard)", 
     "Level 3: Green Computing & Performanță (Avansat)"]
)

# ==========================================
# DICTIONAR TEXTE BILINGV
# ==========================================
txt = {
    "Română": {
        "title": "GreenCode: Algoritmica Sustenabilă și Învățarea Adaptivă",
        "subtitle": "Proiect RED creat pentru personalizarea învățării la Informatică și conștientizarea consumului energetic al codului.",
        "l1_title": "🔍 Level 1: Simulare Vizuală Pas-cu-Pas (Căutare Secvențială)",
        "l1_desc": "Vezi cum calculatorul verifică fiecare element din memorie unul câte unul.",
        "l2_title": "🛠️ Level 2: Laborator de Debugging & Corecție Cod",
        "l2_desc": "Găsește eroarea logică din algoritmul de mai jos pentru a opri bucla infinită!",
        "l3_title": "⚡ Level 3: Simulator Green IT - Amprenta de Carbon a Algoritmilor",
        "l3_desc": "Măsoară direct consumul energetic (Joules) și timpul de executare la Căutarea Secvențială vs. Căutarea Binară.",
        "run_sim": "Rulează Experimentul Energetic",
        "target_num": "Numărul căutat în memorie:",
        "array_size": "Dimensiunea setului de date (elemente):"
    },
    "English": {
        "title": "GreenCode: Sustainable Algorithms & Adaptive Learning",
        "subtitle": "OER Project designed for personalized CS learning and energy efficiency awareness in coding.",
        "l1_title": "🔍 Level 1: Step-by-Step Visual Simulation (Sequential Search)",
        "l1_desc": "See how the computer checks every element in memory one by one.",
        "l2_title": "🛠️ Level 2: Debugging Lab & Code Fix",
        "l2_desc": "Find the logical bug in the algorithm below to stop the infinite loop!",
        "l3_title": "⚡ Level 3: Green IT Simulator - Carbon Footprint of Algorithms",
        "l3_desc": "Directly measure energy consumption (Joules) and execution time for Sequential vs. Binary Search.",
        "run_sim": "Run Energy Experiment",
        "target_num": "Target number in memory:",
        "array_size": "Dataset size (elements):"
    }
}[lang]

# ==========================================
# HEADER PRINCIPAL
# ==========================================
st.markdown(f"<div class='{font_class}'>", unsafe_allow_html=True)
st.title(txt["title"])
st.caption(txt["subtitle"])
st.divider()

# ==========================================
# LEVEL 1: REMEDIERE & VIZUALIZARE PAS-CU-PAS
# ==========================================
if "Level 1" in level:
    st.header(txt["l1_title"])
    st.write(txt["l1_desc"])
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        numbers = [12, 45, 67, 89, 23, 56, 90]
        st.write("**Tablou de date în memorie:**", numbers)
        search_val = st.number_input("Ce număr cauți?", value=89)
        start_anim = st.button("▶️ Pornește Simularea Vizuală")
        
    with col2:
        if start_anim:
            st.write("---")
            found = False
            for idx, val in enumerate(numbers):
                time.sleep(0.5) # Simulare pas-cu-pas
                if val == search_val:
                    st.success(f"✅ Pasul {idx+1}: Valoarea {val} a fost GĂSITĂ la poziția (index) {idx}!")
                    found = True
                    break
                else:
                    st.warning(f"❌ Pasul {idx+1}: Elementul {val} de la indexul {idx} NU se potrivește.")
            if not found:
                st.error(f"⚠️ Valoarea {search_val} nu există în tablou.")
                
    st.info("💡 **Ghid Adaptiv:** Daca obții sub 3 pași în mod constant, poți trece la Level 2!")

# ==========================================
# LEVEL 2: CONSOLIDARE & DEBUGGING
# ==========================================
elif "Level 2" in level:
    st.header(txt["l2_title"])
    st.write(txt["l2_desc"])
    
    code_buggy = """
def cautare_element(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return f"Găsit la index {i}"
        # ⚠️ EROARE: Lipsește incrementarea lui i! (Buclă infinită)
    return "Nu a fost găsit"
    """
    st.code(code_buggy, language="python")
    
    st.subheader("Unde este eroarea care blochează procesorul?")
    answer = st.radio("Alege varianta corectă de remediere:", [
        "A. Condiția `while i < len(arr)` trebuie schimbată în `while i <= len(arr)`",
        "B. Trebuie adăugată instrucțiunea `i += 1` în interiorul buclei pentru a avansa.",
        "C. Instrucțiunea `return` trebuie eliminată."
    ])
    
    if st.button("Verifică Răspunsul"):
        if "B. Trebuie adăugată" in answer:
            st.success("🎉 CORECT! Fără incrementare (`i += 1`), procesorul rămâne blocat la indexul 0, consumând 100% resurse inutil.")
            st.balloons()
        else:
            st.error("❌ Incorect. Gândește-te ce se întâmplă cu valoarea variabilei `i` la fiecare pas.")

# ==========================================
# LEVEL 3: GREEN COMPUTING & SIMULATOR ENERGETIC
# ==========================================
elif "Level 3" in level:
    st.header(txt["l3_title"])
    st.write(txt["l3_desc"])
    
    c1, c2 = st.columns(2)
    with c1:
        n_elements = st.select_slider(txt["array_size"], options=[10000, 50000, 100000, 500000, 1000000], value=100000)
    with c2:
        target_val = n_elements - 1 # Cel mai nefavorabil caz
        st.write(f"**Cazul defavorabil:** Căutare după ultimul element (`{target_val}`).")
        
    if st.button(txt["run_sim"], type="primary"):
        data = list(range(n_elements))
        
        # 1. TEST CĂUTARE SECVENȚIALĂ
        tracemalloc.start()
        t0 = time.perf_counter_ns()
        
        steps_seq = 0
        for x in data:
            steps_seq += 1
            if x == target_val:
                break
                
        t1 = time.perf_counter_ns()
        tracemalloc.stop()
        
        time_seq_ms = (t1 - t0) / 1e6
        energy_seq_joules = (time_seq_ms / 1000.0) * 15.0 # Estimare TDP procesor 15W
        
        # 2. TEST CĂUTARE BINARĂ
        tracemalloc.start()
        t0 = time.perf_counter_ns()
        
        left, right = 0, n_elements - 1
        steps_bin = 0
        while left <= right:
            steps_bin += 1
            mid = (left + right) // 2
            if data[mid] == target_val:
                break
            elif data[mid] < target_val:
                left = mid + 1
            else:
                right = mid - 1
                
        t1 = time.perf_counter_ns()
        tracemalloc.stop()
        
        time_bin_ms = (t1 - t0) / 1e6
        energy_bin_joules = (time_bin_ms / 1000.0) * 15.0
        
        # REZULTATE COMPARATIVE
        col_res1, col_res2, col_res3 = st.columns(3)
        
        with col_res1:
            st.metric("Pași Secvențial", f"{steps_seq:,}")
            st.metric("Pași Binar", f"{steps_bin}")
            
        with col_res2:
            st.metric("Timp Secvențial", f"{time_seq_ms:.3f} ms")
            st.metric("Timp Binar", f"{time_bin_ms:.3f} ms")
            
        with col_res3:
            st.metric("Consum Energetic Secvențial", f"{energy_seq_joules:.6f} J")
            st.metric("Consum Energetic Binar", f"{energy_bin_joules:.6f} J")

        # GRAFIC PLOTLY
        df = pd.DataFrame({
            "Algoritm": ["Căutare Secvențială (O(n))", "Căutare Binară (O(log n))"],
            "Consum Energetic (Joules)": [energy_seq_joules, energy_bin_joules]
        })
        fig = px.bar(df, x="Algoritm", y="Consum Energetic (Joules)", color="Algoritm", 
                     title="Comparație Consum Energetic / Amprentă Carbon", text_auto='.6f')
        st.plotly_chart(fig, use_container_width=True)
        
        if energy_bin_joules > 0:
            ratio = energy_seq_joules / energy_bin_joules
            st.success(f"🌱 **Concluzie Green IT:** Căutarea Binară a fost de **{ratio:.1f}x mai eficientă energetic** decât Căutarea Secvențială pentru {n_elements:,} de date!")

st.markdown("</div>", unsafe_allow_html=True)
