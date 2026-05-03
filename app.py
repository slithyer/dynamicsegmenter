from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
history = []

try:
    model = pickle.load(open("mirasol_dynamic_model.pkl", "rb"))
    scaler = pickle.load(open("mirasol_scaler.pkl", "rb"))
except Exception as e:
    print(f"File Error: {e}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    try:
        age = float(data['age'])
        income = float(data['income'])
        kids = float(data['kids'])
        teens = float(data['teens'])
        recency = float(data['recency'])
        spending = float(data['spending'])

        # LAYER 1: Hard Rules
        if age < 18:
            result = "🚫 REJECTED: UNDERAGE"
        elif income < 15000:
            result = "🚫 REJECTED: LOW INCOME"
        
        # LAYER 2: High Net Worth Override (The "Billionaire" Logic)
        elif income >= 500000:
            result = "💎 QUALIFIED: VIP ELITE"

        # LAYER 3: Machine Learning Analysis
        else:
            user_features = np.array([[income, kids, teens, recency, spending, age]])
            scaled_features = scaler.transform(user_features)
            cluster_id = model.predict(scaled_features)[0]

            status_map = {
                0: "✅ QUALIFIED: VIP ELITE",
                1: "✅ QUALIFIED: STANDARD VIP",
                2: "❌ UNFIT: BUDGET SEGMENT",
                3: "❌ UNFIT: LOW ENGAGEMENT"
            }
            result = status_map.get(cluster_id, "PENDING REVIEW")

    except:
        result = "⚠️ DATA ERROR"

    history.append({
        "name": data['name'],
        "email": data['email'],
        "personality": result,
        "income": income,
        "spending": spending
    })
    return jsonify({"status": "success"})

@app.route("/history")
def history_page():
    return render_template("history.html", history=history)

if __name__ == "__main__":
    app.run(debug=True)