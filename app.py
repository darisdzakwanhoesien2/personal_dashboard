import streamlit as st
import requests
import time

st.set_page_config(page_title="Webhook Trigger Dashboard", layout="centered")
st.title("🚀 Webhook Trigger Dashboard")

# -------------------------------------------------
# Webhook endpoints
# -------------------------------------------------
webhooks = {
    "Generate All (Test All Models)": "https://n8n-tsilhjwcawfn.tomat.sumopod.my.id/webhook/generate-all_test-all_models",
    "Generate All (Test All Models 2)": "https://n8n-tsilhjwcawfn.tomat.sumopod.my.id/webhook/generate-all_test-all_models_2",
    "Random Trigger": "https://n8n-tsilhjwcawfn.tomat.sumopod.my.id/webhook/fxsdfsdfds",
}

# -------------------------------------------------
# Session state for stop control
# -------------------------------------------------
if "stop_run" not in st.session_state:
    st.session_state.stop_run = False

# -------------------------------------------------
# Controls
# -------------------------------------------------
st.subheader("⚙️ Batch Execution Settings")

col1, col2 = st.columns(2)

with col1:
    repeat_n = st.number_input(
        "Number of executions",
        min_value=1,
        max_value=10000,
        value=250,
        step=1
    )

with col2:
    delay_s = st.number_input(
        "Delay between requests (seconds)",
        min_value=0.0,
        max_value=60.0,
        value=3.0,
        step=0.5
    )

selected_label = st.selectbox(
    "Select webhook to trigger",
    list(webhooks.keys())
)

selected_url = webhooks[selected_label]

# -------------------------------------------------
# Action buttons
# -------------------------------------------------
st.subheader("▶️ Execute")

colA, colB = st.columns(2)

with colA:
    start_btn = st.button("▶️ Start Batch Execution")

with colB:
    stop_btn = st.button("⛔ Stop")

if stop_btn:
    st.session_state.stop_run = True
    st.warning("Stopping after current request...")

# -------------------------------------------------
# Batch execution logic
# -------------------------------------------------
if start_btn:
    st.session_state.stop_run = False

    st.info(
        f"Triggering **{selected_label}**\n\n"
        f"• Repetitions: {repeat_n}\n"
        f"• Delay: {delay_s} seconds"
    )

    progress = st.progress(0)
    log_box = st.empty()

    success = 0
    failed = 0

    for i in range(1, repeat_n + 1):

        if st.session_state.stop_run:
            log_box.warning(f"⛔ Stopped at execution {i-1}")
            break

        try:
            r = requests.get(selected_url, timeout=15)

            if r.status_code == 200:
                success += 1
                msg = f"✅ {i}/{repeat_n} | Status {r.status_code}"
            else:
                failed += 1
                msg = f"⚠️ {i}/{repeat_n} | Status {r.status_code}"

        except Exception as e:
            failed += 1
            msg = f"❌ {i}/{repeat_n} | Error: {e}"

        log_box.write(msg)
        progress.progress(i / repeat_n)

        if i < repeat_n:
            time.sleep(delay_s)

    st.success("Batch execution finished.")
    st.write(f"✅ Success: {success}")
    st.write(f"❌ Failed: {failed}")

# -------------------------------------------------
# Single-click manual triggers (original feature)
# -------------------------------------------------
st.divider()
st.subheader("⚡ Quick Single Trigger")

for label, url in webhooks.items():
    if st.button(label, key=f"single_{label}"):
        st.write(f"🔄 Sending GET request to: {url}")

        try:
            response = requests.get(url, timeout=10)
            st.success(f"Status: {response.status_code}")
            st.code(response.text[:3000])

        except Exception as e:
            st.error(f"Error: {e}")
