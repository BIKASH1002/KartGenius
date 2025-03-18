import pandas as pd

def refine_query(user_input, location):
    """
    Mock refinement of user input.
    """
    refined_query = user_input.lower().strip()
    additional_info = "best deals in the market"
    return {"refined_query": refined_query, "additional_info": additional_info}

def generate_comparison_table(products):
    """
    Generate a comparison table and summary for products.
    Tries to parse rating/reviews from direct keys or 'extensions' if needed.
    """
    product_summaries = []

    for p in products[:10]:
        name_html = f"<a href='{p.get('link', '#')}' target='_blank'>{p.get('title', 'N/A')}</a>"

        rating = p.get("rating", None)
        reviews = p.get("reviews", None)
        extensions = p.get("extensions", [])
        if not rating:
            for ext in extensions:
                if "star rating" in ext.lower():
                    try:
                        rating_str = ext.split(" ")[0]
                        rating = float(rating_str)
                        break
                    except:
                        rating = ext
        if not reviews:
            for ext in extensions:
                if "reviews" in ext.lower():
                    ext_clean = ext.replace("+", "")
                    try:
                        reviews_str = ext_clean.split(" ")[0]
                        reviews = int(reviews_str)
                        break
                    except:
                        reviews = ext_clean

        rating_str = f"{rating} ⭐" if rating else "N/A"
        reviews_str = f"{reviews} Reviews" if reviews else "N/A"

        if p.get("thumbnail"):
            image_html = f"<img src='{p.get('thumbnail')}' alt='Product Image' width='100'>"
        else:
            image_html = "N/A"

        actions_html = (
            f"<button class='fav-button' data-title=\"{p.get('title', 'N/A')}\" "
            f"data-link=\"{p.get('link', '#')}\">Add to Favourites</button>"
        )

        product_summaries.append({
            "Image": image_html,
            "Name": name_html,
            "Price": p.get("price", "N/A"),
            "Rating": rating_str,
            "Reviews": reviews_str,
            "Actions": actions_html
        })

    comparison_df = pd.DataFrame(product_summaries)
    comparison_df = comparison_df[["Image", "Name", "Price", "Rating", "Reviews", "Actions"]]
    comparison_table_html = comparison_df.to_html(index=False, escape=False)

    summary = "<h3>Comparison Summary</h3><p>Based on available product data.</p>"
    return comparison_table_html, summary
