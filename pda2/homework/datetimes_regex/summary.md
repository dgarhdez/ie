# Datetimes & Regex Operations - Quick Reference

## 1. Datetime Parsing & Conversion

### Parse mixed date formats
```python
df['datetime_col'] = pd.to_datetime(df['string_col'], errors='coerce', infer_datetime_format=True)
```

### Extract datetime components
```python
df['year'] = df['datetime_col'].dt.year
df['month'] = df['datetime_col'].dt.month
df['day'] = df['datetime_col'].dt.day
df['hour'] = df['datetime_col'].dt.hour
df['day_of_week'] = df['datetime_col'].dt.dayofweek  # Monday=0, Sunday=6
df['quarter'] = df['datetime_col'].dt.quarter
df['is_weekend'] = df['day_of_week'].isin([5, 6])
```

### Filter by date ranges
```python
# Check for outliers
df[df['datetime_col'] < pd.Timestamp('2024-01-01')]
df[df['datetime_col'] > pd.Timestamp('2026-01-29')]
```

## 2. String Cleaning

### Basic cleaning
```python
df['clean'] = df['col'].str.strip()  # Remove whitespace
df['clean'] = df['col'].str.lower()  # Convert to lowercase
df['clean'] = df['col'].str.title()  # Title Case
```

### Clean currency/numeric strings
```python
df['numeric'] = df['amount'].str.replace('$', '', regex=False) \
                             .str.replace(',', '', regex=False) \
                             .astype(float)
```

## 3. Regular Expressions

### Extract patterns
```python
# Extract date from ID (TXN-20240315-000123)
df['date'] = df['id'].str.extract(r'TXN-(\d{8})-')

# Extract region (CUST-US-0001)
df['region'] = df['customer_id'].str.extract(r'CUST-(\w+)-')

# Extract category (ELEC-PHONE-1234)
df['category'] = df['product_code'].str.extract(r'^(\w+)-')
df['subcategory'] = df['product_code'].str.extract(r'^\w+-(\w+)-')
```

### Validate patterns
```python
# Email validation
email_pattern = r'^\w+[\w\.]*@\w+\.\w+$'
df['is_valid'] = df['email'].str.match(email_pattern, na=False)

# Extract email domain
df['domain'] = df['email'].str.extract(r'@([\w\.]+)')
```

### Extract postal codes
```python
# US ZIP (5 digits) or UK postcode
postal_pattern = r'(\d{5})|([A-Z]{1,2}\d{1,2}[A-Z]?\s?\d[A-Z]{2})'
extracted = df['address'].str.extract(postal_pattern)
df['postal_code'] = extracted[0].fillna(extracted[1])
```

### Extract keywords
```python
# Extract status
df['status'] = df['status_col'].str.extract(r'(Delivered|Shipped|Processing|Cancelled)', flags=re.IGNORECASE)
```

## 4. Time Series Operations

### Set datetime index
```python
df_ts = df[df['datetime_col'].notna()].copy()
df_ts = df_ts.set_index('datetime_col').sort_index()
```

### Filter by dates
```python
# Entire year
df_ts['2024']

# Quarter
df_ts['2024-10':'2024-12']

# Single month
df_ts['2024-12']

# By hour
df_ts[(df_ts.index.hour >= 9) & (df_ts.index.hour <= 17)]

# Weekend
df_ts[df_ts.index.dayofweek.isin([5, 6])]
```

### Complex filtering
```python
df_ts[(df_ts.index.year == 2024) & 
      (df_ts.index.month == 12) & 
      (df_ts['category'] == 'ELEC')]
```

## 5. Resampling & Aggregation

### Basic resampling
```python
# Daily
df_ts.resample('D').size()  # Count
df_ts['amount'].resample('D').sum()  # Sum
df_ts['amount'].resample('D').mean()  # Average

# Weekly, Monthly, Quarterly
df_ts['amount'].resample('W').sum()
df_ts['amount'].resample('M').sum()
df_ts['amount'].resample('Q').sum()
```

### Group with time period
```python
# Monthly revenue by category
df_ts.groupby([pd.Grouper(freq='M'), 'category'])['amount'].sum()
```

### Time-based metrics
```python
# Hourly distribution
df_ts.groupby(df_ts.index.hour).size()

# Day of week distribution
df_ts.groupby(df_ts.index.dayofweek).size()
```

## 6. Rolling Windows & Shifts

### Rolling calculations
```python
daily = df_ts['amount'].resample('D').sum()

# Rolling average
daily.rolling(window=7).mean()
daily.rolling(window=30).mean()

# Rolling standard deviation
daily.rolling(window=7).std()
```

### Lag operations
```python
# Previous period
daily.shift(1)  # Previous day
daily.shift(7)  # 7 days ago

# Change calculations
daily - daily.shift(1)  # Day-over-day change
daily.pct_change() * 100  # Percentage change
```

### Trend analysis
```python
rolling_avg = daily.rolling(window=7).mean()
above_trend = daily > rolling_avg
```

## 7. Common Patterns

### Categorize time of day
```python
def categorize_time(hour):
    if pd.isna(hour):
        return None
    if 6 <= hour <= 11:
        return 'morning'
    elif 12 <= hour <= 17:
        return 'afternoon'
    elif 18 <= hour <= 22:
        return 'evening'
    else:
        return 'night'

df['time_of_day'] = df['hour'].apply(categorize_time)
```

### Categorize payment methods
```python
def categorize_payment(payment):
    if pd.isna(payment):
        return 'unknown'
    payment_lower = payment.lower()
    if 'credit' in payment_lower:
        return 'credit_card'
    elif 'debit' in payment_lower:
        return 'debit_card'
    elif any(w in payment_lower for w in ['paypal', 'apple pay', 'google pay']):
        return 'digital_wallet'
    return 'other'

df['payment_category'] = df['payment_method'].apply(categorize_payment)
```

## 8. Key Imports

```python
import pandas as pd
import numpy as np
import re
from datetime import datetime, timedelta
```

## Quick Regex Cheat Sheet

- `\d` - digit (0-9)
- `\w` - word character (a-z, A-Z, 0-9, _)
- `\s` - whitespace
- `^` - start of string
- `$` - end of string
- `+` - one or more
- `*` - zero or more
- `{n}` - exactly n times
- `{n,m}` - between n and m times
- `(...)` - capture group
- `[...]` - character class
- `|` - alternation (OR)
