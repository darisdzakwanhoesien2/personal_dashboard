https://chatgpt.com/c/69344fbc-ea7c-8333-960f-825a70d71ffes personal_dashboard
https://chatgpt.com/c/695e2ec4-ac5c-832a-8324-2831b41589f6

Yes — we can add:

* ✅ number of executions (e.g., 250)
* ✅ delay between calls (e.g., 3 seconds)
* ✅ progress bar
* ✅ live log output
* ✅ stop button (safe interrupt using `st.session_state`)

Below is a **complete improved Streamlit app** that keeps your original buttons and adds batch execution controls.

---

## ✅ Improved Streamlit Webhook Trigger Dashboard

```python
```

---

## ⚠️ Important Notes (for your use case)

Since you mentioned **250 executions with 3s delay**:

* Total runtime ≈ **12.5 minutes**
* Streamlit will **block the UI during the loop**
* If the page refreshes → the run stops

If you later want:

* ✅ background execution
* ✅ parallel requests
* ✅ job queue
* ✅ persistent logs

Then we should move this into:

* FastAPI + Celery / RQ worker
* or n8n loop node
* and Streamlit only becomes a controller UI

---

## 🚀 Possible Next Upgrades (I can help with these)

If useful for your n8n testing pipelines:

* 🔁 Parallel execution (10 requests at once)
* 📊 Success rate charts
* 📝 Save logs to CSV
* ⏱️ Average response time tracking
* 🔐 Auth headers & POST payload support

If you tell me what exactly you’re stress-testing in n8n (model load? DB? RAG?), I can tailor this into a proper load-testing mini dashboard for you.
