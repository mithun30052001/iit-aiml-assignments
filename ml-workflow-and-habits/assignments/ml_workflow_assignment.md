# ML Workflow Assignment

**Dataset:** Retail Customer Repeat Purchase Prediction

---

## Task 1: Label Identification and Data Leakage

### Label Column

**`repeat_purchase_flag`** is the label (target variable).

> This column directly encodes the outcome we are trying to predict — whether a customer made a repeat purchase within 30 days (1) or not (0) — making it the natural dependent variable for the binary classification model.

---

### Column That Would Introduce Data Leakage

**`discount_used_on_repeat_order`** would introduce data leakage if used as a feature.

> This column contains information about the discount applied on the repeat purchase order itself, meaning it is only populated *after* the repeat purchase has already occurred — using it as a feature would leak future information into the model, causing artificially inflated performance metrics that would not generalise to real-world predictions.

---

## Task 2: Missing ML Workflow Steps Before Model Training

### Step 1: Exploratory Data Analysis (EDA)

Before training any model, EDA should be performed to understand the distribution of features, detect missing values, identify class imbalance (e.g., what proportion of customers actually made repeat purchases), and spot outliers in columns like `avg_order_value` or `days_since_last_order`. Skipping EDA means jumping into a complex model without understanding the data, which can lead to poor feature choices, undetected data quality issues, and misleading model outputs.

---

### Step 2: Data Preprocessing and Feature Engineering

Raw data is rarely model-ready — this step involves handling missing values, encoding or scaling features, removing or isolating the data-leaking column (`discount_used_on_repeat_order`), and potentially engineering new features (e.g., interaction terms or recency–frequency combinations). Without proper preprocessing, gradient boosting models may behave unpredictably or silently learn spurious patterns, making this step essential before introducing any algorithm complexity.

---

