# 📦 Pricing Engine – Smart Dynamic Pricing Based on Inventory and Sales

This project is a dynamic pricing engine built with Python that automatically adjusts product prices based on two key factors:

✅ Current inventory levels

✅ Recent sales performance

The goal is to optimize pricing dynamically to reflect real-world supply and demand, while ensuring that each product maintains a minimum profit margin of 20% over its cost. This pricing engine helps businesses make data-driven pricing decisions, improve revenue, and reduce dead stock or overstock situations.

---

## 📊 What This Project Does

- Reads data from two CSV files: `products.csv` and `sales.csv`
- Applies pricing rules to determine a new price per product
- Guarantees a minimum 20% profit margin on each product
- Outputs two result files:
  - `updated_prices.csv` (box-style formatted)
  - `updated_prices_data.csv` (plain CSV for data use or visualization)
- Used **Tableau** for product performance visualizations

---
pricing_engine_project/ ├── products.csv ├── sales.csv ├── updated_prices.csv ├── updated_prices_data.csv ├── pricing_engine.py └── README.md

markdown
Copy code

---

## 🧠 Approach

The engine reads product and sales data from CSV files using `pandas`. For each product, it applies a set of prioritized pricing rules and ensures a minimum profit margin before writing the results back to a new CSV file.

### 🔁 Pricing Rules (Applied in Order of Priority)

1. **Rule 1 – Low Stock, High Demand**
   - **Condition:** `stock < 20` and `quantity_sold > 30`
   - **Action:** Increase price by **15%**

2. **Rule 2 – Dead Stock**
   - **Condition:** `stock > 200` and `quantity_sold == 0`
   - **Action:** Decrease price by **30%**

3. **Rule 3 – Overstocked Inventory**
   - **Condition:** `stock > 100` and `quantity_sold < 20`
   - **Action:** Decrease price by **10%**

4. **Rule 4 – Minimum Profit Constraint**
   - **Condition:** Ensure final price is at least 20% above `cost_price`
   - **Action:** If below, reset to `cost_price * 1.2`

✅ Only the **first applicable rule (1–3)** is applied, followed by **Rule 4** in every case. Final price is **rounded to 2 decimal places**.

---

## 📥 Input Files

- `products.csv`: Product catalog including `sku`, `name`, `current_price`, `cost_price`, and `stock`
- `sales.csv`: Last 30 days of sales performance for each SKU

---

## 📤 Output Files

1. **`updated_prices.csv`**
   - Contains `sku`, `old_price (INR)`, `new_price (INR)`
   - Includes appropriate units (`INR`) and 2 decimal precision

2. **`updated_prices_data.csv`**
   - (Optional) Contains extended data with intermediary calculations

---

## 💻 How to Run

### 🔧 Step 1: Set Up Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\\Scripts\\activate
📦 Step 2: Install Dependencies
bash
Copy code
pip install pandas tabulate
🚀 Step 3: Run the Script
bash
Copy code
python pricing_engine.py
Ensure products.csv and sales.csv are in the same directory as the script.

✅ Sample Output (updated_prices.csv)
sku	old_price (INR)	new_price (INR)
A123	649.99 INR	600.00 INR
B456	699.00 INR	803.85 INR
C789	999.00 INR	699.30 INR
📌 Assumptions
If a product is missing in sales.csv, it's assumed to have quantity_sold = 0

Prices are adjusted only using the first applicable rule

The output enforces a minimum 20% profit margin above cost

Prices include currency unit (INR) and are rounded to 2 decimal places

Script can scale to large product lists using efficient pandas operations

🛠️ Example Calculation (SKU: A123)
current_price = 649.99

stock = 150, quantity_sold = 10

Rule 3 applies (overstocked) → 649.99 × 0.9 = 584.99

Minimum margin check: 500 × 1.2 = 600.00

✅ Final price = 600.00 INR
---

## 👨‍💻 Author

**Shubham Swarnakar**  
Final Year B.Tech CSE (AI & ML)  
*Making data work for better pricing decisions.*

