from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Flask Validator is live."

@app.route('/validate', methods=['POST'])
def validate_script():
    data = request.get_json()
    script = data.get("script", "")

    banned_phrases = [
        "a recent study", "in the ever-evolving world of", "dynamic", "fast-changing",
        "ultimate", "comprehensive", "enhance", "uncover", "realm", "imagine a world where",
        "let’s dive into", "let’s delve into", "delve", "when it comes to"
    ]

    word_count = len(script.split())
    lower_script = script.lower()

    for phrase in banned_phrases:
        if phrase in lower_script:
            return jsonify({
                "status": "invalid",
                "word_count": word_count
            })

    if word_count <= 1000:
        return jsonify({
            "status": "invalid",
            "word_count": word_count
        })

    return jsonify({
        "status": "valid",
        "word_count": word_count
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
