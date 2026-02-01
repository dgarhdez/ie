# Homework/Practice Plan: Datetimes & Regex Operations in Pandas

## Executive Summary

This document outlines the plan for creating a comprehensive homework/practice notebook that integrates concepts from PDA2 sessions 02-05 (datetimes, timeseries, and regex operations in pandas). The practice will be designed as a realistic business analytics scenario requiring students to apply all learned concepts in an integrated manner.

---

## Learning Objectives

### Datetime & Timeseries Operations (Sessions 02-03)
Students will demonstrate proficiency in:

1. **Parsing and converting** dates from various string formats to datetime objects
2. **Creating and manipulating** timestamps, periods, and timedeltas
3. **Indexing and filtering** time series data using date-based selection
4. **Generating date ranges** with different frequency codes (hourly, daily, weekly, monthly, business days)
5. **Resampling** time series data (aggregating from high to low frequency)
6. **Shifting and lagging** data for time-based comparisons
7. **Calculating rolling windows** (moving averages, rolling statistics)
8. **Handling time zones** and UTC conversions
9. **Extracting datetime components** (year, month, day, hour, weekday, quarter)
10. **Working with business frequencies** (business days, month-end, quarter-end)

### String & Regex Operations (Sessions 04-05)
Students will demonstrate proficiency in:

1. **Applying vectorized string operations** using the `.str` accessor
2. **Cleaning and standardizing** text data (case conversion, whitespace removal)
3. **Extracting information** from strings using slicing and indexing
4. **Building and applying regular expressions** for pattern matching
5. **Validating data formats** (emails, phone numbers, product codes)
6. **Splitting and joining** strings using delimiters
7. **Replacing and substituting** text using regex patterns
8. **Extracting groups** from regex patterns
9. **Filtering data** based on string patterns
10. **Creating categorical features** from text using regex

---

## Dataset Theme: E-commerce Platform Analytics

### Overview
We will create a realistic e-commerce/online marketplace dataset containing transaction records with rich opportunities for both datetime and string manipulation. This simulates real-world business analytics scenarios where data arrives messy and requires substantial cleaning.

### Business Context
**Scenario**: An online marketplace tracks customer transactions, product sales, and customer feedback. The data has been collected from multiple sources and contains various formatting inconsistencies that need to be cleaned before analysis.

---

## Data Structure

### Main Dataset: `ecommerce_transactions.csv`

**Size**: ~2000-2500 rows (manageable for practice, realistic for analysis)

**Date Range**: January 2024 - January 2026 (2 years of data)

**Columns**:

1. **transaction_id** (string)
   - Format: `"TXN-YYYYMMDD-XXXXXX"` (e.g., "TXN-20240315-000123")
   - Requires: Regex extraction of date and sequence number
   - Data issues: Some malformed IDs

2. **customer_id** (string)
   - Format: `"CUST-{REGION}-{NUMBER}"` (e.g., "CUST-US-0001", "CUST-EU-0234")
   - Requires: Regex parsing for region extraction
   - Data issues: Inconsistent formatting

3. **customer_name** (string)
   - Examples: "  John Smith  ", "MARY JOHNSON", "dr. robert brown", "Ms. Sarah Lee"
   - Requires: Case standardization, whitespace cleaning, title extraction
   - Data issues: Mixed case, extra spaces, titles embedded

4. **customer_email** (string)
   - Examples: "john@example.com", "MARY.JOHNSON@SHOP.COM", "invalid-email", "user@domain"
   - Requires: Validation, standardization to lowercase
   - Data issues: Some invalid formats, mixed case

5. **transaction_timestamp** (string)
   - Multiple formats:
     - ISO: "2024-03-15T14:30:00Z"
     - US: "03/15/2024 2:30 PM"
     - European: "15/03/2024 14:30"
     - Text: "March 15, 2024 at 2:30pm"
   - Requires: Parsing mixed formats, timezone handling
   - Data issues: Inconsistent formats, some missing times

6. **product_code** (string)
   - Format: `"{CATEGORY}-{SUBCATEGORY}-{ID}"` (e.g., "ELEC-PHONE-1234", "CLOTH-SHIRT-5678")
   - Requires: Regex extraction of category hierarchy
   - Categories: ELEC (Electronics), CLOTH (Clothing), HOME (Home), BOOK (Books), SPORT (Sports)

7. **product_name** (string)
   - Examples: "iPhone 15 Pro Max (256GB)", "Nike Running Shoes - Size 10", "The Great Gatsby [Paperback]"
   - Requires: Pattern extraction for details (sizes, specs, formats)
   - Data issues: Inconsistent formatting

8. **amount** (string)
   - Examples: "$149.99", "€89.50", "£75.00", "99.99", "$1,234.56"
   - Requires: Currency symbol removal, comma removal, conversion to float
   - Data issues: Mixed currency symbols, formatting inconsistencies

9. **payment_method** (string)
   - Examples: "Credit Card (Visa)", "PayPal", "credit_card", "DEBIT CARD - Mastercard"
   - Requires: Standardization, category extraction
   - Data issues: Multiple formats for same payment type

10. **shipping_address** (string)
    - Examples: "123 Main St, New York, NY 10001", "45 High Street, London, UK, SW1A 1AA"
    - Requires: ZIP/postal code extraction using regex
    - Data issues: Varied formats by country

11. **order_status** (string)
    - Examples: "Delivered on 2024-03-20", "Shipped (est. arrival: March 25)", "Processing", "Cancelled - 15/03/2024"
    - Requires: Status extraction, date extraction from text
    - Data issues: Dates embedded in text, multiple formats

12. **customer_feedback** (string)
    - Examples: "Great product! 5 stars ⭐⭐⭐⭐⭐", "Poor quality 😞", "Arrived on time 👍"
    - Requires: Sentiment indicator extraction, emoji handling
    - Data issues: Mixed content, emojis, ratings embedded in text

---

## Intentional Data Quality Issues

To provide realistic practice, the data will include:

1. **Missing values** (~10% across various columns)
2. **Inconsistent date formats** (4-5 different formats)
3. **Mixed timezones** (UTC, EST, PST, CET)
4. **Inconsistent capitalization** in names and text fields
5. **Extra whitespace** at beginning/end of strings
6. **Invalid email formats** (~5% of emails)
7. **Malformed IDs** (~3% of transaction/customer IDs)
8. **Duplicate entries** with slightly different timestamps
9. **Outlier dates** (future dates, very old dates)
10. **Mixed currency symbols** and number formats
11. **Special characters** requiring cleaning
12. **Inconsistent categorical values** (e.g., "Credit Card", "credit_card", "CREDIT CARD")

---

## Data Generation Process

### Script: `generate_ecommerce_data.py`

**Libraries to use**:
- `pandas` for data structure
- `numpy` for random generation
- `faker` for realistic names, emails, addresses
- `random` for introducing variations
- `datetime` for timestamp generation

**Generation Logic**:

1. **Create base data** (2500 transactions)
   - Random customer IDs (500 unique customers)
   - Random product codes (100 unique products)
   - Sequential transaction IDs with dates
   - Realistic amounts based on product categories

2. **Introduce format variations**:
   - Randomly apply different date formats
   - Mix timezone indicators
   - Vary case in names and text
   - Add/remove spaces randomly
   - Mix currency symbols based on region

3. **Inject data quality issues**:
   - Randomly set values to NaN
   - Create some invalid emails
   - Generate malformed IDs
   - Add duplicate transactions
   - Insert outlier dates

4. **Add realistic patterns**:
   - Higher transaction volume on weekends
   - Peak hours for online shopping (evenings)
   - Seasonal trends (higher in Q4)
   - Customer repeat purchase patterns
   - Product category correlations

**Output**: `ecommerce_transactions.csv`

---

## Homework Notebook Structure

### Part 0: Introduction and Setup (5 minutes)

**Content**:
- Business scenario description
- Learning objectives
- Dataset overview
- Import necessary libraries
- Load data and initial exploration

**Code**:
```python
import pandas as pd
import numpy as np
import re
from datetime import datetime, timedelta

# Load data
df = pd.read_csv('ecommerce_transactions.csv')

# Initial exploration
print(df.shape)
print(df.info())
print(df.head())
```

---

### Part 1: Datetime Parsing and Conversion (20 minutes)

**Exercises**:

1. **Parse mixed date formats** in `transaction_timestamp`
   - Handle multiple formats using `pd.to_datetime()` with `errors='coerce'`
   - Identify unparseable dates
   - Create a clean datetime column

2. **Extract datetime components**
   - Year, month, day, hour
   - Day of week (Monday=0, Sunday=6)
   - Quarter
   - Is weekend (boolean)
   - Hour of day category (morning, afternoon, evening, night)

3. **Identify and handle outliers**
   - Find future dates
   - Find dates before 2024
   - Replace invalid dates with median date

**Concepts Practiced**:
- `pd.to_datetime()` with format inference
- `.dt` accessor methods
- Boolean operations on datetimes
- Datetime validation

**Expected Output**: Clean datetime column with extracted components

---

### Part 2: String Cleaning and Standardization (20 minutes)

**Exercises**:

1. **Clean customer names**
   - Remove leading/trailing whitespace
   - Standardize to title case
   - Handle names with titles (Dr., Mr., Mrs., Ms.)

2. **Standardize email addresses**
   - Convert to lowercase
   - Remove extra whitespace
   - Identify invalid email formats

3. **Standardize payment methods**
   - Convert to lowercase
   - Group into categories (credit_card, debit_card, paypal, other)
   - Handle variations of same payment type

4. **Clean amount field**
   - Remove currency symbols ($, €, £)
   - Remove commas from numbers
   - Convert to float
   - Identify and handle invalid amounts

**Concepts Practiced**:
- `.str.strip()`, `.str.lower()`, `.str.upper()`, `.str.title()`
- `.str.replace()` for cleaning
- `.str.contains()` for filtering
- Type conversion with error handling

**Expected Output**: Cleaned text columns ready for analysis

---

### Part 3: Regular Expression Pattern Matching (25 minutes)

**Exercises**:

1. **Extract date from transaction_id**
   - Pattern: `TXN-YYYYMMDD-XXXXXX`
   - Extract date portion using regex groups
   - Validate against transaction_timestamp

2. **Parse customer region from customer_id**
   - Pattern: `CUST-{REGION}-{NUMBER}`
   - Extract region code (US, EU, ASIA, etc.)
   - Create region categorical column

3. **Extract product category hierarchy**
   - Pattern: `{CATEGORY}-{SUBCATEGORY}-{ID}`
   - Extract main category
   - Extract subcategory
   - Create separate columns

4. **Validate email addresses**
   - Build regex pattern for valid email
   - Flag invalid emails
   - Extract email domain

5. **Extract ZIP/postal codes**
   - US ZIP: 5 digits or ZIP+4
   - UK postcode: various formats
   - Extract using appropriate regex patterns

6. **Extract status and dates from order_status**
   - Extract status text (Delivered, Shipped, Processing, Cancelled)
   - Extract embedded dates if present
   - Handle multiple date formats within text

**Concepts Practiced**:
- Basic regex patterns (`\d`, `\w`, `\.`, etc.)
- Character classes `[A-Z]`, `[0-9]`
- Quantifiers `+`, `*`, `{n,m}`
- Groups `( )` and named groups `(?P<name>)`
- `.str.extract()` with groups
- `.str.contains()` with regex
- `.str.replace()` with regex patterns

**Expected Output**: New columns with extracted information

---

### Part 4: Time Series Indexing and Filtering (20 minutes)

**Exercises**:

1. **Set datetime index**
   - Set `transaction_timestamp` as index
   - Sort by datetime

2. **Filter by date ranges**
   - All transactions in 2024
   - Transactions in Q4 2024
   - Last 30 days of data
   - Specific month (e.g., December 2024)

3. **Filter by time of day**
   - Business hours (9 AM - 5 PM)
   - Evening transactions (after 6 PM)
   - Weekend transactions

4. **Advanced filtering**
   - Weekday mornings in Q1 2024
   - Weekend transactions over $100
   - Electronics purchases in December

**Concepts Practiced**:
- Setting datetime index
- Boolean indexing with datetime
- `.between()` for date ranges
- Combining datetime and column filters
- `.dt` accessor for filtering

**Expected Output**: Filtered subsets of data based on time criteria

---

### Part 5: Time Series Aggregation and Resampling (25 minutes)

**Exercises**:

1. **Daily aggregations**
   - Count transactions per day
   - Total revenue per day
   - Average transaction amount per day

2. **Resample to different frequencies**
   - Weekly totals (W)
   - Monthly totals (M)
   - Quarterly totals (Q)
   - Business day frequency (B)

3. **Category-specific aggregations**
   - Daily revenue by product category
   - Monthly transaction count by payment method
   - Weekly average by customer region

4. **Time-based metrics**
   - Peak transaction hour of day
   - Busiest day of week
   - Month-over-month growth rate
   - Compare weekday vs weekend averages

**Concepts Practiced**:
- `.resample()` with frequency codes
- Aggregation functions (sum, mean, count, std)
- `.groupby()` with datetime components
- Multi-level aggregations
- Pivot tables with datetime

**Expected Output**: Aggregated time series data at various frequencies

---

### Part 6: Rolling Windows and Time Shifts (20 minutes)

**Exercises**:

1. **Calculate rolling averages**
   - 7-day rolling average of daily revenue
   - 30-day rolling average of transaction count
   - 14-day rolling standard deviation

2. **Lag and lead operations**
   - Previous day's revenue
   - Next day's transaction count
   - Compare with previous week

3. **Period-over-period calculations**
   - Day-over-day change
   - Week-over-week growth
   - Month-over-month percentage change

4. **Trend identification**
   - Calculate 7-day moving average and compare to daily values
   - Identify days above/below trend
   - Find local maxima and minima

**Concepts Practiced**:
- `.rolling()` with window sizes
- `.shift()` for lagging and leading
- `.pct_change()` for percentage changes
- Window functions (mean, sum, std, min, max)
- Combining rolling and shift operations

**Expected Output**: Time series with trend indicators and comparisons

---

### Part 7: Integrated Analysis (25 minutes)

**Exercises**:

1. **Customer segmentation**
   - Extract customer region from customer_id
   - Calculate metrics by region and time period
   - Identify top regions by growth rate

2. **Product performance analysis**
   - Extract product categories from product codes
   - Analyze sales trends by category over time
   - Find best-performing categories by month

3. **Email campaign validation**
   - Identify customers with valid emails
   - Group by email domain
   - Analyze purchase patterns by domain type

4. **Shipping analysis**
   - Extract ZIP codes from addresses
   - Group by region
   - Analyze delivery times by region

5. **Comprehensive business report**
   - Combine all cleaning and extraction steps
   - Create pivot table: Category × Month with revenue
   - Identify seasonal trends
   - Highlight key insights

**Concepts Practiced**:
- Chaining datetime and string operations
- Complex groupby with multiple keys
- Pivot tables with cleaned data
- Data visualization preparation
- Real-world analytical workflow

**Expected Output**: Business insights and clean analytical dataset

---

## Notebook Delivery Format

### Student Version (unsolved)
**File**: `datetime_regex_practice.ipynb`

**Structure**:
- Markdown cells with instructions
- Empty code cells for student solutions
- Expected output examples (screenshots or descriptions)
- Hints for challenging problems
- Data validation checks (students can run to check answers)

### Solution Version
**File**: `datetime_regex_practice_SOLVED.ipynb`

**Structure**:
- Complete solutions for all exercises
- Detailed comments explaining each step
- Alternative approaches where applicable
- Performance tips and best practices
- Common pitfalls to avoid

---

## Supporting Materials

### 1. Data Dictionary (`data_dictionary.md`)

Complete description of:
- Each column in the dataset
- Expected formats
- Known data quality issues
- Business context

### 2. Regex Cheat Sheet (`regex_cheat_sheet.md`)

Quick reference for:
- Common regex patterns
- Metacharacters
- Character classes
- Quantifiers
- Groups and captures
- Examples from the homework

### 3. Datetime Cheat Sheet (`datetime_cheat_sheet.md`)

Quick reference for:
- Common datetime operations
- Frequency codes
- Format strings
- Timezone handling
- Examples from the homework

---

## Assessment Rubric

### Technical Skills (70 points)

**Datetime Operations (30 points)**
- Parsing and conversion (10 pts)
- Filtering and indexing (8 pts)
- Aggregation and resampling (7 pts)
- Rolling windows and shifts (5 pts)

**String Operations (25 points)**
- Cleaning and standardization (8 pts)
- Regex pattern matching (10 pts)
- Information extraction (7 pts)

**Integration (15 points)**
- Combining techniques (8 pts)
- Real-world application (7 pts)

### Code Quality (20 points)
- Readability and organization (7 pts)
- Proper pandas methods usage (7 pts)
- Comments and documentation (6 pts)

### Analysis and Insights (10 points)
- Correct interpretation (5 pts)
- Business relevance (5 pts)

---

## Implementation Timeline

### Week 1: Data Generation
- **Day 1-2**: Write data generation script
- **Day 3**: Generate and validate dataset
- **Day 4**: Create data dictionary
- **Day 5**: Review and refinement

### Week 2: Notebook Development
- **Day 1-2**: Create notebook structure and Part 1-3
- **Day 3-4**: Create Part 4-6
- **Day 5**: Create Part 7 (integrated analysis)

### Week 3: Solution and Testing
- **Day 1-2**: Complete solution notebook
- **Day 3**: Test all exercises
- **Day 4**: Create cheat sheets and supporting materials
- **Day 5**: Final review and adjustments

---

## Expected Student Outcomes

After completing this homework, students will be able to:

1. **Handle messy real-world data** with confidence
2. **Apply datetime operations** to extract insights from time series
3. **Use regex effectively** for pattern matching and extraction
4. **Clean and standardize** text data efficiently
5. **Combine multiple techniques** to solve complex problems
6. **Perform business analytics** using pandas
7. **Write efficient, readable code** following best practices
8. **Validate and quality-check** their own work

---

## Estimated Completion Time

- **Fast students**: 2-3 hours
- **Average students**: 3-4 hours
- **Struggling students**: 4-5 hours

**Recommendation**: Assign as 1-week homework or 2-session in-class activity

---

## Extensions for Advanced Students

For students who finish early or want extra challenges:

1. **Performance optimization**: Vectorize any remaining loops
2. **Data visualization**: Create plots for time series trends
3. **Advanced regex**: Use lookahead/lookbehind assertions
4. **Custom functions**: Write reusable functions for common tasks
5. **Error handling**: Add try-except blocks for robust code
6. **Additional analysis**: Find more insights in the data

---

## Files to Create

### Primary Files
1. `generate_ecommerce_data.py` - Data generation script
2. `ecommerce_transactions.csv` - Generated dataset
3. `datetime_regex_practice.ipynb` - Student version
4. `datetime_regex_practice_SOLVED.ipynb` - Solution version

### Supporting Files
5. `data_dictionary.md` - Column descriptions
6. `regex_cheat_sheet.md` - Regex quick reference
7. `datetime_cheat_sheet.md` - Datetime quick reference
8. `README.md` - Instructions for students

### Optional Files
9. `test_solutions.py` - Automated solution checker
10. `hints.md` - Additional hints for stuck students

---

## Folder Structure

```
pda1/homework/
├── datetime_regex_practice/
│   ├── README.md
│   ├── data/
│   │   ├── ecommerce_transactions.csv
│   │   └── data_dictionary.md
│   ├── notebooks/
│   │   ├── datetime_regex_practice.ipynb
│   │   └── datetime_regex_practice_SOLVED.ipynb
│   ├── resources/
│   │   ├── regex_cheat_sheet.md
│   │   ├── datetime_cheat_sheet.md
│   │   └── hints.md
│   └── scripts/
│       ├── generate_ecommerce_data.py
│       └── test_solutions.py (optional)
```

---

## Next Steps

1. ✅ **Complete this plan document**
2. ⬜ Review plan with instructor/team
3. ⬜ Create data generation script
4. ⬜ Generate and validate dataset
5. ⬜ Create student notebook (unsolved)
6. ⬜ Create solution notebook
7. ⬜ Create supporting materials
8. ⬜ Test with sample students
9. ⬜ Refine based on feedback
10. ⬜ Finalize and deploy

---

## Success Criteria

This homework will be considered successful if:

- ✅ Students can complete 80%+ of exercises independently
- ✅ Student feedback indicates high learning value
- ✅ Clear progression from basic to advanced concepts
- ✅ Realistic business context maintains engagement
- ✅ Data quality issues are realistic and instructive
- ✅ Solutions demonstrate best practices
- ✅ Time requirement matches target (3-4 hours)

---

## Notes and Considerations

### Pedagogical Approach
- **Scaffolding**: Start simple, build complexity gradually
- **Contextualization**: Every exercise tied to business need
- **Active learning**: Students discover solutions, not just apply formulas
- **Reflection**: Encourage students to think about when/why to use techniques

### Common Student Challenges to Address
- Regex syntax can be intimidating → provide clear examples
- Datetime parsing errors → show error handling strategies
- Chaining operations → demonstrate step-by-step approach
- Debugging → teach how to inspect intermediate results

### Alternative Scenarios (if needed)
- Healthcare appointments data
- Social media post analytics
- Airline flight records
- Hotel booking system
- Financial transaction logs

---

**Plan prepared**: January 2026  
**Target deployment**: PDA2 Course  
**Estimated preparation time**: 15-20 hours  
**Student completion time**: 3-4 hours
