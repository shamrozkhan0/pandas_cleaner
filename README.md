# Data Cleaner With Pandas 2.0
#### This cleaner is made using `python` and `pandas` using industry standard practices. Use `median()`, `mean()`, `fillna()` etc.

---

### Problems:
- Column with `Nan`
- Incorrect `DateTime` format
- Missing Values
- Un-realistic Values
- Outlier

### Cleaning Steps:

- `Step 1: Convert CSV File Data into DataFrame `
- `Step 2: Removes Duplicate order_id`
- `Step 3: Fills Nan valus: ` 
     - `Column "customer_name", "city", "gender" to unknown instead of removing the row, becuase sales data need to be accurate.`
     - `For age i have taken the age column median(), because in age outlier is common because customer can be of age 5 or 50, and for the amount and date column.`
- `Step 4: Capatitalize the gender value and filling unknown if the value is midding, and standardizing M/F to Male and Female.`
- `Step 5: Capitalizizing Status and replacing complete to Completed.`
- `Step 6: Genrating CSV`


