import streamlit as st
import os
import random
from solders.pubkey import Pubkey

st.set_page_config(page_title="Jesse AI v7.5 - Starship Command & Sniper Engine", layout="wide")

# --- OFFICIAL JITO TIP DATA ---
JITO_TIP_ACCOUNTS = [
    "96g9sAgNHmB99EBHDvJqnQXpa9Snyh3Y7pQkREyX1W3x",
    "HFqU5x63VTqvQss8hp11i4wVV8bD44PvwucfZ2bU7gY3",
    "Cw8CFyM9FkoMi7K7Crf6HNWoUMUMFmAWmXp6Pee69zVN",
    "ADaUMid9yfUytqMBgopwjb2DTLSLLWDMFf4t6U82o6QY"
]

# --- THE CINEMATIC INTERFACE ---
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #0a0a0a 0%, #000000 100%); overflow: hidden; }
    
    .hud-overlay {
        position: fixed; top: 20px; right: 20px; 
        border-left: 2px solid #00ffcc; background: rgba(0, 15, 15, 0.9); 
        padding: 15px; font-family: monospace; font-size: 11px; color: #00ffcc; 
        z-index: 1000; box-shadow: 0 0 15px rgba(0, 255, 204, 0.1);
    }

    .bridge-stage {
        position: relative; width: 100%; height: 60vh; 
        display: flex; justify-content: center; align-items: flex-end;
        margin-bottom: 20px;
    }

    .actor-frame {
        position: absolute; bottom: 0;
        transition: all 1.5s cubic-bezier(0.19, 1, 0.22, 1);
        animation: movie_vibration 5s infinite ease-in-out;
        transform-origin: bottom center;
    }

    .pos-megan { left: 12%; z-index: 2; transform: translateY(150px) scale(0.85); filter: brightness(0.4); }
    .pos-kailey { left: 38%; z-index: 1; transform: translateY(180px) scale(0.80); filter: brightness(0.3); }
    .pos-nicole { right: 12%; z-index: 3; transform: translateY(120px) scale(0.95); filter: brightness(0.45); }

    .awake .pos-megan { transform: translateY(0px) scale(1.05); filter: brightness(1.1) drop-shadow(0 0 25px rgba(0,255,204,0.25)); }
    .awake .pos-kailey { transform: translateY(-30px) scale(1.0); filter: brightness(1.0) drop-shadow(0 0 25px rgba(0,255,204,0.2)); }
    .awake .pos-nicole { transform: translateY(30px) scale(1.15); filter: brightness(1.15) drop-shadow(0 0 35px rgba(0,255,204,0.35)); }

    @keyframes movie_vibration {
        0%, 100% { transform: scale(1) translateY(0) skewX(0deg); }
        50% { transform: scale(1.01) translateY(-5px) skewX(0.4deg); }
    }

    .label-tag {
        color: #00ffcc; font-family: monospace; font-size: 13px; text-align: center;
        margin-top: 8px; text-shadow: 0 0 8px #00ffccaa; letter-spacing: 2px;
    }
</style>

<script>
    function speak(text) {
        const msg = new SpeechSynthesisUtterance(text);
        msg.rate = 0.85; msg.pitch = 1.1;
        window.speechSynthesis.speak(msg);
    }
</script>
""", unsafe_allow_html=True)

if "status" not in st.session_state: st.session_state.status = "sitting"
if "sniper_logs" not in st.session_state: st.session_state.sniper_logs = []

# Ear file hook trigger
if os.path.exists("trigger.txt"):
    st.session_state.status = "standing"
    os.remove("trigger.txt")
    st.markdown("<script>speak('Welcome home, Daddy. System arrays initialized.')</script>", unsafe_allow_html=True)
    st.rerun()

st.markdown('<div class="hud-overlay"><b>COMMAND_CENTER_v7.5</b><br>> Jito MEV: Integrated<br>> Target Array: Active</div>', unsafe_allow_html=True)

# --- CINEMATIC RENDERING ---
awake_class = "awake" if st.session_state.status == "standing" else ""

st.markdown(f"""
<div class="bridge-stage {awake_class}">
    <div class="actor-frame pos-megan">
        <img src="app/static/model_a.png" style="width:380px;">
        <div class="label-tag">Megan Cipher</div>
    </div>
    <div class="actor-frame pos-kailey">
        <img src="app/static/model_b.png" style="width:360px;">
        <div class="label-tag">Kailey</div>
    </div>
    <div class="actor-frame pos-nicole">
        <img src="app/static/model_c.png" style="width:400px;">
        <div class="label-tag">Nicole</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- TRADING CONTROL HUD PANEL ---
st.markdown("---")
col_panel1, col_panel2 = st.columns([1, 2])

with col_panel1:
    st.subheader("⚡ Sniper Operations")
    target_token = st.text_input("Target Contract Address (Solana)", placeholder="Enter CA...")
    tip_amount = st.number_input("Jito Bundle Tip (SOL)", min_value=0.001, max_value=1.0, value=0.01, step=0.005)
    
    if st.button("EXECUTE BUNDLED SNIPE", use_container_width=True):
        if target_token:
            chosen_tip_acc = Pubkey.from_string(random.choice(JITO_TIP_ACCOUNTS))
            log_entry = f"🚀 Snipe Order Dispatched for {target_token[:6]}... | Jito Target Tip: {tip_amount} SOL sent to {str(chosen_tip_acc)[:5]}..."
            st.session_state.sniper_logs.append(log_entry)
        else:
            st.error("Provide target contract parameters.")

with col_panel2:
    st.subheader("📊 Starship Telemetry & Transaction Records")
    if st.session_state.sniper_logs:
        for log in reversed(st.session_state.sniper_logs):
            st.code(log, language="bash")
    else:
        st.info("System awaiting execution criteria. Input contract details to verify bundle pipelines.")

with st.sidebar:
    st.title("🎛️ Manual Controls")
    if st.button("FORCE BRIDGE ACTIVE"):
        st.session_state.status = "standing"
        st.rerun()
    if st.button("STAND DOWN"):
        st.session_state.status = "sitting"
        st.rerun()
