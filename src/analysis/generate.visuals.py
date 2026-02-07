import matplotlib.pyplot as plt 
import seaborn as sns
import os
import pandas as pd
from connection import get_db_data

def run_analysis():
    # 1. SETUP BASE PATHS
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, "../../"))
    viz_folder = os.path.join(project_root, "visualisations")
    os.makedirs(viz_folder, exist_ok=True)

    # Vis 1: Country Distribution
    print("Generating Chart 1 (Geography)...")
    q1 = "SELECT country, COUNT(*) AS nb FROM customers GROUP BY country ORDER BY nb DESC;"
    df1 = get_db_data(q1)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df1, x='nb', y='country', hue='country', palette='viridis', legend=False)
    plt.title('Customer Distribution by Country')
    plt.savefig(os.path.join(viz_folder, "sales_by_country.png"), bbox_inches='tight')
    plt.close()

    # Vis 2: Top 10 Products 
    print("Generating Chart 2 (Top Products)...")
    q2 = """
        SELECT p.productName, SUM(od.quantityOrdered) AS qty 
        FROM orderdetails od 
        JOIN products p ON od.productCode = p.productCode 
        GROUP BY p.productName 
        ORDER BY qty DESC LIMIT 10;
    """
    df2 = get_db_data(q2)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df2, x='qty', y='productName', hue='productName', palette='coolwarm', legend=False)
    plt.title('Top 10 Best Selling Products')
    plt.savefig(os.path.join(viz_folder, "top_10_products.png"), bbox_inches='tight')
    plt.close()

    # Vis 3: Revenue by Line 
    print("Generating Chart 3 (Product Lines)...")
    q3 = """
        SELECT p.productLine, SUM(od.quantityOrdered * od.priceEach) AS rev 
        FROM orderdetails od 
        JOIN products p ON od.productCode = p.productCode 
        GROUP BY p.productLine ORDER BY rev DESC;
    """
    df3 = get_db_data(q3)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df3, x='rev', y='productLine', hue='productLine', palette='rocket', legend=False)
    plt.title('Revenue by Product Line')
    plt.savefig(os.path.join(viz_folder, "revenue_by_product_line.png"), bbox_inches='tight')
    plt.close()

    # Vis 4: Low Stock (Inventory Analysis)
    print("Generating Chart 4 (Low Stock)...")
    q4 = "SELECT productName, quantityInStock FROM products WHERE quantityInStock < 1000 ORDER BY quantityInStock ASC;"
    df4 = get_db_data(q4)
    if not df4.empty:
        plt.figure(figsize=(10, 6))
        sns.barplot(data=df4, x='quantityInStock', y='productName', hue='productName', palette='autumn', legend=False)
        plt.title('Critical Stock Levels (<1000 units)')
        plt.savefig(os.path.join(viz_folder, "low_stock_inventory.png"), bbox_inches='tight')
        plt.close()

    # Vis 5: Sales Evolution 
    print("Generating Chart 5 (Time Series)...")
    q5 = """
        SELECT DATE_FORMAT(orderDate, '%Y-%m') AS month, SUM(quantityOrdered * priceEach) AS monthly_sales
        FROM orders o
        JOIN orderdetails od ON o.orderNumber = od.orderNumber
        GROUP BY month
        ORDER BY month;
    """
    df5 = get_db_data(q5)
    plt.figure(figsize=(12, 6))
    plt.plot(df5['month'], df5['monthly_sales'], marker='o', linestyle='-', color='b')
    plt.xticks(rotation=45)
    plt.title('Monthly Sales Evolution')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(os.path.join(viz_folder, "sales_evolution.png"))
    plt.close()

    # Vis 6: Correlation 
    print("Generating Chart 6 (Correlation Heatmap)...")
    q6 = "SELECT quantityOrdered, priceEach, (quantityOrdered * priceEach) AS total_val FROM orderdetails;"
    df6 = get_db_data(q6)
    plt.figure(figsize=(8, 6))
    sns.heatmap(df6.corr(), annot=True, cmap='YlGnBu', fmt=".2f")
    plt.title('Correlation Matrix: Quantity vs Price')
    plt.savefig(os.path.join(viz_folder, "correlation_heatmap.png"), bbox_inches='tight')
    plt.close()

    # Vis 7: Revenue Distribution (Top Clients vs Others) 
    print("Generating Chart 7 (Revenue Distribution)...")
    q7 = """
        SELECT c.customerName, SUM(od.quantityOrdered * od.priceEach) AS total_spent
        FROM customers c
        JOIN orders o ON c.customerNumber = o.customerNumber
        JOIN orderdetails od ON o.orderNumber = od.orderNumber
        GROUP BY c.customerName
        ORDER BY total_spent DESC;
    """
    df7 = get_db_data(q7)
    top_10 = df7.head(10).copy()
    others_value = df7.iloc[10:]['total_spent'].sum()
    others_df = pd.DataFrame([{'customerName': 'Others', 'total_spent': others_value}])
    plot_data = pd.concat([top_10, others_df], ignore_index=True)

    plt.figure(figsize=(10, 8))
    plt.pie(plot_data['total_spent'], labels=plot_data['customerName'], autopct='%1.1f%%', startangle=140)
    plt.title('Revenue Distribution: Top 10 Clients vs Others')
    plt.savefig(os.path.join(viz_folder, "revenue_distribution.png"), bbox_inches='tight')
    plt.close()

    # Vis 8: Order Status Distribution
    print("Generating Chart 8 (Order Status)...")
    q8 = "SELECT status, COUNT(*) AS count FROM orders GROUP BY status;"
    df8 = get_db_data(q8)
    plt.figure(figsize=(8, 8))
    plt.pie(df8['count'], labels=df8['status'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Order Status Distribution')
    plt.savefig(os.path.join(viz_folder, "order_status_distribution.png"), bbox_inches='tight')
    plt.close()

    print(f"DONE! All 8 visuals saved in: {viz_folder}")

if __name__ == "__main__":
    run_analysis()