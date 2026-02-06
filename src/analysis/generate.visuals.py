import matplotlib.pyplot as plt 
import seaborn as sns
import os
from connection import get_db_data

def run_analysis():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, "../../"))
    target_folder = os.path.join(project_root, "visualisations")
    
    # Ensuring the folder exists!
    os.makedirs(target_folder, exist_ok=True)

    # --- Chart 1: Customer distribution by country ---
    print("Step 1: Fetching Geodata...")
    query_geo = """
        SELECT country, COUNT(*) AS nb_customers 
        FROM customers 
        GROUP BY country 
        ORDER BY nb_customers DESC;
    """
    df_geo = get_db_data(query_geo)

    print("Step 2: Generating Sales by Country chart...")
    plt.figure(figsize=(12, 8))
    sns.barplot(data=df_geo, x='nb_customers', y='country', hue='country', palette='viridis', legend=False)
    plt.title('Customer Distribution by Country', fontsize=15)
    plt.tight_layout()
    
    output_path = os.path.join(target_folder, "sales_by_country.png")
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"SUCCESS! Saved: {output_path}")

    # --- Chart 2: Top 10 Best Selling Products ---
    # NOTE: This is now INSIDE the function (indented)
    print("Step 3: Generating Top 10 Products chart...")
    query_products = """
        SELECT p.productName, SUM(od.quantityOrdered) AS total_quantity
        FROM orderdetails od
        JOIN products p ON od.productCode = p.productCode
        GROUP BY p.productName
        ORDER BY total_quantity DESC
        LIMIT 10;
    """
    df_prod = get_db_data(query_products)
    
    plt.figure(figsize=(12, 8))
    sns.barplot(data=df_prod, x='total_quantity', y='productName', hue='productName', palette='coolwarm', legend=False)
    plt.title('Top 10 Best Selling Products')
    plt.xlabel('Quantity Sold')
    plt.tight_layout()
    
    final_output = os.path.join(target_folder, "top_10_products.png")
    plt.savefig(final_output)
    plt.close()
    print(f"SUCCESS! Saved: {final_output}")

# The entry point that starts the function
if __name__ == "__main__":
    run_analysis()