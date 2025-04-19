# 📦 Pricing Engine – Smart Dynamic Pricing Based on Inventory and Sales

This project is a **dynamic pricing engine built with Python** that automatically adjusts product prices based on two key factors:

✅ Current inventory levels  
✅ Recent sales performance  

The goal is to optimize pricing dynamically to reflect real-world supply and demand, while ensuring that each product maintains a **minimum profit margin of 20%** over its cost. This pricing engine helps businesses make **data-driven pricing decisions**, improve revenue, and reduce dead stock or overstock situations.

---

## 📊 What This Project Does

- Reads data from two CSV files: `products.csv` and `sales.csv`
- Applies pricing rules to determine a new price per product
- Guarantees a minimum **20% profit margin**
- Outputs two result files:
  - `updated_prices.csv` (box-style formatted using `tabulate`)
  - `updated_prices_data.csv` (plain CSV for data usage or visualization)
- Optionally used Tableau for product performance visualizations

---

## 📁 Project Structure

pricing_engine_project/ ├── products.csv ├── sales.csv ├── updated_prices.csv ├── updated_prices_data.csv ├── pricing_engine.py └── README.md

yaml
Copy
Edit

---

## 🧠 Approach

The engine reads product and sales data using **pandas**. For each product, it applies a set of **prioritized pricing rules**, and always applies a minimum profit margin rule before writing the results to a new CSV file.

---

## 🔁 Pricing Rules (Applied in Order of Priority)

1. **Rule 1 – Low Stock, High Demand**  
   📌 Condition: `stock < 20` and `quantity_sold > 30`  
   🔧 Action: Increase price by **15%**

2. **Rule 2 – Dead Stock**  
   📌 Condition: `stock > 200` and `quantity_sold == 0`  
   🔧 Action: Decrease price by **30%**

3. **Rule 3 – Overstocked Inventory**  
   📌 Condition: `stock > 100` and `quantity_sold < 20`  
   🔧 Action: Decrease price by **10%**

4. **Rule 4 – Minimum Profit Constraint**  
   📌 Condition: Ensure final price is **at least 20% above `cost_price`**  
   🔧 Action: If below, reset to `cost_price * 1.2`

✅ Only the **first applicable rule (1–3)** is applied, followed by **Rule 4** in every case.  
✍️ Final price is always **rounded to 2 decimal places**.

---

## 📥 Input Files

- **`products.csv`** – Product catalog including `sku`, `name`, `current_price`, `cost_price`, and `stock`
- **`sales.csv`** – Last 30 days of sales data per `sku`

---

## 📤 Output Files

- **`updated_prices.csv`**  
  - Columns: `sku`, `old_price (INR)`, `new_price (INR)`
  - Formatted with box style using the `tabulate` package
  - Includes appropriate currency unit (`INR`) and two-decimal precision

- **`updated_prices_data.csv`** *(Optional)*  
  - Plain CSV version with extended internal calculations for visualization or analysis

---

## 💻 How to Run

### 🔧 Step 1: Set Up Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\\Scripts\\activate
📦 Step 2: Install Dependencies
bash
Copy
Edit
pip install pandas tabulate
🚀 Step 3: Run the Script
bash
Copy
Edit
python pricing_engine.py
Make sure products.csv and sales.csv are in the same directory as the script.

✅ Sample Output (updated_prices.csv)

sku	old_price (INR)	new_price (INR)
A123	649.99 INR	600.00 INR
B456	699.00 INR	803.85 INR
C789	999.00 INR	699.30 INR
📌 Assumptions
Products missing in sales.csv are assumed to have quantity_sold = 0

Only one rule among Rule 1, 2, or 3 is applied per product

All products are guaranteed to have at least a 20% margin over cost

Prices are always rounded to 2 decimal places

Script scales to large datasets efficiently using pandas

🛠️ Example Calculation (SKU: A123)
current_price = 649.99

stock = 150, quantity_sold = 10

✅ Rule 3 applies → 649.99 × 0.9 = 584.99

🔒 Minimum margin check: 500 × 1.2 = 600.00

✅ Final price = 600.00 INR

👨‍💻 Author
Shubham Swarnakar
🎓 Final Year B.Tech CSE (AI & ML)
📌 Making data work for better pricing decisions
