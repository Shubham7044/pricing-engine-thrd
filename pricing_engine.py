import pandas as pd
from tabulate import tabulate

# Step 1: Read input CSVs
products_df = pd.read_csv('products.csv')
sales_df = pd.read_csv('sales.csv')

# Step 2: Merge data on 'sku'
merged_df = pd.merge(products_df, sales_df, on='sku', how='left')
merged_df['quantity_sold'].fillna(0, inplace=True)

# Step 3: Apply pricing rules
updated_prices = []

for index, row in merged_df.iterrows():
    sku = row['sku']
    current_price = row['current_price']
    cost_price = row['cost_price']
    stock = row['stock']
    quantity_sold = row['quantity_sold']

    new_price = current_price  # default

    # Rule 1 – Low Stock, High Demand
    if stock < 20 and quantity_sold > 30:
        new_price = current_price * 1.15

    # Rule 2 – Dead Stock
    elif stock > 200 and quantity_sold == 0:
        new_price = current_price * 0.70

    # Rule 3 – Overstocked Inventory
    elif stock > 100 and quantity_sold < 20:
        new_price = current_price * 0.90

    # Rule 4 – Minimum Profit Constraint
    min_price = cost_price * 1.20
    if new_price < min_price:
        new_price = min_price

    # Final Rounding
    new_price = round(new_price, 2)
    old_price_with_unit = f"{current_price:.2f} INR"
    new_price_with_unit = f"{new_price:.2f} INR"

    updated_prices.append({
        'sku': sku,
        'old_price': old_price_with_unit,
        'new_price': new_price_with_unit
    })

# Step 4: Create DataFrame
final_df = pd.DataFrame(updated_prices)

# Step 5: Save box-style output as text into CSV file
box_output = tabulate(final_df, headers='keys', tablefmt='fancy_grid')

with open('updated_prices.csv', 'w', encoding='utf-8') as f:
    f.write("📦 Final Updated Product Prices:\n\n")
    f.write(box_output)

# Optional: Also save as actual CSV for data processing if needed
final_df.to_csv('updated_prices_data.csv', index=False)

# Step 6: Print to terminal
print("\n📦 Final Updated Product Prices:\n")
print(box_output)
