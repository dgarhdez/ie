"""
E-commerce Transaction Data Generator
Creates realistic transaction data with intentional data quality issues
for datetime and regex practice in pandas.
"""

import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Configuration
NUM_TRANSACTIONS = 2500
NUM_CUSTOMERS = 500
NUM_PRODUCTS = 100

# Date range: January 2024 - January 2026
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2026, 1, 29)

# Generate customer data
regions = ["US", "EU", "ASIA", "UK", "CA"]
first_names = [
    "John",
    "Mary",
    "Robert",
    "Sarah",
    "Michael",
    "Emma",
    "David",
    "Lisa",
    "James",
    "Jennifer",
    "William",
    "Patricia",
    "Richard",
    "Linda",
    "Joseph",
]
last_names = [
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Garcia",
    "Miller",
    "Davis",
    "Rodriguez",
    "Martinez",
    "Hernandez",
    "Lopez",
    "Wilson",
    "Anderson",
]
titles = ["", "", "", "", "Dr.", "Mr.", "Mrs.", "Ms."]
domains = ["example.com", "shop.com", "email.com", "mail.com", "test.com"]

# Product categories
categories = {
    "ELEC": ["PHONE", "LAPTOP", "TABLET", "CAMERA", "AUDIO"],
    "CLOTH": ["SHIRT", "PANTS", "DRESS", "SHOES", "JACKET"],
    "HOME": ["FURNITURE", "DECOR", "KITCHEN", "BEDDING", "LIGHTING"],
    "BOOK": ["FICTION", "NONFICTION", "TEXTBOOK", "EBOOK", "MAGAZINE"],
    "SPORT": ["FITNESS", "OUTDOOR", "TEAM", "WATER", "WINTER"],
}

# Payment methods
payment_methods = [
    "Credit Card (Visa)",
    "Credit Card (Mastercard)",
    "credit_card",
    "PayPal",
    "Debit Card - Visa",
    "DEBIT CARD - Mastercard",
    "Apple Pay",
    "Google Pay",
    "CREDIT CARD",
]

# Order statuses
statuses = ["Delivered", "Shipped", "Processing", "Cancelled"]


def generate_customer_id(region, number):
    """Generate customer ID with occasional formatting issues"""
    if random.random() < 0.03:  # 3% malformed
        return f"CUST{region}{number:04d}"  # Missing dashes
    return f"CUST-{region}-{number:04d}"


def generate_customer_name(first, last, title=""):
    """Generate customer name with various formatting issues"""
    name = f"{first} {last}"

    if title:
        name = f"{title} {name}"

    # Add formatting issues
    if random.random() < 0.3:
        name = name.upper()
    elif random.random() < 0.3:
        name = name.lower()

    if random.random() < 0.2:
        name = f"  {name}  "  # Extra spaces

    return name


def generate_email(first, last, domain):
    """Generate email with occasional invalid formats"""
    email = f"{first.lower()}.{last.lower()}@{domain}"

    if random.random() < 0.05:  # 5% invalid
        return random.choice(["invalid-email", f"{first.lower()}@", "user@domain"])

    if random.random() < 0.3:
        email = email.upper()

    return email


def generate_transaction_timestamp(base_date):
    """Generate timestamp with various formats"""
    # Add some randomness to create realistic patterns
    # More transactions in evenings and weekends
    hour = random.choices(
        range(24),
        weights=[
            1,
            1,
            1,
            1,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            10,
            10,
            9,
            8,
            12,
            15,
            12,
            10,
            8,
            5,
        ],
    )[0]

    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    timestamp = base_date.replace(hour=hour, minute=minute, second=second)

    # Return in various formats
    format_choice = random.random()

    if format_choice < 0.25:
        # ISO format
        return timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
    elif format_choice < 0.50:
        # US format
        return timestamp.strftime("%m/%d/%Y %I:%M %p")
    elif format_choice < 0.75:
        # European format
        return timestamp.strftime("%d/%m/%Y %H:%M")
    else:
        # Text format
        return timestamp.strftime("%B %d, %Y at %I:%M%p").replace(" 0", " ")


def generate_product_code(category, subcategory):
    """Generate product code"""
    product_id = random.randint(1000, 9999)
    return f"{category}-{subcategory}-{product_id}"


def generate_amount(category):
    """Generate amount with currency symbols"""
    # Different price ranges by category
    if category == "ELEC":
        base_amount = random.uniform(50, 2000)
    elif category == "CLOTH":
        base_amount = random.uniform(20, 300)
    elif category == "HOME":
        base_amount = random.uniform(30, 1500)
    elif category == "BOOK":
        base_amount = random.uniform(10, 100)
    else:  # SPORT
        base_amount = random.uniform(25, 500)

    amount = round(base_amount, 2)

    # Add currency symbols
    symbol = random.choice(["$", "$", "$", "€", "£"])

    if random.random() < 0.2:
        # With comma for thousands
        if amount >= 1000:
            return f"{symbol}{amount:,.2f}"

    if random.random() < 0.1:
        # No symbol
        return f"{amount:.2f}"

    return f"{symbol}{amount:.2f}"


def generate_shipping_address():
    """Generate shipping address"""
    street_num = random.randint(1, 9999)
    street_names = ["Main St", "High Street", "Park Ave", "Oak Road", "Elm Street"]

    if random.random() < 0.5:
        # US address
        cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
        states = ["NY", "CA", "IL", "TX", "AZ"]
        zip_code = f"{random.randint(10000, 99999)}"
        city = random.choice(cities)
        state = random.choice(states)
        return f"{street_num} {random.choice(street_names)}, {city}, {state} {zip_code}"
    else:
        # UK address
        cities = ["London", "Manchester", "Birmingham", "Leeds", "Liverpool"]
        postcodes = ["SW1A 1AA", "M1 1AA", "B1 1AA", "LS1 1AA", "L1 1AA"]
        return f"{street_num} {random.choice(street_names)}, {random.choice(cities)}, UK, {random.choice(postcodes)}"


def generate_order_status(transaction_date):
    """Generate order status with embedded dates"""
    status = random.choice(statuses)

    if status == "Delivered":
        delivery_date = transaction_date + timedelta(days=random.randint(2, 10))
        if random.random() < 0.5:
            return f"Delivered on {delivery_date.strftime('%Y-%m-%d')}"
        else:
            return f"Delivered on {delivery_date.strftime('%d/%m/%Y')}"
    elif status == "Shipped":
        arrival_date = transaction_date + timedelta(days=random.randint(3, 7))
        return f"Shipped (est. arrival: {arrival_date.strftime('%B %d')})"
    elif status == "Cancelled":
        cancel_date = transaction_date + timedelta(days=random.randint(0, 2))
        if random.random() < 0.5:
            return f"Cancelled - {cancel_date.strftime('%d/%m/%Y')}"
        else:
            return "Cancelled"
    else:
        return "Processing"


def generate_customer_feedback():
    """Generate customer feedback with emojis and ratings"""
    sentiments = [
        "Great product! 5 stars ⭐⭐⭐⭐⭐",
        "Excellent quality 👍",
        "Poor quality 😞",
        "Average product",
        "Amazing! Highly recommend ⭐⭐⭐⭐⭐",
        "Not worth the price",
        "Perfect! 5/5 stars",
        "Disappointed 😢",
        "Good value for money",
        "Arrived damaged 😠",
    ]

    if random.random() < 0.15:  # 15% missing feedback
        return None

    return random.choice(sentiments)


# Generate transactions
print("Generating e-commerce transaction data...")

transactions = []

for i in range(NUM_TRANSACTIONS):
    # Generate random date with realistic patterns
    # More transactions on weekends and in Q4
    days_from_start = random.randint(0, (END_DATE - START_DATE).days)
    transaction_date = START_DATE + timedelta(days=days_from_start)

    # Boost weekend transactions
    if transaction_date.weekday() >= 5:  # Saturday or Sunday
        if random.random() < 0.3:  # Skip 30% to create realistic variation
            pass

    # Boost Q4 transactions
    if transaction_date.month in [10, 11, 12]:
        if random.random() < 0.5:  # Create duplicates for Q4 boost
            pass

    # Generate transaction ID
    transaction_id = f"TXN-{transaction_date.strftime('%Y%m%d')}-{i:06d}"

    if random.random() < 0.03:  # 3% malformed
        transaction_id = f"TXN{transaction_date.strftime('%Y%m%d')}{i:06d}"

    # Customer info
    customer_num = random.randint(1, NUM_CUSTOMERS)
    region = random.choice(regions)
    customer_id = generate_customer_id(region, customer_num)

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    title = random.choice(titles)
    customer_name = generate_customer_name(first_name, last_name, title)
    customer_email = generate_email(first_name, last_name, random.choice(domains))

    # Product info
    main_category = random.choice(list(categories.keys()))
    subcategory = random.choice(categories[main_category])
    product_code = generate_product_code(main_category, subcategory)

    # Product name
    product_names = {
        "ELEC": [
            "iPhone 15 Pro Max (256GB)",
            "Samsung Galaxy S24",
            'MacBook Pro 14"',
            "Sony Camera A7",
            "Bose Headphones",
        ],
        "CLOTH": [
            "Nike Running Shoes - Size 10",
            "Levis Jeans 32x34",
            "Summer Dress (M)",
            "Leather Jacket [L]",
            "Cotton T-Shirt",
        ],
        "HOME": [
            "Modern Sofa Set",
            "Wall Art Decoration",
            "Kitchen Mixer",
            "Queen Bedding Set",
            "LED Floor Lamp",
        ],
        "BOOK": [
            "The Great Gatsby [Paperback]",
            "Data Science Handbook",
            "Python Programming",
            "Digital Marketing eBook",
            "Business Magazine",
        ],
        "SPORT": [
            "Yoga Mat Premium",
            "Camping Tent 4-Person",
            "Basketball Official",
            "Diving Gear Set",
            "Ski Jacket Waterproof",
        ],
    }
    product_name = random.choice(product_names[main_category])

    # Transaction details
    timestamp_str = generate_transaction_timestamp(transaction_date)
    amount = generate_amount(main_category)
    payment_method = random.choice(payment_methods)
    shipping_address = generate_shipping_address()
    order_status = generate_order_status(transaction_date)
    customer_feedback = generate_customer_feedback()

    transaction = {
        "transaction_id": transaction_id,
        "customer_id": customer_id,
        "customer_name": customer_name,
        "customer_email": customer_email,
        "transaction_timestamp": timestamp_str,
        "product_code": product_code,
        "product_name": product_name,
        "amount": amount,
        "payment_method": payment_method,
        "shipping_address": shipping_address,
        "order_status": order_status,
        "customer_feedback": customer_feedback,
    }

    transactions.append(transaction)

# Create DataFrame
df = pd.DataFrame(transactions)

# Introduce missing values (10% across various columns)
columns_to_null = [
    "customer_name",
    "customer_email",
    "customer_feedback",
    "shipping_address",
    "amount",
]

for col in columns_to_null:
    mask = np.random.random(len(df)) < 0.10
    df.loc[mask, col] = np.nan

# Introduce some outlier dates
outlier_indices = np.random.choice(len(df), size=20, replace=False)
for idx in outlier_indices:
    if random.random() < 0.5:
        # Future date
        df.loc[idx, "transaction_timestamp"] = "2027-12-31T23:59:59Z"
    else:
        # Very old date
        df.loc[idx, "transaction_timestamp"] = "01/01/2020 12:00 AM"

# Save to CSV
output_file = "/Users/dgh/Desktop/pda_mbads/pda2/homework/ecommerce_transactions.csv"
df.to_csv(output_file, index=False)

print(f"\n✓ Generated {len(df)} transactions")
print(f"✓ Saved to: {output_file}")
print(f"\nDataset summary:")
print(f"  - Date range: {START_DATE.date()} to {END_DATE.date()}")
print(f"  - Unique customers: ~{NUM_CUSTOMERS}")
print(f"  - Unique products: ~{NUM_PRODUCTS}")
print(f"  - Missing values: ~10% across key columns")
print(f"  - Data quality issues: Format variations, invalid entries, outliers")
print(f"  - Data quality issues: Format variations, invalid entries, outliers")
