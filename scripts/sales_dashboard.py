import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (16, 10)

print("=" * 80)
print("SALES DATA ANALYSIS DASHBOARD")
print("=" * 80)

print("\n📥 Loading sales data...")
df = pd.read_csv('../data/raw/sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

print(f"✓ Loaded {len(df)} records")

print("\n📊 Calculating metrics...")

total_sales = df['Net_Amount'].sum()
total_transactions = len(df)
total_units = df['Quantity'].sum()
avg_transaction = df['Net_Amount'].mean()

df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('YearMonth')['Net_Amount'].sum()
sales_by_product = df.groupby('Product')['Net_Amount'].sum().sort_values(ascending=False)
sales_by_region = df.groupby('Region')['Net_Amount'].sum().sort_values(ascending=False)
sales_by_category = df.groupby('Category')['Net_Amount'].sum().sort_values(ascending=False)

print(f"\n{'─' * 80}")
print("KEY METRICS")
print(f"{'─' * 80}")
print(f"Total Revenue:          ₹{total_sales:,.2f}")
print(f"Total Transactions:     {total_transactions:,}")
print(f"Total Units Sold:       {total_units:,}")
print(f"Average Transaction:    ₹{avg_transaction:,.2f}")

print(f"\n{'─' * 80}")
print("TOP 5 PRODUCTS")
print(f"{'─' * 80}")
for product, amount in sales_by_product.head(5).items():
    print(f"{product:20} ₹{amount:>12,.2f}")

print(f"\n{'─' * 80}")
print("SALES BY REGION")
print(f"{'─' * 80}")
for region, amount in sales_by_region.items():
    pct = (amount/total_sales)*100
    print(f"{region:20} ₹{amount:>12,.2f}  ({pct:>5.1f}%)")

print("\n📈 Creating visualizations...")

fig = plt.figure(figsize=(16, 10))

# Chart 1: Monthly Sales
ax1 = plt.subplot(2, 3, 1)
monthly_sales.plot(ax=ax1, marker='o', color='#2E86AB', linewidth=2)
ax1.set_title('Monthly Sales Trend', fontweight='bold')
ax1.set_ylabel('Revenue (₹)')
ax1.grid(True, alpha=0.3)

# Chart 2: Top Products
ax2 = plt.subplot(2, 3, 2)
sales_by_product.head(8).plot(kind='barh', ax=ax2, color='#A23B72')
ax2.set_title('Top 8 Products by Revenue', fontweight='bold')
ax2.set_xlabel('Revenue (₹)')

# Chart 3: Sales by Region
ax3 = plt.subplot(2, 3, 3)
ax3.pie(sales_by_region.values, labels=sales_by_region.index, autopct='%1.1f%%', startangle=90)
ax3.set_title('Sales by Region', fontweight='bold')

# Chart 4: Sales by Category
ax4 = plt.subplot(2, 3, 4)
ax4.pie(sales_by_category.values, labels=sales_by_category.index, autopct='%1.1f%%', startangle=90)
ax4.set_title('Sales by Category', fontweight='bold')

# Chart 5: Quantity by Product
ax5 = plt.subplot(2, 3, 5)
qty = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(8)
qty.plot(kind='bar', ax=ax5, color='#06D6A0')
ax5.set_title('Quantity Sold by Product', fontweight='bold')
ax5.set_ylabel('Quantity')

# Chart 6: Average by Region
ax6 = plt.subplot(2, 3, 6)
avg = df.groupby('Region')['Net_Amount'].mean().sort_values(ascending=False)
avg.plot(kind='bar', ax=ax6, color='#9D4EDD')
ax6.set_title('Average Transaction by Region', fontweight='bold')
ax6.set_ylabel('Average (₹)')

plt.tight_layout()
plt.savefig('../results/sales_dashboard.png', dpi=300, bbox_inches='tight')
print("✓ Dashboard saved to ../results/sales_dashboard.png")
plt.show()

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE!")
print("=" * 80)