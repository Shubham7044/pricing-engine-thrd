# 📦 Pricing Engine – Smart Dynamic Pricing Based on Inventory and Sales

This project is a dynamic pricing engine built with Python that automatically adjusts product prices based on two key factors:

✅ **Current inventory levels**  
✅ **Recent sales performance**

The goal is to optimize pricing dynamically to reflect real-world supply and demand, while ensuring that each product maintains a minimum profit margin of 20% over its cost. This pricing engine helps businesses make data-driven pricing decisions, improve revenue, and reduce dead stock or overstock situations.

---

## 📊 What This Project Does

- Reads data from two CSV files: `products.csv` and `sales.csv`
- Applies pricing rules to determine a new price per product
- Guarantees a minimum 20% profit margin on each product
- Outputs two result files:
  - `updated_prices.csv` – formatted output (includes units)
  - `updated_prices_data.csv` – raw CSV data (suitable for visualization/analysis)
- Visualizations (e.g. Tableau) can be created from the output file

---

## 📁 Project Structure

pricing-engine/
├── pricing_engine.py           # Main Python script
├── products.csv                # Product data
├── sales.csv                   # Sales data
├── updated_prices.csv          # Formatted price updates
├── updated_prices_data.csv     # Raw data with new prices
└── README.md                   # Project documentation

---

## 🧠 Approach

The engine reads product and sales data from CSV files using `pandas`. For each product, it applies a set of prioritized pricing rules and ensures a minimum profit margin before writing the results back to new output files.

---

## 🔁 Pricing Rules (Applied in Order of Priority)

### Rule 1 – Low Stock, High Demand (Highest Priority)
- **Condition:** `stock < 20` and `quantity_sold > 30`
- **Action:** Increase the price by **15%**

### Rule 2 – Dead Stock
- **Condition:** `stock > 200` and `quantity_sold == 0`
- **Action:** Decrease the price by **30%**

### Rule 3 – Overstocked Inventory
- **Condition:** `stock > 100` and `quantity_sold < 20`
- **Action:** Decrease the price by **10%**

### Rule 4 – Minimum Profit Constraint (Always Applied)
- **Condition:** Final price must be at least **20% above `cost_price`**
- **Action:** If below, reset price to `cost_price * 1.2`
- **Note:** Final price is always rounded to **2 decimal places**

> ✅ Only the first applicable rule among Rule 1–3 is applied. Rule 4 is always applied.

---

## 📥 Input Files

- `products.csv`: Product catalog including `sku`, `name`, `current_price`, `cost_price`, and `stock`
- `sales.csv`: Last 30 days of sales performance for each SKU (`sku`, `quantity_sold`)

---

## 📤 Output Files

### ✅ `updated_prices.csv`
- Contains `sku`, `old_price (INR)`, `new_price (INR)`
- Prices include units and are rounded to 2 decimal places

### 📊 `updated_prices_data.csv` (Optional)
- Contains extended output for analysis/visualization

---

## 💻 How to Run

### 🔧 Step 1: Set Up Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
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
📂 Make sure products.csv and sales.csv are in the same directory as the script.

✅ Sample Output (updated_prices.csv)

sku	old_price (INR)	new_price (INR)
A123	649.99 INR	600.00 INR
B456	699.00 INR	803.85 INR
C789	999.00 INR	699.30 INR
📌 Assumptions
If a product is missing in sales.csv, it's assumed to have quantity_sold = 0

Only the first applicable rule (1–3) is applied to each product

All outputs ensure at least 20% margin over cost

Currency is INR and precision is 2 decimal places

Scalable using efficient pandas operations

🛠️ Example Calculation (SKU: A123)
current_price = 649.99

cost_price = 500

stock = 150

quantity_sold = 10

Rule 3 applies (overstocked):
→ 649.99 × 0.9 = 584.99
Minimum margin check: 500 × 1.2 = 600.00
✅ Final price = 600.00 INR

👨‍💻 Author
Shubham Swarnakar
Final Year B.Tech CSE (AI & ML)
Making data work for better pricing decisions.
