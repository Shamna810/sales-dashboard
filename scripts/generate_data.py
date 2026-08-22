import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

print("=" * 70)
print("GENERATING SAMPLE SALES DATA")
print("=" * 70)

start_date = datetime.now() - timedelta(days=730)
end_date = datetime.now()
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

products = ['Laptop', 'Mobile Phone', 'Tablet', 'Headphones', 'Monitor', 
            'Keyboard', 'Mouse', 'USB Drive', 'Speaker', 'Webcam']
regions = ['North', 'South', 'East', 'West', 'Central']

data = []
for date in date_range:
    num_transactions = np.random.randint(2, 6)
    
    for _ in range(num_transactions):
        product = random.choice(products)
        region = random.choice(regions)
        quantity = np.random.randint(1, 10)
        
        prices = {
            'Laptop': np.random.uniform(40000, 100000),
            'Mobile Phone': np.random.uniform(20000, 80000),
            'Tablet': np.random.uniform(15000, 50000),
            'Headphones': np.random.uniform(1000, 10000),
            'Monitor': np.random.uniform(10000, 40000),
            'Keyboard': np.random.uniform(1500, 8000),
            'Mouse': np.random.uniform(500, 3000),
            'USB Drive': np.random.uniform(500, 2000),
            'Speaker': np.random.uniform(2000, 15000),
            'Webcam': np.random.uniform(2000, 8000)
        }
        
        price = prices[product]
        total = quantity * price
        
        if product in ['Laptop', 'Mobile Phone', 'Tablet', 'Monitor']:
            category = 'Electronics'
        elif product in ['Headphones', 'Speaker', 'Webcam']:
            category = 'Accessories'
        else:
            category = 'Peripherals'
        
        data.append({
            'Date': date,
            'Product': product,
            'Category': category,
            'Region': region,
            'Quantity': quantity,
            'Unit_Price': price,
            'Total_Amount': total,
            'Discount': np.random.uniform(0, 0.15) * total
        })

df = pd.DataFrame(data)
df['Net_Amount'] = df['Total_Amount'] - df['Discount']
df.to_csv('../data/raw/sales_data.csv', index=False)

print(f"\n✓ Generated {len(df)} sales records")
print(f"✓ Date range: {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"✓ Data saved to: ../data/raw/sales_data.csv")
print("=" * 70)