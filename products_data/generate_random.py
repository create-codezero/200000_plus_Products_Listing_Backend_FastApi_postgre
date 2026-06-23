import csv
import random
from datetime import datetime, timedelta
from uuid import uuid4

TOTAL_PRODUCTS = 220_000

BRANDS = [
    "Apple", "Samsung", "Sony", "LG", "Dell", "HP", "Lenovo",
    "Asus", "Acer", "Nike", "Adidas", "Puma", "Reebok",
    "Boat", "JBL", "OnePlus", "Xiaomi", "Realme", "Canon",
    "Nikon", "Philips", "Panasonic", "Zara", "H&M", "Levis",
    "Allen Solly", "UCB", "Woodland", "Titan", "Fossil"
]

CATEGORIES = {
    "Smartphones": (8000, 150000),
    "Laptops": (25000, 250000),
    "Tablets": (7000, 100000),
    "Smartwatches": (1000, 60000),
    "Headphones": (500, 30000),
    "Speakers": (700, 50000),
    "Cameras": (10000, 500000),
    "Televisions": (12000, 300000),
    "Monitors": (5000, 80000),
    "Printers": (3000, 50000),

    "T-Shirts": (199, 2999),
    "Shirts": (399, 4999),
    "Jeans": (699, 6999),
    "Trousers": (499, 5999),
    "Track Pants": (399, 3999),
    "Hoodies": (699, 5999),
    "Jackets": (999, 9999),
    "Sweatshirts": (599, 4999),
    "Ethnic Wear": (799, 9999),
    "Innerwear": (99, 1999),

    "Running Shoes": (799, 14999),
    "Sneakers": (999, 19999),
    "Sandals": (299, 4999),
    "Flip Flops": (99, 1499),
    "Formal Shoes": (999, 12999),

    "Books": (99, 2999),
    "Stationery": (49, 999),
    "Notebooks": (49, 499),
    "School Bags": (299, 4999),
    "Office Supplies": (99, 2999),

    "Kitchen Appliances": (499, 50000),
    "Cookware": (299, 15000),
    "Furniture": (999, 150000),
    "Home Decor": (199, 30000),
    "Lighting": (199, 20000),

    "Beauty": (99, 9999),
    "Skincare": (99, 9999),
    "Haircare": (99, 7999),
    "Perfumes": (299, 25000),
    "Makeup": (99, 15000),

    "Fitness Equipment": (499, 50000),
    "Sportswear": (299, 7999),
    "Cricket Gear": (299, 30000),
    "Football Gear": (199, 15000),
    "Cycling": (999, 150000),

    "Toys": (99, 9999),
    "Board Games": (199, 4999),
    "Baby Products": (99, 20000),
    "Pet Supplies": (99, 15000),
    "Groceries": (20, 5000),

    "Watches": (499, 100000),
    "Jewelry": (299, 300000),
    "Bags": (399, 25000),
    "Wallets": (199, 9999),
    "Sunglasses": (299, 25000),

    "Power Banks": (399, 7999),
    "Chargers": (149, 2999),
    "Computer Accessories": (99, 9999),
    "Gaming Accessories": (299, 30000),
    "Networking Devices": (999, 25000)
}

ADJECTIVES = [
    "Premium", "Classic", "Smart", "Ultra", "Pro",
    "Elite", "Advanced", "Portable", "Wireless",
    "Modern", "Stylish", "Comfort", "Lightweight",
    "Professional", "Designer", "Luxury", "Compact",
    "Eco", "Durable", "Performance"
]

COLORS = [
    "Black", "White", "Blue", "Red", "Green",
    "Silver", "Grey", "Gold", "Pink", "Brown"
]

CATEGORY_WEIGHTS = {
    "Smartphones": 8,
    "Laptops": 5,
    "T-Shirts": 10,
    "Shirts": 8,
    "Jeans": 8,
    "Running Shoes": 6,
    "Sneakers": 6,
    "Books": 5,
    "Beauty": 5,
    "Groceries": 4
}

# default weight
DEFAULT_WEIGHT = 2

weighted_categories = []

for cat in CATEGORIES:
    weight = CATEGORY_WEIGHTS.get(cat, DEFAULT_WEIGHT)
    weighted_categories.extend([cat] * weight)


def random_date():
    start = datetime.now() - timedelta(days=1095)

    created = start + timedelta(
        seconds=random.randint(
            0,
            int((datetime.now() - start).total_seconds())
        )
    )

    updated = created + timedelta(
        days=random.randint(0, 365)
    )

    if updated > datetime.now():
        updated = datetime.now()

    return created, updated


def generate_product():

    category = random.choice(weighted_categories)

    brand = random.choice(BRANDS)

    adjective = random.choice(ADJECTIVES)

    color = random.choice(COLORS)

    min_price, max_price = CATEGORIES[category]

    price = random.randint(min_price, max_price)

    created_at, updated_at = random_date()
    
    updated_at = updated_at.replace(
        second=0,
        microsecond=0
    )

    product_name = (
        f"{brand} {adjective} {color} {category}"
    )

    return {
        "public_id": str(uuid4()),
        "name": product_name,
        "brand": brand,
        "category": category,
        "price": price,
        "created_at": created_at.isoformat(),
        "updated_at": updated_at.isoformat()
    }


def main():

    output_file = "products.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:

        writer = csv.DictWriter(
            csvfile,
            fieldnames=[
                "public_id",
                "name",
                "brand",
                "category",
                "price",
                "created_at",
                "updated_at"
            ]
        )

        writer.writeheader()

        for i in range(TOTAL_PRODUCTS):

            writer.writerow(generate_product())

            if i % 10000 == 0:
                print(f"Generated {i:,} products")

    print(f"\nDone. Generated {TOTAL_PRODUCTS:,} products.")


if __name__ == "__main__":
    main()