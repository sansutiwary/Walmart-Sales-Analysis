# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S72G94j_d6RwinsVmC4gZWV256_iEnmW
"""

import pandas as pd

import numpy as np

import pandas as pd
df = pd.read_excel('Walmart Sales (1).xlsx')

total_sales_by_city = df.groupby('City')['Unit price'].sum()

total_revenue_by_city = df.groupby('City')['Revenue'].sum()
print("Total sales by city:")
print(total_sales_by_city)

print("\nTotal revenue by city:")
print(total_revenue_by_city)

top_selling_city = total_sales_by_city.sort_values(ascending=False).index[0]


bottom_selling_city = total_sales_by_city.sort_values().index[0]


top_revenue_city = total_revenue_by_city.sort_values(ascending=False).index[0]


bottom_revenue_city = total_revenue_by_city.sort_values().index[0]

print("Top performing city based on sales:", top_selling_city)
print("Bottom performing city based on sales:", bottom_selling_city)
print("Top performing city based on revenue:", top_revenue_city)
print("Bottom performing city based on revenue:", bottom_revenue_city)

average_sales_by_branch = df.groupby('Branch')['Unit price'].mean()
average_revenue_by_branch = df.groupby('Branch')['Revenue'].mean()

print("\nAverage sales by branch:")
print(average_sales_by_branch)

print("\nAverage revenue by branch:")
print(average_revenue_by_branch)

top_selling_branch_by_city = {}
bottom_selling_branch_by_city = {}
for city in df['City'].unique():
  city_df = df[df['City'] == city]
  top_selling_branch_by_city[city] = city_df.groupby('Branch')['Unit price'].sum().sort_values(ascending=False).index[0]
  bottom_selling_branch_by_city[city] = city_df.groupby('Branch')['Unit price'].sum().sort_values().index[0]


top_revenue_branch_by_city = {}
bottom_revenue_branch_by_city = {}
for city in df['City'].unique():
  city_df = df[df['City'] == city]
  top_revenue_branch_by_city[city] = city_df.groupby('Branch')['Revenue'].sum().sort_values(ascending=False).index[0]
  bottom_revenue_branch_by_city[city] = city_df.groupby('Branch')['Revenue'].sum().sort_values().index[0]


top_selling_branch_overall = df.groupby('Branch')['Unit price'].sum().sort_values(ascending=False).index[0]
bottom_selling_branch_overall = df.groupby('Branch')['Unit price'].sum().sort_values().index[0]


top_revenue_branch_overall = df.groupby('Branch')['Revenue'].sum().sort_values(ascending=False).index[0]
bottom_revenue_branch_overall = df.groupby('Branch')['Revenue'].sum().sort_values().index[0]


print("Top performing branches by city (sales):")
print(top_selling_branch_by_city)

print("\nBottom performing branches by city (sales):")
print(bottom_selling_branch_by_city)

print("\nTop performing branches by city (revenue):")
print(top_revenue_branch_by_city)

print("\nBottom performing branches by city (revenue):")
print(bottom_revenue_branch_by_city)

print("\nTop performing branch overall (sales):")
print(top_selling_branch_overall)

print("\nBottom performing branch overall (sales):")
print(bottom_selling_branch_overall)

print("\nTop performing branch overall (revenue):")
print(top_revenue_branch_overall)

print("\nBottom performing branch overall (revenue):")
print(bottom_revenue_branch_overall)

city_performance = df.groupby('City')['Revenue'].mean()
branch_performance = df.groupby('Branch')['Revenue'].mean()

correlation_location = city_performance.corr(branch_performance)

print("Correlation between city performance and branch performance:", correlation_location)

import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))
total_sales_by_city.plot(kind='bar')
plt.title('Total Sales by City')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.show()


plt.figure(figsize=(10, 6))
total_revenue_by_city.plot(kind='pie', autopct='%1.1f%%')
plt.title('Total Revenue by City')
plt.show()


plt.figure(figsize=(10, 6))
average_sales_by_branch.plot(kind='bar')
plt.title('Average Sales by Branch')
plt.xlabel('Branch')
plt.ylabel('Average Sales')
plt.show()


plt.figure(figsize=(10, 6))
average_revenue_by_branch.plot(kind='pie', autopct='%1.1f%%')
plt.title('Average Revenue by Branch')
plt.show()

average_price_by_branch = df.groupby('Branch')['Revenue'].sum() / df.groupby('Branch')['Quantity'].sum()

print("\nAverage price per item by branch:")
print(average_price_by_branch)

average_price_by_city = df.groupby('City')['Revenue'].sum() / df.groupby('City')['Quantity'].sum()
print(average_price_by_city)


price_difference = average_price_by_branch - average_price_by_city
print(price_difference)


high_price_branches = price_difference[price_difference > average_price_by_branch.std()].index.tolist()
print(high_price_branches)


low_price_branches = price_difference[price_difference < -average_price_by_branch.std()].index.tolist()


print("\nBranches with significantly higher average prices:")
print(high_price_branches)

print("\nBranches with significantly lower average prices:")
print(low_price_branches)

average_price_by_branch_category = df.groupby(['Branch', 'Product line'])['Revenue'].sum() / df.groupby(['Branch', 'Product line'])['Quantity'].sum()


high_price_categories = {}
for branch, category_prices in average_price_by_branch_category.groupby('Branch'):
  high_price_categories[branch] = category_prices[category_prices > category_prices.mean() + category_prices.std()].index.tolist()


print("\nProduct categories with significantly higher average prices in each branch:")
print(high_price_categories)


product_mix_high_price_branches = {}
for branch in high_price_branches:
  branch_data = df[df['Branch'] == branch]
  product_mix_high_price_branches[branch] = branch_data.groupby('Product line')['Revenue'].sum() / branch_data['Revenue'].sum()


print("\nProduct mix of high-price branches:")
print(product_mix_high_price_branches)


overall_product_mix = df.groupby('Product line')['Revenue'].sum() / df['Revenue'].sum()
print("\nOverall product mix:")
print(overall_product_mix)

#Month-over-Month Sales & Revenue Analysis

sales_mom_growth_product_line = df.groupby(['Month', 'Product line'])['Unit price'].sum().pct_change() * 100


revenue_mom_growth_product_line = df.groupby(['Month', 'Product line'])['Revenue'].sum().pct_change() * 100


sales_mom_growth_gender = df.groupby(['Month', 'Gender'])['Unit price'].sum().pct_change() * 100


revenue_mom_growth_gender = df.groupby(['Month', 'Gender'])['Revenue'].sum().pct_change() * 100


sales_mom_growth_payment_method = df.groupby(['Month', 'Payment'])['Unit price'].sum().pct_change() * 100


revenue_mom_growth_payment_method = df.groupby(['Month', 'Payment'])['Revenue'].sum().pct_change() * 100


print("MoM Sales Growth by Product Line:")
print(sales_mom_growth_product_line)

print("\nMoM Revenue Growth by Product Line:")
print(revenue_mom_growth_product_line)

print("\nMoM Sales Growth by Gender:")
print(sales_mom_growth_gender)

print("\nMoM Revenue Growth by Gender:")
print(revenue_mom_growth_gender)

print("\nMoM Sales Growth by Payment Method:")
print(sales_mom_growth_payment_method)

print("\nMoM Revenue Growth by Payment Method:")
print(revenue_mom_growth_payment_method)

# Identify categories with significant positive or negative growth

significant_sales_growth_categories = sales_mom_growth_product_line[
  (sales_mom_growth_product_line > sales_mom_growth_product_line.mean() + sales_mom_growth_product_line.std()) |
  (sales_mom_growth_product_line < sales_mom_growth_product_line.mean() - sales_mom_growth_product_line.std())
]


significant_revenue_growth_categories = revenue_mom_growth_product_line[
  (revenue_mom_growth_product_line > revenue_mom_growth_product_line.mean() + revenue_mom_growth_product_line.std()) |
  (revenue_mom_growth_product_line < revenue_mom_growth_product_line.mean() - revenue_mom_growth_product_line.std())
]


print("\nCategories with significant positive or negative growth in sales:")
print(significant_sales_growth_categories)

print("\nCategories with significant positive or negative growth in revenue:")
print(significant_revenue_growth_categories)

declining_sales_categories = sales_mom_growth_product_line[sales_mom_growth_product_line < 0]


declining_sales_genders = sales_mom_growth_gender[sales_mom_growth_gender < 0]


declining_sales_payment_methods = sales_mom_growth_payment_method[sales_mom_growth_payment_method < 0]


print("\nProduct lines with declining sales:")
print(declining_sales_categories)

print("\nGenders with declining sales:")
print(declining_sales_genders)

print("\nPayment methods with declining sales:")
print(declining_sales_payment_methods)



high_growth_categories = sales_mom_growth_product_line[sales_mom_growth_product_line > sales_mom_growth_product_line.mean()]

print("\nCategories with high growth potential:")
print(high_growth_categories)

import pandas as pd
import matplotlib.pyplot as plt

long_term_sales_mom_growth_product_line = df.groupby(['Month', 'Product line'])['Unit price'].sum().pct_change(periods=12) * 100


long_term_revenue_mom_growth_product_line = df.groupby(['Month', 'Product line'])['Revenue'].sum().pct_change(periods=12) * 100


consistently_high_growth_categories = long_term_sales_mom_growth_product_line[long_term_sales_mom_growth_product_line > long_term_sales_mom_growth_product_line.mean()]
consistently_low_growth_categories = long_term_sales_mom_growth_product_line[long_term_sales_mom_growth_product_line < long_term_sales_mom_growth_product_line.mean()]


plt.figure(figsize=(10, 6))
long_term_sales_mom_growth_product_line.unstack().plot(title='Long-Term MoM Sales Growth by Product Line')
plt.xlabel('Month')
plt.ylabel('MoM Growth (%)')
plt.show()


average_monthly_growth = df.groupby('Month')['Unit price'].sum().pct_change() * 100
average_monthly_growth = average_monthly_growth.reset_index()


long_term_sales_mom_growth_product_line = df.groupby(['Month', 'Product line'])['Unit price'].sum().pct_change(periods=6) * 100


long_term_revenue_mom_growth_product_line = df.groupby(['Month', 'Product line'])['Revenue'].sum().pct_change(periods=6) * 100
average_monthly_growth = average_monthly_growth.set_index('Month')


plt.figure(figsize=(10, 6))
average_monthly_growth.plot(title='Average Monthly Sales Growth')
plt.xlabel('Month')
plt.ylabel('Average MoM Growth (%)')
plt.show()