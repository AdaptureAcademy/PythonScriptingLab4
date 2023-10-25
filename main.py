import pandas as pd

def transform_waf_status(input_path: str, output_path: str) -> None:
    df = pd.read_excel(input_path)

    # Define aggregation functions for each column
    agg_funcs = {
        'No of Zones': pd.NamedAgg(column='Zone ID',aggfunc= 'count'),
        'Old WAF Status-Enabled': pd.NamedAgg( column = 'old_waf_status', aggfunc = lambda x:(x == 'enabled').sum()),
        'Old WAF Status-Disabled': pd.NamedAgg( column='old_waf_status', aggfunc= lambda x : (x == 'disabled').sum()),
        'Old WAF Status-Free Plan': pd.NamedAgg(column='old_waf_status',aggfunc = lambda x : (x == 'Free Plan').sum()),
        'New WAF Status-Enabled': pd.NamedAgg(column='new_waf_status',aggfunc = lambda x :( x == 'enabled').sum()),
        'New WAF Status-Disabled': pd.NamedAgg(column='new_waf_status',aggfunc = lambda x :( x == 'disabled').sum()),
        'New WAF Status-Free Plan': pd.NamedAgg(column='new_waf_status',aggfunc = lambda x :( x == 'Free Plan').sum()),
        'Source-Default': pd.NamedAgg(column='source',aggfunc = lambda x :( x == 'defaults').sum()),
        'Source-Zone': pd.NamedAgg(column='source',aggfunc = lambda x :( x == 'zone').sum()),
        'Source-Free Plan': pd.NamedAgg(column='source',aggfunc = lambda x :( x == 'Free Plan').sum()),
        'Migration Status-Default': pd.NamedAgg(column='migration_state',aggfunc = lambda x :( x == 'default').sum()),
        'Migration Status-Complete': pd.NamedAgg(column='migration_state',aggfunc = lambda x :( x == 'complete').sum()),
        'Migration Status-Start': pd.NamedAgg(column='migration_state',aggfunc = lambda x :( x == 'start').sum()),
        'Migration Status-Validation': pd.NamedAgg(column='migration_state',aggfunc = lambda x :( x == 'validation').sum()),
        'Migration Status-Free Plan': pd.NamedAgg(column='migration_state',aggfunc = lambda x :( x == 'Free Plan').sum())
        
    }


    # Group by 'Account Name' and apply aggregation
    grouped = df.groupby('Account Name').agg(**agg_funcs).reset_index()

    # Save the transformed data to an output XLSX file
    grouped.to_excel(output_path, index=False)

if __name__ == "__main__":
    input_path = "raw_data.xlsx"  
    output_path = "my_filtered_data.xlsx"  
    transform_waf_status(input_path, output_path)
    print("Data transformation completed!")
