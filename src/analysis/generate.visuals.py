import matplotlib.pyplot as plt 
import seaborn as sns
import os
from connection import get_db_data

def run_analysis():
    # 1. SETUP PATHS (This is where target_folder is born)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, "../../"))
    target_folder = os.path.join(project_root, "visualisations")
    os.makedirs(target_folder, exist_ok=True)

    # --- CHART 1: Distribution by Country ---
    print("Step 1: Generating Country Chart...")
    query_geo = "SELECT country, COUNT(*) AS nb_customers FROM customers GROUP BY country ORDER BY nb_customers DESC;"
    df_geo = get_db_data(query_geo)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_geo, x='nb_customers', y='country', hue='country', palette='viridis', legend=False)
    plt.savefig(os.path.join(target_folder, "sales_by_country.png"), bbox_inches='tight')
    plt.close()

    # --- CHART 2: Top 10 Products ---
    print("Step 2: Generating Top 10 Products Chart...")
    query_prod = """
        SELECT p.productName, SUM(od.quantityOrdered) AS total_quantity
        FROM orderdetails od
        JOIN products p ON od.productCode = p.productCode
        GROUP BY p.productName
        ORDER BY total_quantity DESC LIMIT 10;
    """
    df_prod = get_db_data(query_prod)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_prod, x='total_quantity', y='productName', hue='productName', palette='coolwarm', legend=False)
    plt.savefig(os.path.join(target_folder, "top_10_products.png"), bbox_inches='tight')
    plt.close()

    # --- CHART 3: Revenue by Product Line ---
    print("Step 3: Generating Product Line Chart...")
    query_line = """
        SELECT p.productLine, SUM(od.quantityOrdered * od.priceEach) AS total_revenue
        FROM orderdetails od
        JOIN products p ON od.productCode = p.productCode
        GROUP BY p.productLine
        ORDER BY total_revenue DESC;
    """
    df_line = get_db_data(query_line)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_line, x='total_revenue', y='productLine', hue='productLine', palette='rocket', legend=False)
    plt.savefig(os.path.join(target_folder, "revenue_by_product_line.png"), bbox_inches='tight')
    plt.close()

    print(f"SUCCESS! in: {target_folder}")


if __name__ == "__main__":
    run_analysis()