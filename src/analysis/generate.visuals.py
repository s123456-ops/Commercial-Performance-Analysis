import matplotlib.pyplot as plt 
import seaborn as sns
import os
from connection import get_db_data

def run_analysis():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, "../../"))
    target_folder = os.path.join(project_root, "visualisations")
    
    # Ensuring the folder exists !
    os.makedirs(target_folder, exist_ok=True)

    # Now i fetch data from mysql workbench
    print("Step 1: Connecting to database and fetching data...")
    query_geo = """
        SELECT country, COUNT(*) AS nb_customers 
        FROM customers 
        GROUP BY country 
        ORDER BY nb_customers DESC;
    """
    df_geo = get_db_data(query_geo)

    # 3. VISUALIZATION
    print("Step 2: Generating Sales by Country chart...")
    plt.figure(figsize=(12, 8))
    
    # Updated to avoid the FutureWarning
    sns.barplot(data=df_geo, x='nb_customers', y='country', hue='country', palette='viridis', legend=False)
    
    plt.title('Customer Distribution by Country', fontsize=15)
    plt.xlabel('Number of Customers', fontsize=12)
    plt.ylabel('Country', fontsize=12)
    plt.tight_layout()

    # 4. SAVING: Using the absolute path with the 's' spelling
    output_path = os.path.join(target_folder, "sales_by_country.png")
    
    print(f"DEBUG: Saving file to: {output_path}")
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    
    print(f"SUCCESS! You can find the file here: {output_path}")

# THE START BUTTON
if __name__ == "__main__":
    run_analysis()