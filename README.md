# Lab Task - Data Transformation with Pandas

In this lab, you are tasked with enhancing the `main.py` script to read an Excel file (`raw_data.xlsx`), process the data, and write the formatted data to a new Excel file (`filtered_data.xlsx`). The lab's purpose is to train you on data transformation using Pandas.

### Pre-requisites:
1. Make a new branch with your name or fork the existing repository.
2. Run the following command to install the required dependencies:
```
pip install -r requirements.txt
```
**Note**: The `requirements.txt` should contain at least the following:
```
pandas
openpyxl
```

### Implementation Steps:

#### 1. Data Loading
Define a function `load_data` that reads an Excel file and returns a Pandas DataFrame:
```python
import pandas as pd

def load_data(file_path):
    return pd.read_excel(file_path)
```

#### 2. Data Transformation
Now, define a function `transform_waf_status` to process the loaded data:
```python
def transform_waf_status(input_path, output_path):
    df = pd.read_excel(input_path)

    # Define aggregation functions for each column
    
    # Group by 'Account Name' and apply aggregation

    # Save the transformed data
```

#### 3. Execute the Data Transformation
In your `main.py`:
```python
if __name__ == "__main__":
    input_path = "raw_data.xlsx"
    output_path = "filtered_data.xlsx"
    transform_waf_status(input_path, output_path)
    print("Data transformation completed!")
```

### Guidelines:
1. Ensure you have the required libraries installed. If not, install them using the `requirements.txt` file.
2. Make sure you understand the data and the transformation steps before writing the function.
3. Handle different possible errors gracefully, e.g., file not found, invalid data, etc.
4. Ensure your code is well-commented to explain the logic and flow of your operations, making it easier for others to understand.

### Submission:
1. Once you have completed the tasks, submit your `main.py` script with the completed functions.
2. Also, attach the `raw_data.xlsx` file you used for testing and the `filtered_data.xlsx` file generated as output.
3. Ensure that all scenarios have been tested and everything is working as expected.

Good luck and happy coding! 🐍🚀

---
