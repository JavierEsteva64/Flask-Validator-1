from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Flask app is running"

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
                "word_count": word_count,
                "reason": f"Banned phrase detected: '{phrase}'"
            })

    if word_count < 1150:
        return jsonify({
            "status": "invalid",
            "word_count": word_count,
            "reason": "Script too short"
        })

    paragraphs = script.strip().split("\n\n")
    hook = paragraphs[0] if len(paragraphs) > 0 else ""
    cta = paragraphs[-1] if len(paragraphs) > 1 else ""

    return jsonify({
        "status": "valid",
        "word_count": word_count,
        "hook": hook.strip(),
        "cta": cta.strip()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
