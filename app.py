import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from custom_refinement import refine_query, generate_comparison_table
from serp_api import search_products

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Render the homepage with the search form."""
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    """Process the search query submitted by the user."""
    user_input = request.form["query"]
    location = request.form.get("location", "India")
    
    refined_query_response = refine_query(user_input, location)
    refined_query = f"{refined_query_response['refined_query']} {refined_query_response['additional_info']}".strip()

    products = search_products(refined_query, location=location)
    if not products:
        return render_template("index.html", error="No products found for your query.")

    comparison_table, summary = generate_comparison_table(products)
    return render_template("index.html", refined_query=refined_query, comparison_table=comparison_table, summary=summary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
