# InternNova — Data Analytics Internship
## Week 2 Assignment: NumPy & Pandas for Data Analytics 
**Dataset:** `employees.csv`& `departments.csv` \
**Prepared by:** Brojo Mohan Dutta   
 
# Task 1: NumPy Introduction & Arrays 
import numpy as np

arr = np.array([12, 45, 23, 67, 34, 89, 15, 56, 78, 90])
print("Array:", arr)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)

arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("1D Array:\n", arr_1d)
print("2D Array:\n", arr_2d)


# Task 2: NumPy Indexing, Slicing & Reshaping
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print("Element at index 3:", arr[3])
print("Sliced array (index 2 to 5):", arr[2:6])

arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("2D Array:\n", arr_2d)
print("Row 1:", arr_2d[1])
print("Column 2:", arr_2d[:, 2])

reshaped = arr.reshape(2, 4)
print("Original array:", arr)
print("Reshaped array (2x4):\n", reshaped)
 

# Task 3: NumPy Mathematical & Statistical Operations
import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([1, 2, 3, 4, 5])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))
print("Standard Deviation:", np.std(a))
print("Sum:", np.sum(a))


# Task 4: Pandas Series & Data Frame
import pandas as pd

s = pd.Series([25, 30, 35, 40], index=["a", "b", "c", "d"])
print("Pandas Series:\n", s)

data = {
    "name": ["Aarav Sharma", "Priya Nair", "Rohan Das"],
    "department": ["Sales", "Marketing", "Sales"],
    "salary": [42000, 55000, 48000]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
print("Column Names:", df.columns.tolist())
print("Index:", df.index.tolist())

df["bonus"] = df["salary"] * 0.10
print("Updated DataFrame with bonus column:\n", df)


# Task 5: Reading & Inspecting Data
import pandas as pd

df = pd.read_csv("employees.csv")

print("First 5 rows:\n", df.head())
print("Last 5 rows:\n", df.tail())
print("Shape (rows, columns):", df.shape)
print("Column Names:", df.columns.tolist())
print("Data Types:\n", df.dtypes)
print("Info:")
df.info()
print("Describe:\n", df.describe())
 

# Task 6: Selecting, Filtering & Sorting Data
import pandas as pd

df = pd.read_csv("employees.csv")

print("Selected columns (name, department, salary):\n", df[["name", "department", "salary"]])

print("Selected rows (index 0 to 4):\n", df.iloc[0:5])

print("Filter: salary > 55000:\n", df[df["salary"] > 55000])

print("Multiple conditions: department == 'Sales' AND salary > 45000:\n",
      df[(df["department"] == "Sales") & (df["salary"] > 45000)])

print("Sorted ascending by salary:\n", df.sort_values("salary"))
print("Sorted descending by salary:\n", df.sort_values("salary", ascending=False))


# Task 7: Handling Missing Values# --- String Operations ---
import pandas as pd

df = pd.read_csv("employees.csv")

print("Missing values (True/False):\n", df.isnull())
print("Missing values count per column:\n", df.isnull().sum())

df_dropped = df.dropna()
print("Dataset after dropping rows with missing values:\n", df_dropped)

df_filled = df.copy()
df_filled["age"] = df_filled["age"].fillna(df_filled["age"].mean())
df_filled["salary"] = df_filled["salary"].fillna(df_filled["salary"].median())
print("Dataset after filling missing values (age->mean, salary->median):\n", df_filled)


# Task 8: Merge, Concatenate, GroupBy & Pivot Table  
import pandas as pd

employees = pd.read_csv("employees.csv")
departments = pd.read_csv("departments.csv")

# Merge
merged_df = pd.merge(employees, departments, on="department", how="left")
print("Merged DataFrame (employees + departments):\n", merged_df)

# Concatenate
new_hires = pd.DataFrame({
    "emp_id": [116, 117],
    "name": ["Tanya Sen", "Farhan Ali"],
    "department": ["Sales", "IT"],
    "age": [24, 30],
    "salary": [44000, 66000],
    "city": ["Kolkata", "Bangalore"],
    "join_year": [2023, 2023]
})
concatenated_df = pd.concat([employees, new_hires], ignore_index=True)
print("Concatenated DataFrame (original + new hires):\n", concatenated_df)

# GroupBy
grouped = employees.groupby("department")["salary"].agg(["sum", "mean", "count", "min", "max"])
print("GroupBy department -> salary aggregates:\n", grouped)

# Pivot Table
pivot = pd.pivot_table(employees, values="salary", index="department", columns="city", aggfunc="mean")
print("Pivot Table (avg salary by department & city):\n", pivot)


# Task 9: Exporting Data 
import pandas as pd

df = pd.read_csv("employees.csv")

df["age"] = df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(df["salary"].median())

df.to_csv("employees_processed.csv", index=False)

check = pd.read_csv("employees_processed.csv")
print("Exported file preview:\n", check.head())
print("Exported file shape:", check.shape)
print("Missing values after export:\n", check.isnull().sum())


# Task 10: Mini Data Analysis Project
import pandas as pd

# 1. Load dataset
df = pd.read_csv("employees.csv")

# 2. Data inspection
print("Shape:", df.shape)
df.info()
print("Describe:\n", df.describe())

# 3. Handle missing values
print("Missing values before cleaning:\n", df.isnull().sum())
df["age"] = df["age"].fillna(df["age"].mean()).round().astype(int)
df["salary"] = df["salary"].fillna(df["salary"].median())
print("Missing values after cleaning:\n", df.isnull().sum())

# 4. Selecting & filtering
high_earners = df[df["salary"] > 55000]
print("High earners (salary > 55000):\n", high_earners[["name", "department", "salary"]])

# 5. Sorting
top5_salary = df.sort_values("salary", ascending=False).head(5)
print("Top 5 salaries:\n", top5_salary[["name", "department", "salary"]])

# 6. GroupBy analysis
dept_summary = df.groupby("department")["salary"].agg(["mean", "count"]).round(2)
print("Average salary & headcount by department:\n", dept_summary)

# 7. Pivot table
pivot = pd.pivot_table(df, values="salary", index="department", columns="city", aggfunc="mean")
print("Pivot table - avg salary by department & city:\n", pivot)

# 8. Insights
highest_paid_dept = dept_summary["mean"].idxmax()
largest_dept = df["department"].value_counts().idxmax()
print(f"Insight 1: '{highest_paid_dept}' has the highest average salary.")
print(f"Insight 2: '{largest_dept}' has the most employees.")
print(f"Insight 3: Overall average salary is {df['salary'].mean():.2f}.")

# 9. Export cleaned dataset
df.to_csv("employee_analysis_final.csv", index=False)
print("Cleaned dataset exported as 'employee_analysis_final.csv'")
