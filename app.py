import streamlit as st
from agents import app
from fpdf import FPDF
import base64

# 1. Page Configuration
st.set_page_config(
    page_title="The Council - AI Strategy Simulator",
    page_icon="🏛️",  # or use "⚖️"
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. BRANDING SIDEBAR
with st.sidebar:
    st.image("logo.png",output_format="PNG") 
    st.markdown("### **Rohit's AI Studio**")
    st.caption("Building the future of Management Tech.")
    st.markdown("---")
    st.markdown("**Version:** 1.0 (Beta)")
    st.markdown("**Model:** Llama 3 70B")

# 3. PDF GENERATOR
def create_pdf(topic, cfo, union, visionary, ceo):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Header
    pdf.set_font("Arial", "B", 20)
    pdf.cell(200, 15, txt="THE COUNCIL", ln=True, align='C')
    pdf.set_font("Arial", "I", 12)
    pdf.cell(200, 10, txt="Strategy Simulation Report", ln=True, align='C')
    pdf.ln(10)
    
    # Topic
    pdf.set_font("Arial", "B", 12)
    pdf.set_fill_color(240, 240, 240)
    pdf.multi_cell(0, 10, txt=f"TOPIC: {topic}", align='L', fill=True)
    pdf.ln(10)
    
    # Sections
    def add_section(title, body, color=(0,0,0)):
        pdf.set_font("Arial", "B", 14)
        pdf.set_text_color(*color)
        pdf.cell(0, 10, txt=title, ln=True)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", size=11)
        pdf.multi_cell(0, 7, txt=body)
        pdf.ln(5)

    add_section("1. THE CFO (Financial View)", cfo, (16, 185, 129))   # Green
    add_section("2. THE UNION LEADER (People View)", union, (239, 68, 68)) # Red
    add_section("3. THE VISIONARY (Future View)", visionary, (139, 92, 246)) # Purple
    
    pdf.add_page()
    add_section("4. THE CEO VERDICT", ceo, (180, 83, 9)) # Gold
    
    return pdf.output(dest="S").encode("latin1")

# 4. WORLD-CLASS CSS
st.markdown("""
<style>
    /* MAIN BACKGROUND */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #1F2937 0%, #0E1117 100%);
        color: #FAFAFA;
    }

    /* TITLE STYLING */
    .council-title {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        font-size: 4.5rem;
        background: linear-gradient(135deg, #FFD700 10%, #FBFBFB 50%, #FFD700 90%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
        text-shadow: 0px 4px 20px rgba(255, 215, 0, 0.3);
    }
    .subtitle {
        text-align: center; color: #9CA3AF; font-size: 1.2rem; margin-bottom: 30px; letter-spacing: 3px; text-transform: uppercase;
    }

    /* INPUT AREA */
    .stTextArea textarea {
        background-color: #111827;
        color: white;
        caret-color: #FFD700; /* This makes the cursor GOLD! */
        border: 1px solid #374151;
        border-radius: 10px;
    }
    /* This handles the placeholder text color too */
    .stTextArea textarea::placeholder {
        color: #6B7280; 
    }

    /* BUTTON STYLING (Gold & Centered) */
    /* BUTTON STYLING (Gold & Centered) */
    /* Updated to target both standard buttons and form submit buttons */
    div.stButton > button, div.stFormSubmitButton > button {
        background: linear-gradient(135deg, #B45309 0%, #D97706 100%);
        color: white;
        border: none;
        padding: 15px 32px;
        font-size: 1.1rem;
        border-radius: 8px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 14px 0 rgba(180, 83, 9, 0.39);
    }
    
    div.stButton > button:hover, div.stFormSubmitButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(180, 83, 9, 0.23);
        background: linear-gradient(135deg, #D97706 0%, #F59E0B 100%);
        color: white;
    }

    /* ANIMATION KEYFRAMES */
    @keyframes slideUp {
        0% { opacity: 0; transform: translateY(50px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    /* CARD STYLING */
    .agent-card {
        background-color: rgba(30, 30, 36, 0.9);
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        /* ADD THIS LINE BELOW: */
        min-height: 350px; 
        /* This ensures short answers don't look tiny */
        border: 1px solid rgba(255,255,255,0.05);
        opacity: 0; 
        animation: slideUp 0.8s ease-out forwards;
    }
    
    .delay-1 { animation-delay: 0.2s; }
    .delay-2 { animation-delay: 0.4s; }
    .delay-3 { animation-delay: 0.6s; }
    .delay-4 { animation-delay: 0.8s; }

    /* BORDERS */
    .cfo-border { border-top: 4px solid #10B981; }
    .union-border { border-top: 4px solid #EF4444; }
    .visionary-border { border-top: 4px solid #8B5CF6; }
    .ceo-border { border: 1px solid #F59E0B; background: radial-gradient(circle at top, #2b2200, #000000); }

    /* TEXT */
    .agent-name { font-size: 1.6rem; font-weight: 700; margin-bottom: 5px; }
    .agent-role { font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1.5px; opacity: 0.7; font-weight: 600; }
    .agent-body { font-size: 1.05rem; line-height: 1.7; color: #D1D5DB; font-weight: 300; }

</style>
""", unsafe_allow_html=True)

# 5. HEADER & INSTRUCTIONS
# The trick: We use a <span> to shrink the font size of just the trademark symbol to 40%
st.markdown('<div class="council-title">THE COUNCIL<span style="font-size: 45%; vertical-align: top;">&trade;</span></div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Strategy Simulation System</div>', unsafe_allow_html=True)

# The "Manual" (Clean & Hidden by default)
with st.expander("💡 How to use The Council"):
    st.markdown("""
    **Welcome to the Boardroom.**
    This AI system simulates a high-stakes management meeting to help you make better decisions.
    
    1.  **Enter a Dilemma:** Type a strategic question (e.g., *"Should we switch to a 4-day work week?"*).
    2.  **Convene:** Click the button to wake up the agents.
    3.  **Analyze:** Watch the **CFO** (Money), **Union** (People), and **Visionary** (Future) debate.
    4.  **Decide:** The **CEO** will provide a final binding verdict.
    5.  **Export:** Download the official PDF report for your records.
    6.  **Language:** The agents speak different languages.
    """)

# 6. INPUT SECTION
# 6. INPUT SECTION (Now with Form Logic)
with st.container():
    # We create a Form to enable Cmd+Enter functionality
    with st.form(key="council_form"):
        topic = st.text_area(
            "", 
            placeholder="Enter a strategic management decision here...",
            height=100
        )
        
        # Centered Submit Button
        col_l, col_btn, col_r = st.columns([1, 2, 1])
        with col_btn:
            # Change: This is now a form_submit_button
            run_btn = st.form_submit_button("⚡ CONVENE THE COUNCIL", use_container_width=True)

# 7. MAIN LOGIC (No changes needed here, run_btn works the same)
if run_btn and topic:
    # ... rest of your code ...
    with st.spinner("The Council is deliberating..."):
        try:
            result = app.invoke({"topic": topic})
            
            # Cards
            c1, c2, c3 = st.columns(3)
            with c1: st.markdown(f"""<div class="agent-card cfo-border delay-1"><div class="agent-name" style="color:#10B981;">💰 The CFO</div><div class="agent-role">Financial Guardian</div><div class="agent-body">{result['cfo_opinion']}</div></div>""", unsafe_allow_html=True)
            with c2: st.markdown(f"""<div class="agent-card union-border delay-2"><div class="agent-name" style="color:#EF4444;">🤝 Union Leader</div><div class="agent-role">People's Voice</div><div class="agent-body">{result['union_opinion']}</div></div>""", unsafe_allow_html=True)
            with c3: st.markdown(f"""<div class="agent-card visionary-border delay-3"><div class="agent-name" style="color:#8B5CF6;">🚀 The Visionary</div><div class="agent-role">Future Architect</div><div class="agent-body">{result['visionary_opinion']}</div></div>""", unsafe_allow_html=True)
            
            # CEO
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"""<div class="agent-card ceo-border delay-4" style="text-align:center;"><div class="agent-name" style="color:#F59E0B;font-size:2.2rem;">👑 The CEO's Verdict</div><div class="agent-role" style="color:#F59E0B;">Final Binding Resolution</div><hr style="border-color:#F59E0B;opacity:0.2;width:50%;margin:20px auto;"><div class="agent-body" style="text-align:center;font-size:1.2rem;">{result['ceo_verdict']}</div></div>""", unsafe_allow_html=True)

            # ... (CEO Verdict card code is above here) ...

            # PDF Download Section with SAFETY NET
            st.markdown("<br>", unsafe_allow_html=True)
            
            try:
                pdf_bytes = create_pdf(topic, result['cfo_opinion'], result['union_opinion'], result['visionary_opinion'], result['ceo_verdict'])
                
                c1, c2, c3 = st.columns([1,1,1])
                with c2:
                    st.download_button(
                        label="⬇ Download Official Report (PDF)",
                        data=pdf_bytes,
                        file_name="Council_Report.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
            except UnicodeEncodeError:
                # This runs if the user typed in Hindi/Korean/etc.
                st.warning("⚠️ PDF Report is currently available in English only. (Multilingual support coming in V2).")
            except Exception as e:
                st.error(f"❌ PDF Generation Error: {e}")

        except Exception as e:
            st.error(f"❌ Error: {e}")
# ... (End of your script) ...

st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #6B7280; font-size: 0.8rem;'>
        &copy; 2026 <a href='https://www.linkedin.com/in/i-rohit-goswami/' target='_blank' style='color: #F59E0B; text-decoration: none;'>Rohit's AI Studio</a>. All Rights Reserved. <br>
        <i>Built with Llama 3 & LangGraph.</i>
    </div>
    """, 
    unsafe_allow_html=True
)