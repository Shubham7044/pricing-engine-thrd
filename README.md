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
📂 Project Structure
Copy
Edit
pricing_engine_project/
├── products.csv
├── sales.csv
├── updated_prices.csv
├── updated_prices_data.txt
├── pricing_engine.py
└── README.md
🧠 Approach
The script uses pandas for efficient data handling and tabulate for clean tabular formatting in the .txt output.

🔁 Pricing Rules (Applied in Priority)
Rule 1 – Low Stock, High Demand

stock < 20 and quantity_sold > 30 → Increase price by 15%

Rule 2 – Dead Stock

stock > 200 and quantity_sold == 0 → Decrease price by 30%

Rule 3 – Overstocked Inventory

stock > 100 and quantity_sold < 20 → Decrease price by 10%

Rule 4 – Minimum Profit Enforcement

Ensure price ≥ cost_price * 1.2 (minimum 20% margin)

✅ Only the first matching rule (1–3) is applied. Rule 4 is always applied.

📊 Input Files
products.csv – Product data: SKU, name, current price, cost, stock

sales.csv – SKU-wise quantity sold in the last 30 days

📤 Output Files
updated_prices.csv
➤ Columns: sku, old_price (INR), new_price (INR)
➤ Includes prices with INR units and 2 decimal places.

updated_prices_data.txt
➤ Nicely formatted human-readable table using tabulate.

💻 How to Run the Project
1. 🔧 Set Up Python Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
2. 📦 Install Required Libraries
bash
Copy
Edit
pip install pandas tabulate
3. 🚀 Run the Script
Make sure products.csv and sales.csv are in the same folder as pricing_engine.py.

bash
Copy
Edit
python pricing_engine.py
📁 Sample Output (updated_prices.csv)

sku	old_price (INR)	new_price (INR)
A123	649.99 INR	600.00 INR
B456	699.00 INR	803.85 INR
C789	999.00 INR	699.30 INR
✅ Prices are rounded to 2 decimal places and include INR as unit.

✅ Assumptions
If a SKU in products.csv is not found in sales.csv, quantity_sold is assumed to be 0.

All monetary values are handled in INR and suffixed appropriately in output.

Price adjustments follow the first applicable rule only, except Rule 4 which is always enforced.

Script is robust to handle large product catalogs via vectorized pandas operations.

🛠️ Example: SKU A123
Current price: 649.99

Stock: 150, Sales: 10

Rule 3 applies (overstocked) → 649.99 × 0.9 = 584.99

Minimum profit: 500 × 1.2 = 600.00

Final price: 600.00 INR



---

## 👨‍💻 Author

**Shubham Swarnakar**  
Final Year B.Tech CSE (AI & ML)  
*Making data work for better pricing decisions.*

