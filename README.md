# 📊 Data Cleaner with Pandas

A data cleaning pipeline built using **Python and Pandas** that handles real-world messy sales data using practical and business-oriented rules.

This project simulates how data analysts and AI engineers clean raw datasets before analysis or modeling.

---

## 🚀 Purpose

Real-world data is rarely clean.  
This project demonstrates how to:

- Handle missing values
- Fix inconsistent formats
- Remove duplicates
- Validate unrealistic values
- Standardize categorical data
- Log cleaning steps professionally

It follows beginner-friendly **production-style practices**.

---

## 🛠 Tech Stack

- Python
- Pandas
- Logging module

---

## 📂 Dataset Issues

The raw dataset contains:

- Missing values (NaN)
- Incorrect datetime formats
- Duplicate records
- Unrealistic values (age outliers)
- Inconsistent categorical values (gender/status)
- Formatting issues in amount column

---

## 🧹 Cleaning Steps

### 1️⃣ Load Data
- Reads CSV using Pandas
- Handles bad lines safely

### 2️⃣ Remove Duplicates
- Drops duplicate `order_id` records

### 3️⃣ Handle Missing Values
- `customer_name` & `city` → filled with `"Unknown"`
- `age` → filled with median
- Validates age range
- `amount` → filled with median
- `order_date` → converted to datetime and filled using median date

### 4️⃣ Standardize Gender
- Converts M/F to Male/Female
- Capitalizes values
- Removes extra spaces

### 5️⃣ Standardize Status
- Fixes variations like:
  - complete
  - Completed
  - COMPLETE

### 6️⃣ Generate Clean CSV
- Exports cleaned dataset

---

## 📊 Logging

The project uses Python logging to track:

- Data loading
- Cleaning steps
- File generation

This mimics real-world data pipelines.

---

## ▶️ Usage

```bash
python main.py
