import os
import json
from flask import Blueprint, render_template
from products.database import init_db, db_session
from products.models import Product


products_app = Blueprint("products_app", __name__,
                         template_folder="./templates",
                         static_folder="./static")

db_dir_path = os.path.join(os.path.dirname(__file__), 'database/')
db_path = os.path.join(db_dir_path, 'products.db')
json_path = os.path.join(db_dir_path, 'products.json')

try:
    if not os.path.exists(db_path):
        init_db()
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        for product in data["products"]:
            db_session.add(Product(
              product["author"], 
              product["name"], 
              product["price"], 
              product["description"], 
              product["image"]
            ))
        db_session.commit()
    else:
        init_db()
except Exception as e:
    print(e)


@products_app.route('/', methods=['GET'])
def all_products_page():
    products = Product.query.all()
    print(products)
    return render_template('products.html', products=products)


@products_app.route('/<int:product_id>/', methods=['GET'])
def current_product_page(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return render_template('404.html'), 404
    return render_template('product.html', product=product)
