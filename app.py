from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY


def get_db_connection():
    """Create and return a new DB connection."""
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )
    return connection


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        address = request.form.get("address")
        password = request.form.get("password")
        school = request.form.get("school")

        # Simple validation
        if not username or not address or not password or not school:
            flash("All fields are required!", "error")
            return redirect(url_for("index"))

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            insert_query = """
                INSERT INTO users (username, address, password, school)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (username, address, password, school))
            conn.commit()

            cursor.close()
            conn.close()

            flash("Details saved successfully!", "success")
            return redirect(url_for("index"))

        except Error as e:
            print("Error while connecting to MySQL:", e)
            flash("Error saving to database!", "error")
            return redirect(url_for("index"))

    # GET request
    # Also fetch all users to display below the form (optional)
    users = []
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, username, address, school FROM users ORDER BY id DESC")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
    except Error as e:
        print("Error fetching users:", e)

    return render_template("index.html", users=users)


if __name__ == "__main__":
    # For local testing (in Docker, you will use gunicorn or this with host=0.0.0.0)
    app.run(host="0.0.0.0", port=5000, debug=True)
