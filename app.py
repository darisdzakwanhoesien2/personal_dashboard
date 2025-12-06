import streamlit as st
import requests

st.title("Webhook Trigger Dashboard")

# --- List of your webhook endpoints ---
webhooks = {
    "Generate All (Test All Models)": "https://n8n-tsilhjwcawfn.tomat.sumopod.my.id/webhook/generate-all_test-all_models",
    "Generate All (Test All Models 2)": "https://n8n-tsilhjwcawfn.tomat.sumopod.my.id/webhook/generate-all_test-all_models_2",
    "Random Trigger": "https://n8n-tsilhjwcawfn.tomat.sumopod.my.id/webhook/fxsdfsdfds",
}

st.subheader("Click a button to trigger a webhook")

for label, url in webhooks.items():

    if st.button(label):
        st.write(f"🔄 Sending GET request to: {url}")

        try:
            response = requests.get(url, timeout=10)

            st.success(f"Status: {response.status_code}")
            st.code(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
