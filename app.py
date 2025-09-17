rom flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from googletrans import Translator   # Google Translate

app = Flask(_name_)

# Twilio credentials
account_sid = "AC3544ea0e102c9990258eaabc801c03e0"
auth_token = "4c11dcc444ac491a6969e8854f18d12f"
twilio_whatsapp = "whatsapp:+14155238886"   # Twilio Sandbox number

client = Client(account_sid, auth_token)
translator = Translator()

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "")
    resp = MessagingResponse()
    msg = resp.message()

    # 🌐 Translate incoming message to English
    translated = translator.translate(incoming_msg, dest="en")
    text_en = translated.text.lower()

    # 🛠 Custom replies
    if "interview" in text_en:
        msg.body("📌 Interview details: We provide daily interview updates. Apply now!")
    elif "internship" in text_en:
        msg.body("🎓 Internship details: Latest internships are available. Visit our site!")
    elif "apply" in text_en:
        msg.body("✅ Application link: https://yourwebsite.com/apply")
    else:
        msg.body(f"🌍 You said: {incoming_msg}\n\n🔄 Translated: {text_en}")

    return str(resp)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
