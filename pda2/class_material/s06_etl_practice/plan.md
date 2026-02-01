# ETL Practice - 4-Layer Architecture for Machine Learning Projects

## Project Overview

**Use Case**: Customer Churn Prediction for a Subscription-Based Service

This exercise demonstrates a complete ETL pipeline for a machine learning project, teaching students how to structure data processing in layers from raw data to ML-ready datasets.

---

## Learning Objectives

By the end of this practice, students will be able to:
1. Understand the 4-layer ETL architecture (Raw → Staging → Intermediate → Final)
2. Apply data quality checks and basic transformations in the staging layer
3. Perform feature engineering and data integration in the intermediate layer
4. Prepare a final dataset ready for ML model training
5. Write clean, documented, and reproducible ETL code

---

## Architecture Overview

```
┌─────────────┐
│   RAW       │  - Original CSV files (as received)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  STAGING    │  - Data type conversions
└──────┬──────┘  - Date parsing
       │          - Basic cleaning (NaN handling)
       │          - Column standardization
       ▼
┌─────────────┐
│INTERMEDIATE │  - Feature engineering
└──────┬──────┘  - Table joins
       │          - Aggregations
       │          - Derived metrics
       ▼
┌─────────────┐
│   FINAL     │  - Single consolidated dataset
└─────────────┘  - Ready for train/test split
                 - ML-ready format
```

---

## 1. Raw Layer - Data Sources

### Dataset 1: `customers.csv`
**Description**: Customer demographic and account information

**Columns**:
- `customer_id` (int): Unique customer identifier
- `signup_date` (string): Date customer signed up (format: "DD/MM/YYYY")
- `country` (string): Customer country
- `age` (int): Customer age (contains some NaN)
- `gender` (string): Customer gender (M/F/Other, contains some NaN)
- `subscription_tier` (string): Basic/Premium/Enterprise
- `monthly_fee` (float): Monthly subscription fee

**Data Quality Issues**:
- Date format needs conversion
- Missing values in age and gender
- Inconsistent country names (e.g., "USA", "United States", "US")

### Dataset 2: `usage_logs.csv`
**Description**: Customer product usage over time

**Columns**:
- `customer_id` (int): Unique customer identifier
- `log_date` (string): Date of usage (format: "YYYY-MM-DD")
- `sessions` (int): Number of sessions that day
- `duration_minutes` (float): Total usage time in minutes
- `features_used` (int): Number of different features accessed
- `errors_encountered` (int): Number of errors during usage

**Data Quality Issues**:
- Some customers have missing days
- Negative values in duration_minutes (data entry errors)
- Date format needs standardization

### Dataset 3: `support_tickets.csv`
**Description**: Customer support interactions

**Columns**:
- `ticket_id` (int): Unique ticket identifier
- `customer_id` (int): Customer who created the ticket
- `created_date` (string): Ticket creation date (format: "YYYY/MM/DD HH:MM:SS")
- `resolved_date` (string): Ticket resolution date (contains NaN for unresolved)
- `category` (string): Issue category (Technical/Billing/General)
- `priority` (string): Low/Medium/High
- `satisfaction_score` (float): 1-5 rating (NaN if not provided)

**Data Quality Issues**:
- Datetime format needs parsing
- Unresolved tickets have NaN in resolved_date
- Missing satisfaction scores

### Dataset 4: `churn.csv`
**Description**: Target variable - whether customer churned

**Columns**:
- `customer_id` (int): Unique customer identifier
- `churn_date` (string): Date customer cancelled (format: "YYYY-MM-DD")
- `churned` (int): 1 if churned, 0 if active
- `observation_date` (string): Date of observation (2024-12-31 for all)

**Data Quality Issues**:
- Only churned customers have churn_date
- Date formats need standardization

---

## 2. Staging Layer Notebook (`01_staging.ipynb`)

### Purpose
Clean and standardize raw data, making it consistent and ready for further processing.

### Key Concepts to Teach
1. **Data Type Conversions**: Converting strings to proper datetime objects
2. **Handling Missing Values**: Different strategies (fill, drop, impute)
3. **Data Validation**: Checking for impossible values
4. **Standardization**: Consistent formats across datasets

### Transformations per Dataset

#### `customers_staged.csv`
- Convert `signup_date` to datetime
- Standardize country names (create mapping dict)
- Fill missing `age` with median
- Fill missing `gender` with "Unknown"
- Ensure `subscription_tier` is title case
- Validate: age between 18-100, monthly_fee > 0

#### `usage_logs_staged.csv`
- Convert `log_date` to datetime
- Replace negative `duration_minutes` with 0
- Ensure all numeric columns are proper types
- Sort by customer_id and log_date
- Validate: sessions >= 0, features_used >= 0

#### `support_tickets_staged.csv`
- Parse `created_date` and `resolved_date` to datetime
- Fill missing `resolved_date` with pd.NaT (keep as missing)
- Fill missing `satisfaction_score` with 0 (indicating no feedback)
- Standardize `category` and `priority` to title case
- Calculate `resolution_time_hours` where applicable

#### `churn_staged.csv`
- Convert `churn_date` and `observation_date` to datetime
- Validate: churned column is binary (0 or 1)
- Ensure all customer_ids are present

### Code Structure
```python
# For each dataset:
# 1. Load raw data
# 2. Inspect data (shape, dtypes, missing values)
# 3. Apply transformations
# 4. Validate results
# 5. Save to staging folder
```

### Output Files
- `staging/customers_staged.csv`
- `staging/usage_logs_staged.csv`
- `staging/support_tickets_staged.csv`
- `staging/churn_staged.csv`

---

## 3. Intermediate Layer Notebook (`02_intermediate.ipynb`)

### Purpose
Create features from staged data and join tables to build analytical datasets.

### Key Concepts to Teach
1. **Aggregations**: Groupby operations for creating summary statistics
2. **Time-based Features**: Extracting temporal patterns
3. **Joining Tables**: Merging multiple data sources
4. **Feature Engineering**: Creating predictive features from raw data

### Feature Engineering Tasks

#### Customer Features (from `customers_staged.csv`)
- `account_age_days`: Days since signup (as of observation_date)
- `is_premium`: Binary flag for Premium/Enterprise tiers
- `age_group`: Categorical bins (18-25, 26-35, 36-50, 51+)
- `country_region`: Group countries into regions

#### Usage Features (from `usage_logs_staged.csv`)
**Aggregate per customer over the observation period (e.g., last 90 days)**:
- `total_sessions`: Total number of sessions
- `avg_session_duration`: Average session duration in minutes
- `total_usage_minutes`: Total time spent
- `avg_features_per_session`: Average features used per session
- `total_errors`: Total errors encountered
- `days_active`: Number of unique days with activity
- `usage_consistency`: Std deviation of daily sessions (lower = more consistent)
- `last_activity_date`: Most recent usage date
- `days_since_last_activity`: Days since last activity
- `usage_trend`: Slope of sessions over time (increasing/decreasing engagement)

#### Support Features (from `support_tickets_staged.csv`)
**Aggregate per customer**:
- `total_tickets`: Total number of support tickets
- `unresolved_tickets`: Number of tickets still open
- `avg_resolution_hours`: Average time to resolve tickets
- `technical_tickets_pct`: Percentage of technical issues
- `high_priority_tickets`: Count of high priority tickets
- `avg_satisfaction`: Average satisfaction score (excluding 0s)
- `last_ticket_date`: Most recent ticket date
- `days_since_last_ticket`: Days since last ticket

### Joining Strategy
```python
# 1. Create customer features dataframe
# 2. Create usage features dataframe (aggregated)
# 3. Create support features dataframe (aggregated)
# 4. Join all together on customer_id (left join from customers)
# 5. Join with churn data
```

### Output File
- `intermediate/features.csv`

---

## 4. Final Layer Notebook (`03_final.ipynb`)

### Purpose
Prepare the final ML-ready dataset with proper encoding and feature selection.

### Key Concepts to Teach
1. **Feature Selection**: Choosing relevant features for the model
2. **Encoding Categorical Variables**: One-hot encoding, label encoding
3. **Handling Missing Values in Features**: Final imputation strategies
4. **Data Validation**: Ensuring dataset is ready for ML
5. **Train/Test Split Considerations**: What the final dataset should look like

### Final Transformations

#### Feature Selection
- Remove redundant features (e.g., customer_id, dates)
- Remove leakage features (churn_date - only use churned as target)
- Keep only predictive features

#### Encoding
- One-hot encode: `subscription_tier`, `gender`, `age_group`, `country_region`
- Keep numeric features as-is
- Create binary flags where appropriate

#### Missing Value Handling
- Fill remaining NaN in usage features with 0 (no usage)
- Fill remaining NaN in support features with 0 (no tickets)
- Validate no missing values remain (or explicitly handle)

#### Feature Scaling Preparation
- Note: Actual scaling should be done AFTER train/test split
- Document which features should be scaled (numeric continuous)
- Document which features should not be scaled (binary, one-hot encoded)

#### Final Dataset Structure
**Target Variable**: `churned` (0 or 1)

**Feature Categories**:
1. **Demographic Features**: age, gender_*, country_region_*, subscription_tier_*
2. **Account Features**: account_age_days, monthly_fee, is_premium
3. **Usage Features**: All engineered usage metrics
4. **Support Features**: All engineered support metrics

### Validation Checks
```python
# 1. Check for missing values
# 2. Check for infinite values
# 3. Verify data types
# 4. Check target variable distribution
# 5. Verify no data leakage (no future information)
# 6. Check for duplicate rows
```

### Train/Test Split Demonstration
```python
from sklearn.model_selection import train_test_split

# Separate features and target
X = final_df.drop('churned', axis=1)
y = final_df['churned']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Display shapes and class distribution
```

### Output File
- `final/ml_ready_dataset.csv`

---

## 5. Implementation Plan

### Step 1: Create Raw Datasets
Create synthetic data using pandas and numpy to simulate realistic business data:
- Generate ~5000 customers
- Generate usage logs covering 90 days
- Generate support tickets with realistic patterns
- Generate churn labels (20-30% churn rate)

### Step 2: Create Staging Notebook
- Start with explanatory markdown cells
- Show before/after for each transformation
- Include data quality checks
- Add comments explaining each operation
- Show sample outputs

### Step 3: Create Intermediate Notebook
- Explain aggregation concepts
- Show feature engineering rationale
- Demonstrate join operations
- Visualize key features
- Show correlation with target

### Step 4: Create Final Notebook
- Explain encoding strategies
- Show final feature list
- Demonstrate validation checks
- Show train/test split
- Provide summary statistics

---

## 6. Folder Structure

```
s06_etl_practice/
├── plan.md (this file)
├── raw/
│   ├── customers.csv
│   ├── usage_logs.csv
│   ├── support_tickets.csv
│   └── churn.csv
├── staging/
│   ├── customers_staged.csv
│   ├── usage_logs_staged.csv
│   ├── support_tickets_staged.csv
│   └── churn_staged.csv
├── intermediate/
│   └── features.csv
├── final/
│   └── ml_ready_dataset.csv
├── notebooks/
│   ├── 00_generate_raw_data.ipynb (utility to create raw datasets)
│   ├── 01_staging.ipynb
│   ├── 02_intermediate.ipynb
│   └── 03_final.ipynb
└── solutions/ (optional)
    ├── 01_staging_solved.ipynb
    ├── 02_intermediate_solved.ipynb
    └── 03_final_solved.ipynb
```

---

## 7. Teaching Notes

### Discussion Points
1. **Why 4 layers?**
   - Separation of concerns
   - Easier debugging
   - Reproducibility
   - Team collaboration

2. **When to fill vs. drop NaN?**
   - Business context matters
   - Amount of missing data
   - Importance of the feature

3. **Feature engineering creativity**
   - Domain knowledge is key
   - Temporal features are powerful for churn
   - Interaction features can be valuable

4. **Data leakage prevention**
   - No future information
   - Be careful with aggregations
   - Understand temporal relationships

### Common Pitfalls to Address
- Applying train statistics to test data
- Using deprecated pandas methods
- Not validating data at each stage
- Creating features that won't be available in production

### Extensions (Advanced Students)
1. Add data versioning (using DVC or similar)
2. Create a pipeline using prefect/airflow
3. Add data quality tests (using Great Expectations)
4. Create an automated ETL script that runs all notebooks
5. Add logging and error handling
6. Create a configuration file for parameters

---

## 8. Estimated Timeline

- **Raw data generation**: 1-2 hours
- **Staging notebook**: 2-3 hours (including explanations)
- **Intermediate notebook**: 2-3 hours
- **Final notebook**: 1-2 hours
- **Testing and refinement**: 1-2 hours

**Total**: ~8-12 hours of development time

---

## 9. Next Steps

1. ✅ Create folder structure
2. ⬜ Generate synthetic raw datasets
3. ⬜ Create staging notebook with solutions
4. ⬜ Create intermediate notebook with solutions
5. ⬜ Create final notebook with solutions
6. ⬜ Test complete pipeline end-to-end
7. ⬜ Create student versions (remove solutions)
8. ⬜ Prepare presentation slides (if needed)
9. ⬜ Create assessment/exercises

---

## 10. Assessment Ideas

### Coding Exercises
1. Add a new feature to the intermediate layer
2. Handle a data quality issue in staging
3. Fix a deliberately introduced bug in the pipeline

### Conceptual Questions
1. Explain why we separate staging and intermediate layers
2. What would happen if we one-hot encode before train/test split?
3. How would you modify this pipeline for real-time predictions?

### Project Extension
Ask students to:
- Add a 5th raw dataset (e.g., payment history)
- Integrate it through all layers
- Justify their transformation decisions
