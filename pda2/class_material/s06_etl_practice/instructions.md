# ETL Practice: Instructions

## 📚 Overview

Welcome to the ETL (Extract, Transform, Load) practice session! In this exercise, you'll learn how to build a complete data pipeline for a machine learning project using the **4-layer architecture**:

1. **Raw** - Original data files
2. **Staging** - Clean and standardize
3. **Intermediate** - Feature engineering and joins
4. **Final** - ML-ready dataset

## 🎯 Learning Objectives

By completing this exercise, you will:
- Understand the purpose of each ETL layer
- Learn data cleaning and standardization techniques
- Practice feature engineering for ML
- Master pandas aggregation and joining operations
- Prepare data properly for machine learning

---

## 📁 Project Structure

```
s06_etl_practice/
├── plan.md                          # Detailed project plan
├── instructions.md                  # This file
├── raw/                             # ✅ Already created
│   ├── customers.csv
│   ├── usage_logs.csv
│   ├── support_tickets.csv
│   └── churn.csv
├── staging/                         # You'll create these
│   └── (staged CSV files)
├── intermediate/                    # You'll create these
│   └── features.csv
├── final/                           # You'll create these
│   └── ml_ready_dataset.csv
└── notebooks/
    ├── 00_generate_raw_data.ipynb   # ✅ Already run
    ├── 01_staging.ipynb             # ← START HERE
    ├── 02_intermediate.ipynb        # ← Then this
    └── 03_final.ipynb               # ← Finally this
```

---

## 🚀 Getting Started

### Step 0: Verify Raw Data Exists

The raw datasets have already been generated. Verify they exist:

```python
import pandas as pd

# Check if raw files exist
customers = pd.read_csv('raw/customers.csv')
print(f"Customers: {customers.shape}")

usage_logs = pd.read_csv('raw/usage_logs.csv')
print(f"Usage Logs: {usage_logs.shape}")

support_tickets = pd.read_csv('raw/support_tickets.csv')
print(f"Support Tickets: {support_tickets.shape}")

churn = pd.read_csv('raw/churn.csv')
print(f"Churn: {churn.shape}")
```

Expected output:
- Customers: (5000, 7)
- Usage Logs: (~212,000, 6)
- Support Tickets: (~6,000, 7)
- Churn: (5000, 4)

---

## 📝 Layer 1: Staging (`01_staging.ipynb`)

### Time Estimate: 30-45 minutes (In Class)

### Goal
Clean and standardize raw data - fix data types, handle missing values, correct errors.

### Tasks

#### For `customers.csv`:
1. ✅ **Convert `signup_date`** from DD/MM/YYYY string to datetime
   - Hint: Use `pd.to_datetime()` with `dayfirst=True`

2. ✅ **Standardize country names**
   - Create a mapping: `{'United States': 'USA', 'US': 'USA', 'United Kingdom': 'UK', 'Britain': 'UK'}`
   - Use `.replace()` to apply the mapping

3. ✅ **Handle missing ages**
   - Strategy: Fill with median age
   - Hint: `df['age'].fillna(df['age'].median())`

4. ✅ **Handle missing genders**
   - Strategy: Fill with "Unknown"
   - Hint: `df['gender'].fillna('Unknown')`

5. ✅ **Standardize `subscription_tier`**
   - Convert to title case: "Basic", "Premium", "Enterprise"
   - Hint: `df['subscription_tier'].str.title()`

6. ✅ **Validate** the data
   - Check: age between 18-100
   - Check: monthly_fee > 0
   - Check: no missing values remain

7. ✅ **Save** to `staging/customers_staged.csv`

#### For `usage_logs.csv`:
1. ✅ **Convert `log_date`** to datetime
   - Format is already YYYY-MM-DD (easier!)

2. ✅ **Fix negative `duration_minutes`**
   - Replace negative values with 0
   - Hint: `df.loc[df['duration_minutes'] < 0, 'duration_minutes'] = 0`

3. ✅ **Sort** by customer_id and log_date
   - Hint: `df.sort_values(['customer_id', 'log_date'])`

4. ✅ **Validate** no negative values in any column

5. ✅ **Save** to `staging/usage_logs_staged.csv`

#### For `support_tickets.csv`:
1. ✅ **Parse datetime columns**
   - `created_date` and `resolved_date`
   - Hint: `pd.to_datetime(df['created_date'])`

2. ✅ **Handle missing `satisfaction_score`**
   - Fill with 0 (meaning "no feedback")

3. ✅ **Standardize `category` and `priority`**
   - Convert to title case

4. ✅ **Calculate `resolution_time_hours`**
   - Formula: `(resolved_date - created_date).dt.total_seconds() / 3600`

5. ✅ **Validate** resolved_date > created_date (for resolved tickets)

6. ✅ **Save** to `staging/support_tickets_staged.csv`

#### For `churn.csv`:
1. ✅ **Convert dates** to datetime
   - `churn_date` and `observation_date`

2. ✅ **Validate**
   - churned column is 0 or 1
   - If churned=1, churn_date should exist
   - If churned=0, churn_date should be NaN

3. ✅ **Save** to `staging/churn_staged.csv`

### ✅ Success Criteria
- All date columns are datetime objects
- No invalid values (negative numbers where they shouldn't be)
- Missing values handled appropriately
- All files saved to `staging/` folder

---

## 🔧 Layer 2: Intermediate (`02_intermediate.ipynb`)

### Time Estimate: 45-60 minutes (Partially in class, complete as homework)

### Goal
Create features from staged data and join everything into one dataset.

### Tasks

#### Part 1: Customer Features
1. ✅ **Calculate `account_age_days`**
   - Days from signup_date to observation_date
   - Hint: `(observation_date - df['signup_date']).dt.days`

2. ✅ **Create `is_premium`** binary flag
   - 1 if Premium or Enterprise, 0 if Basic
   - Hint: `df['subscription_tier'].isin(['Premium', 'Enterprise']).astype(int)`

3. ✅ **Create `age_group`** categories
   - Bins: [0, 25, 35, 50, 100]
   - Labels: ['18-25', '26-35', '36-50', '51+']
   - Hint: `pd.cut(df['age'], bins=..., labels=...)`

4. ✅ **Map `country_region`**
   - Group countries into regions (North America, Europe, etc.)

#### Part 2: Usage Features (⚡ Most Important!)
Aggregate usage_logs by customer_id. Calculate:

1. ✅ **Total and average sessions**
   - `total_sessions` = sum of sessions
   - `avg_sessions_per_day` = mean of sessions

2. ✅ **Usage time metrics**
   - `total_usage_minutes` = sum of duration_minutes
   - `avg_session_duration` = mean of duration_minutes

3. ✅ **Feature usage**
   - `avg_features_per_session` = mean of features_used

4. ✅ **Errors**
   - `total_errors` = sum of errors_encountered

5. ✅ **Activity metrics**
   - `days_active` = count of unique log_dates
   - `last_activity_date` = max of log_date
   - `days_since_last_activity` = observation_date - last_activity_date

6. ✅ **Usage consistency**
   - `usage_consistency_std` = std of sessions (lower = more consistent)

7. ✅ **Usage trend**
   - Compare early period vs late period usage
   - Positive = increasing usage, Negative = decreasing

**Hint**: Use `groupby('customer_id').agg({...})`

#### Part 3: Support Features
Aggregate support_tickets by customer_id. Calculate:

1. ✅ **Ticket counts**
   - `total_tickets` = count
   - `unresolved_tickets` = count where resolved_date is NaN

2. ✅ **Resolution metrics**
   - `avg_resolution_hours` = mean of resolution_time_hours

3. ✅ **Ticket types**
   - `technical_tickets_pct` = percentage that are Technical
   - `high_priority_tickets` = count of High priority

4. ✅ **Satisfaction**
   - `avg_satisfaction` = mean of satisfaction_score (excluding 0)

5. ✅ **Recency**
   - `days_since_last_ticket` = days since last ticket

#### Part 4: Join Everything
1. ✅ Start with customers as base
2. ✅ **Left join** usage features (not all customers have usage)
3. ✅ **Left join** support features (not all customers have tickets)
4. ✅ **Left join** churn labels
5. ✅ **Fill NaN** with 0 for customers with no usage/tickets
6. ✅ **Save** to `intermediate/features.csv`

### ✅ Success Criteria
- One row per customer (5,000 rows)
- ~30-35 columns (features + target)
- No missing values (all filled appropriately)
- All customers have churn label

---

## 🎯 Layer 3: Final (`03_final.ipynb`)

### Time Estimate: 30-45 minutes (Homework)

### Goal
Prepare ML-ready dataset with encoded features.

### Tasks

#### Step 1: Remove Unnecessary Columns
1. ✅ Drop `customer_id` (identifier, not predictive)
2. ✅ Drop `signup_date` (already in account_age_days)
3. ✅ Drop `country` (already in country_region)

#### Step 2: Encode Categorical Variables
1. ✅ **One-hot encode**:
   - `gender`
   - `subscription_tier`
   - `age_group`
   - `country_region`
   - Hint: `pd.get_dummies(df, columns=[...], drop_first=False, dtype=int)`

#### Step 3: Validate
1. ✅ Check for missing values (should be 0)
2. ✅ Check for infinite values (should be 0)
3. ✅ Check target distribution (~25% churn rate)
4. ✅ Check for data leakage (no future information)
5. ✅ Check for duplicates (should be 0)

#### Step 4: Document Features
1. ✅ Categorize features:
   - Demographic (gender, age_group)
   - Account (age, monthly_fee, tier, premium flag)
   - Geographic (region)
   - Usage (all usage metrics)
   - Support (all support metrics)

#### Step 5: Save
1. ✅ **Save** to `final/ml_ready_dataset.csv`

#### Step 6: Demonstrate Train/Test Split
1. ✅ Separate X (features) and y (target)
2. ✅ Split 80/20 with stratification
3. ✅ Show churn rate is balanced
4. ✅ Document which features to scale (continuous) vs not scale (binary/one-hot)

### ✅ Success Criteria
- All features are numeric
- No missing values
- Ready for sklearn
- Proper documentation

---

## 💡 Tips for Success

### General Tips
1. **Read the explanations** in each notebook - they teach the concepts
2. **Run cells in order** - later cells depend on earlier ones
3. **Check your work** - use `.head()`, `.info()`, `.describe()` frequently
4. **Validate at each step** - catch errors early!

### Common Mistakes to Avoid
❌ **DON'T**:
- Skip validation steps
- Forget to save your work
- Create features in the staging layer (only clean!)
- Include future information (data leakage)
- Scale features before train/test split

✅ **DO**:
- Understand WHY each transformation is needed
- Check for missing values after each step
- Use meaningful variable names
- Comment your code
- Ask questions when confused!

### Debugging Tips
If something doesn't work:
1. Check the error message carefully
2. Print intermediate results
3. Check data types: `df.dtypes`
4. Check for missing values: `df.isna().sum()`
5. Check shape: `df.shape`

---

## 📊 Expected Results Summary

| Layer | Input | Output | Key Metrics |
|-------|-------|--------|-------------|
| **Raw** | N/A | 4 CSV files | 5K customers, ~212K logs, ~6K tickets |
| **Staging** | 4 raw CSVs | 4 clean CSVs | All dates parsed, no invalid values |
| **Intermediate** | 4 staged CSVs | 1 features CSV | 5K rows × ~35 columns |
| **Final** | 1 features CSV | 1 ML-ready CSV | 5K rows × ~40+ encoded columns |

---

## 🏆 What You're Building

You're preparing data for a **Customer Churn Prediction** model. The business question:

> *"Which customers are likely to cancel their subscription in the next 90 days?"*

Your ETL pipeline transforms raw operational data into ML-ready features that capture:
- **Who** the customer is (demographics, account info)
- **How** they use the product (usage patterns)
- **If** they need support (ticket history)

This will enable models to predict churn and help the business take action!

---

## ⏱️ Time Management

### In Class (1.5 hours)
- ✅ Overview and setup: 10 min
- ✅ Staging layer: 40-50 min (complete together)
- ✅ Intermediate layer (Part 1 & 2): 30-40 min (start together)

### Homework
- ✅ Intermediate layer (complete Parts 3 & 4): 20-30 min
- ✅ Final layer: 30-45 min
- ✅ Total homework time: ~1 hour

---

## 🤔 Comprehension Check Questions

After completing each layer, answer these:

### After Staging:
1. Why do we fill missing ages with median instead of mean?
2. Why is it okay for `churn_date` to have missing values?
3. What would happen if we didn't fix negative durations?

### After Intermediate:
1. Why do we use left joins instead of inner joins?
2. What does a negative `usage_trend` indicate?
3. Why might `days_since_last_activity` be predictive of churn?

### After Final:
1. Why do we drop `customer_id` before training?
2. Why must we scale AFTER train/test split?
3. What is data leakage and how did we prevent it?

---

## 🆘 Getting Help

### During Class
- Raise your hand
- Ask in the class chat
- Work with a neighbor

### Outside Class
- Review the notebook explanations
- Check the `plan.md` file for detailed specs
- Post questions in the course forum
- Office hours

---

## 🎓 Learning Resources

### Pandas Documentation
- [pd.to_datetime()](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)
- [groupby()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)
- [merge()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
- [get_dummies()](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html)

### Concepts
- ETL pipelines
- Feature engineering
- Data leakage
- Train/test splitting

---

## ✅ Submission Checklist

Before considering the exercise complete:

- [ ] All raw datasets exist in `raw/` folder
- [ ] All 4 staged files saved in `staging/` folder
- [ ] `features.csv` saved in `intermediate/` folder
- [ ] `ml_ready_dataset.csv` saved in `final/` folder
- [ ] No missing values in final dataset
- [ ] All categorical variables encoded
- [ ] Can successfully perform train/test split
- [ ] Understand the purpose of each layer
- [ ] Can explain your transformations

---

## 🎉 Bonus Challenges

If you finish early or want extra practice:

1. **Add a new feature** in the intermediate layer
   - Example: "percentage of days active" = days_active / 90

2. **Create interaction features**
   - Example: usage_per_dollar = total_usage_minutes / monthly_fee

3. **Add data visualizations**
   - Plot churn rate by subscription tier
   - Plot usage trends for churned vs active customers

4. **Calculate feature importance**
   - Use correlation with target
   - Identify top 10 most predictive features

5. **Build a simple model**
   - Logistic Regression
   - Calculate accuracy, precision, recall

---

## 📝 Final Notes

This exercise mirrors real-world data science workflows. In actual projects:
- Data is messier (you'll spend 70-80% of time on ETL!)
- Business context drives feature engineering
- Iteration is key (you'll revisit and improve features)
- Documentation is critical (for yourself and others)

Take your time, understand each step, and don't hesitate to ask questions. The goal is learning, not just completing!

**Good luck! 🚀**
