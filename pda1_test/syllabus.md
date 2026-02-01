# Python for Data Analytics 1 (PDA1) - Course Syllabus

## Course Overview

This course provides a comprehensive introduction to Python programming with a focus on data analytics applications. Students will learn fundamental Python concepts, data manipulation techniques using pandas, and practical problem-solving skills for business applications.

## Course Structure

The course is divided into two main blocks:

- **Block 1**: Python Fundamentals (Sessions 1-11) + Midterm Exam (Session 12)
- **Block 2**: Pandas for Data Analytics (Sessions 13-20)

---

## BLOCK 1: Python Fundamentals

### SESSION 1 (LIVE IN-PERSON) - Variables, Types, and Basic Operations

**Topics Covered:**

- What is a variable and how to create one
- Data types: integers, floats, booleans, strings
- Arithmetic operators (+, -, *, /, //, %, **)
- Comparison operators (==, !=, <, >, <=, >=)
- Logical operators (and, or, not)
- Type conversion and checking

**Format:** Lecture + Practice at the end
**Homework:** s01_variables_homework.ipynb

---

### SESSION 2 (LIVE IN-PERSON) - Practice: Variables and Operations

**Topics Covered:**

- Solving business problems using variables and operations
- Combining different data types
- Building simple calculations for real-world scenarios

**Format:** Hands-on practice session

---

### SESSION 3 (LIVE IN-PERSON) - Data Structures I: Lists and Tuples

**Topics Covered:**

- Introduction to data structures: storing multiple values
- Lists: creation, indexing, slicing, mutability
- List methods: append, extend, insert, remove, pop, sort
- Tuples: creation, indexing, immutability
- When to use lists vs tuples
- Nested structures

**Format:** Lecture + Practice at the end
**Homework:** s03_data_structures_1_homework.ipynb

---

### SESSION 4 (LIVE IN-PERSON) - Data Structures II: Dictionaries and Sets

**Topics Covered:**

- Dictionaries: key-value pairs, creation, access
- Dictionary methods: keys, values, items, get, update
- Sets: unique values, creation, set operations
- Set methods: add, remove, union, intersection, difference
- Choosing the right data structure for the problem

**Format:** Lecture + Practice at the end
**Homework:** s04_data_structures_2_homework.ipynb

---

### SESSION 5 (LIVE IN-PERSON) - Strings and Text Processing

**Topics Covered:**

- String properties and immutability
- String indexing and slicing (applying concepts from lists)
- String methods: upper, lower, strip, split, join, replace, find
- String formatting: f-strings, format method
- Working with text data in business contexts

**Format:** Lecture + Practice at the end
**Homework:** s05_strings_homework.ipynb

---

### SESSION 6 (LIVE IN-PERSON) - Practice: Data Structures and Strings

**Topics Covered:**

- Combining different data structures
- Text processing challenges
- Building data models with dictionaries and lists
- Extracting and transforming information

**Format:** Hands-on practice session

---

### SESSION 7 (LIVE IN-PERSON) - Conditionals and Boolean Logic

**Topics Covered:**

- if, elif, else statements
- Nested conditionals
- Combining conditions with and, or, not
- Ternary expressions
- Truthy and falsy values
- Decision trees in code

**Format:** Lecture + Practice at the end
**Homework:** s07_conditionals_homework.ipynb

---

### SESSION 8 (LIVE IN-PERSON) - Loops and Iteration

**Topics Covered:**

- for loops: iterating over sequences
- The range function
- while loops: condition-based iteration
- Loop control: break, continue, pass
- Nested loops
- Common loop patterns: counting, accumulating, searching

**Format:** Lecture + Practice at the end
**Homework:** s08_loops_homework.ipynb

---

### SESSION 9 (LIVE IN-PERSON) - Practice: Loops and Comprehensions

**Topics Covered:**

- Reinforcing loop concepts through practice
- Introduction to list comprehensions
- Conditional comprehensions
- Dictionary and set comprehensions
- When to use loops vs comprehensions
- The enumerate and zip functions

**Format:** Hands-on practice session (comprehensions introduced through guided practice)

---

### SESSION 10 (LIVE IN-PERSON) - Functions and Code Organization

**Topics Covered:**

- Why functions matter: reusability and organization
- Defining functions with def
- Parameters and arguments
- Return values
- Default parameters and keyword arguments
- Variable scope: local vs global
- Lambda functions and their use cases
- Docstrings and documentation

**Format:** Lecture + Practice at the end
**Homework:** s10_functions_homework.ipynb

---

### SESSION 11 (LIVE IN-PERSON) - Practice: Flow Control and Functions

**Topics Covered:**

- Combining conditionals, loops, and functions
- Building complete solutions to complex problems
- Code organization best practices
- Midterm preparation exercises

**Format:** Hands-on practice session

---

### SESSION 12 (LIVE IN-PERSON) - MIDTERM EXAMINATION

**Format:**

- Live coding in class (90 minutes)
- Open book examination
- Covers: Sessions 1-10 (Python fundamentals)

**Exam Structure:**

| Exercise | Topic | Points |
|----------|-------|--------|
| 1 | Sales Commission Calculator | 1.5 |
| 2 | Product Inventory Management | 1.5 |
| 3 | Customer Segmentation | 2.0 |
| 4 | Log File Parser | 2.0 |
| 5 | Grade Analysis System | 2.0 |
| 6 | E-Commerce Order Processor | 3.0 |
| **Total** | | **12.0** (scaled to 10) |

**Important Policies:**

- **NO AI ALLOWED**: No Copilot, no Gemini, no ChatGPT, or any AI assistance
- **IMPORTANT**: Usage of AI will result in immediate course failure

---

## BLOCK 2: Pandas for Data Analytics

**Block Overview:**

Building and operating with tabular data for real-world analytics applications. This block alternates between lecture sessions and practice sessions to reinforce learning.

---

### SESSION 13 (LIVE IN-PERSON) - Introduction to Pandas and Reading Data

**Topics Covered:**

- What is pandas and why use it
- Installing and importing pandas
- Series: 1-dimensional labeled data
- DataFrame: 2-dimensional tabular data
- Creating DataFrames from dictionaries and lists
- Basic DataFrame properties: shape, columns, dtypes, info
- Viewing data: head, tail, sample
- Reading CSV files with read_csv
- Reading JSON files with read_json
- Handling common file issues: encoding, separators, headers
- Saving DataFrames: to_csv, to_json

**Format:** Lecture + Practice at the end
**Homework:** s13_pandas_intro_homework.ipynb

---

### SESSION 14 (LIVE IN-PERSON) - Practice: Pandas Basics

**Topics Covered:**

- Creating DataFrames from various sources
- Exploring and understanding datasets
- Basic column operations
- Reading and writing files
- Initial data exploration workflow

**Format:** Hands-on practice session

---

### SESSION 15 (LIVE IN-PERSON) - Filtering, Selecting, and Aggregation

**Topics Covered:**

- Selecting columns by name and position
- Selecting rows with loc and iloc
- Boolean indexing: filtering with conditions
- Combining multiple conditions
- The query method
- Applying functions to columns: apply, map
- Sorting data: sort_values, sort_index
- Basic aggregation functions: sum, mean, count, min, max, std
- The groupby object: split-apply-combine
- Multiple aggregations with agg
- Named aggregations

**Format:** Lecture + Practice at the end
**Homework:** s15_pandas_filtering_homework.ipynb

---

### SESSION 16 (LIVE IN-PERSON) - Practice: Data Manipulation

**Topics Covered:**

- Filtering datasets with complex conditions
- Grouping and aggregating real-world data
- Answering business questions with pandas
- Building analysis pipelines

**Format:** Hands-on practice session

---

### SESSION 17 (LIVE IN-PERSON) - Combining DataFrames and Data Quality

**Topics Covered:**

**Combining DataFrames:**
- Concatenating DataFrames: vertical and horizontal
- The concat function and its parameters
- Merge: combining on common columns
- Types of joins: inner, outer, left, right
- Joining on multiple columns
- When to use concat vs merge

**Data Quality:**
- Checking and converting data types: astype
- Working with categorical data
- Identifying missing values: isnull, notnull
- Handling missing data: dropna, fillna
- Identifying outliers: statistical methods, IQR
- Data validation and consistency checks

**Format:** Lecture + Practice at the end
**Homework:** s17_pandas_combining_homework.ipynb

---

### SESSION 18 (LIVE IN-PERSON) - Practice: Data Cleaning and Merging

**Topics Covered:**

- Combining multiple datasets
- Cleaning messy data
- Handling missing values in context
- End-to-end data preparation workflows

**Format:** Hands-on practice session

---

### SESSION 19 (LIVE IN-PERSON) - Final Practice: Comprehensive Exercises

**Topics Covered:**

A comprehensive review of all course material through exercises:

| Topic | # Exercises |
|-------|-------------|
| Variables and Types | 8 |
| Lists and Tuples | 10 |
| Dictionaries and Sets | 10 |
| Strings | 8 |
| Conditionals | 8 |
| Loops | 10 |
| Comprehensions | 8 |
| Functions | 10 |
| Pandas Basics | 8 |
| Filtering and Selecting | 5 |
| Aggregation and Grouping | 5 |
| Combining DataFrames | 3 |
| Data Quality | 2 |

**Format:** Hands-on practice session (exam preparation)

---

### SESSION 20 (LIVE IN-PERSON) - FINAL EXAM

**Format:**

- Live coding in class
- Open book examination
- Covers: All Python fundamentals + Pandas operations

**Important Policies:**

- **NO AI ALLOWED**: No Copilot, no Gemini, no ChatGPT, or any AI assistance
- **IMPORTANT**: Usage of AI will result in immediate course failure

---

## Assessment Structure

| Assessment | Type | Session | Description |
|------------|------|---------|-------------|
| Homework | Individual | Throughout | 10 assignments for lecture sessions |
| Midterm Exam (S12) | Individual | Session 12 | Python fundamentals (S01-S10) |
| Group Assignment | Group | Separate | Data analytics project |
| Final Exam (S20) | Individual | Session 20 | Comprehensive Python and Pandas |

---

## Learning Outcomes

By the end of this course, students will be able to:

1. **Understand and apply** fundamental Python programming concepts
2. **Create and manipulate** various data structures (lists, dictionaries, sets, tuples)
3. **Write functions** to organize and reuse code effectively
4. **Use pandas** to load, clean, transform, and analyze tabular data
5. **Combine datasets** using joins and merges
6. **Handle data quality issues** including missing values and outliers
7. **Solve business problems** through structured data analysis

---

## Course Materials

### Session Notebooks

Each session has a corresponding Jupyter notebook in the `notebooks/` folder.

### Homework Assignments

Homework is provided for lecture sessions in the `homework/` folder:
- `sXX_topic_homework.ipynb` - Assignment
- `sXX_topic_homework_solved.ipynb` - Solutions

### Exams

Exam materials are in the `exams/` folder:
- `midterm_exam.ipynb` - Midterm examination

### Data Files

Sample datasets are provided in the `data/` folder for practice and homework exercises.

---

## Session Format

- All sessions are **LIVE IN-PERSON**
- Lecture sessions follow **Lecture + Practice** format
- Practice sessions are fully **Hands-on**
- Materials for each session are provided in Jupyter notebooks

---

## Important Policies

### AI Usage Policy

- **STRICTLY PROHIBITED** during examinations (Sessions 12 and 20)
- No AI assistants of any kind are allowed during exams
- Violation results in immediate course failure

### Attendance

- All sessions are live and in-person
- Active participation is expected

### Academic Integrity

- All exam work must be your own
- Collaboration is encouraged during practice sessions
- Group assignments should reflect equal contribution from all members
