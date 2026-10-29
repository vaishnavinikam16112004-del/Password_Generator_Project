from flask import Flask, render_template, request
from password_generator import generate_password

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    password = None
    error = None

    if request.method == "POST":
        try:
            length = int(request.form.get("length", ""))
        except ValueError:
            length = 0

        use_lower = request.form.get("lower") == "on"
        use_upper = request.form.get("upper") == "on"
        use_digits = request.form.get("digits") == "on"
        use_symbols = request.form.get("symbols") == "on"
        selected_count = sum([use_lower, use_upper, use_digits, use_symbols])

        if length < 1:
            error = "Enter a password length greater than 0."
        elif length > 1024:
            error = "Choose a length of 1024 or less."
        elif selected_count == 0:
            error = "Select at least one character type."
        elif length < selected_count:
            error = "Length must be at least the number of selected types."
        else:
            password = generate_password(
                length, use_lower, use_upper, use_digits, use_symbols
            )

    return render_template("index.html", password=password, error=error)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)