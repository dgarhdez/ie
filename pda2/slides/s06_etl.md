---
marp: true
author: 
  - name: Daniel Garcia
  - email: dgarciah@faculty.ie.edu
  - url: www.linkedin.com/in/dgarhdez
header: ![center width:100px](../../img/ie_logo.png)
size: 16:9
footer: "Programming for Data Analytics II, dgarciah@faculty.ie.edu"
theme: default
math: katex
style: |
    img[alt~="center"] {
      display: block;
      margin: 0 auto;
    }
---

<!-- _color: "rgba(21, 51, 96, 1)" -->

# Programming for Data Analytics II: Session 6

## ETL Pipeline with Pandas

---

## Overview

A simple ETL (Extract, Transform, Load) pipeline using Pandas and CSV files.

---

## Pipeline Architecture

1. **Sources / Raw**: Original data files (CSV).
2. **Staging**: Cleaned data, standardized types.
3. **Intermediate**: Enriched data, joins, business logic.
4. **Marts**: Aggregated data ready for reporting.

---

## 1. Sources / Raw

- **Location**: `data/raw/`
- **Files**:
  - `customers.csv`: Customer details.
  - `products.csv`: Product catalog.
  - `orders.csv`: Transactional data.
- **State**: Raw, potentially messy, untyped.

---

## 2. Staging

- **Location**: `data/staging/`
- **Process**:
  - Read raw CSVs.
  - Convert dates to datetime objects.
  - Standardize column names (if needed).
  - Handle basic data quality issues.
- **Goal**: Prepare data for joining.

---

## 3. Intermediate / Business Logic

- **Location**: `data/intermediate/`
- **Process**:
  - Join `orders` with `customers` and `products`.
  - Calculate derived columns (e.g., `total_amount = quantity * price`).
  - Filter invalid records.
- **Goal**: Create a "Wide Table" or "Enriched" dataset containing all necessary context.

---

## 4. Marts

- **Location**: `data/marts/`
- **Process**:
  - Group by dimensions (Category, Date, Country).
  - Aggregate metrics (Sum of Revenue, Count of Orders).
- **Goal**: Small, focused tables for specific reports or dashboards.

---

## ETL Pipeline Diagram

[center width:100px](../../img/etl.png)

---

## Summary

This pipeline demonstrates how to structure data processing into logical layers, making the code more maintainable, debuggable, and scalable.

---