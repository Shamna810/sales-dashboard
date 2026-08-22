import sys
sys.path.insert(0, '..')

import pandas as pd
import numpy as np

# Test 1: Check if data loads correctly
def test_load_data():
    df = pd.read_csv('../data/raw/sales_data.csv')
    assert len(df) > 0, "Data should not be empty"
    assert 'Net_Amount' in df.columns, "Net_Amount column missing"
    print("✅ Test 1 passed: Data loaded correctly")

# Test 2: Check if revenue calculation works
def test_calculate_revenue():
    df = pd.read_csv('../data/raw/sales_data.csv')
    total_revenue = df['Net_Amount'].sum()
    assert total_revenue > 0, "Revenue should be positive"
    print(f"✅ Test 2 passed: Total revenue = ₹{total_revenue:,.2f}")

# Test 3: Check if product data exists
def test_products_exist():
    df = pd.read_csv('../data/raw/sales_data.csv')
    products = df['Product'].unique()
    assert len(products) > 0, "No products found"
    print(f"✅ Test 3 passed: Found {len(products)} unique products")

# Test 4: Check regions
def test_regions_exist():
    df = pd.read_csv('../data/raw/sales_data.csv')
    regions = df['Region'].unique()
    assert len(regions) == 5, "Should have 5 regions"
    print(f"✅ Test 4 passed: Found {len(regions)} regions")

# Run all tests
if __name__ == "__main__":
    print("=" * 50)
    print("Running Unit Tests")
    print("=" * 50)
    
    try:
        test_load_data()
        test_calculate_revenue()
        test_products_exist()
        test_regions_exist()
        
        print("\n" + "=" * 50)
        print("✅ ALL TESTS PASSED!")
        print("=" * 50)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")