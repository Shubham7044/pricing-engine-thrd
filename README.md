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

## 🔧 Project Structure

```
pricing-engine/
├── pricing_engine.py              # Main Python script
├── products.csv                   # Product data
├── sales.csv                      # Sales data
├── updated_prices.csv             # Formatted price updates
├── updated_prices_data.csv        # Raw data with new prices
└── README.md                      # Project documentation
```

---

## 🐍 Set Up Python Virtual Environment

Using a virtual environment is recommended.

### Step-by-Step:

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install pandas tabulate
```

---

## ▶️ How to Run the Script

1. Make sure you have Python 3.x installed
2. Place `products.csv` and `sales.csv` in the same folder as the script
3. Then run the following command:

```bash
python pricing_engine.py
```

---

## 📁 Output Files

| File Name                | Description                                       |
|-------------------------|---------------------------------------------------|
| `updated_prices.csv`    | Box-styled readable format for review             |
| `updated_prices_data.csv` | Clean CSV version for data processing or Tableau |

---

## 📈 Tableau Insights

Visualized inventory vs. sales and price adjustment trends using Tableau:
- Which products are overstocked or underperforming?
- Pricing sensitivity across SKUs
- Ideal margins for future pricing

---

## 👨‍💻 Author

**Shubham Swarnakar**  
Final Year B.Tech CSE (AI & ML)  
*Making data work for better pricing decisions.*

