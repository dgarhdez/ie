# Session Context

## Project: PDA1 Course Restructuring

### Objective
Restructure the PDA1 course with a new session order, more practice sessions, and comprehensive homework/exercise materials.

---

## Completed Tasks

### 1. Created Plan Document
- **File**: `/Users/dgh/Desktop/pda_mbads/plan.md`
- Contains full restructuring plan with:
  - Current vs proposed structure comparison
  - Rationale for changes
  - Notebook inventory
  - Implementation tasks

### 2. Created New Syllabus
- **File**: `/Users/dgh/Desktop/pda_mbads/pda1_test/syllabus.md`
- 20 sessions restructured into:
  - Block 1: Python Fundamentals (S01-S12)
  - Block 2: Pandas for Data Analytics (S13-S20)

### 3. Created Block 1 Notebooks (12/12)

| Session | File | Source |
|---------|------|--------|
| S01 | s01_variables_and_types.ipynb | Migrated from pda1 |
| S02 | s02_practice.ipynb | Migrated from pda1 |
| S03 | s03_data_structures_lists_tuples.ipynb | Migrated from pda1/s04, title updated |
| S04 | s04_data_structures_dicts_sets.ipynb | Migrated from pda1/s05, title updated |
| S05 | s05_strings.ipynb | Migrated from pda1/s03, title updated |
| S06 | s06_practice.ipynb | Migrated from pda1 |
| S07 | s07_conditionals.ipynb | Migrated from pda1 |
| S08 | s08_loops.ipynb | Migrated from pda1/s08, title updated |
| S09 | s09_practice_comprehensions.ipynb | **NEW** - Practice introducing comprehensions |
| S10 | s10_functions.ipynb | Migrated from pda1 |
| S11 | s11_practice.ipynb | **NEW** - Flow control and functions practice |
| S12 | **MIDTERM EXAM** | Exam covering S01-S10 |

### 4. Created Block 2 Notebooks (8/8) ✅

| Session | File | Description |
|---------|------|-------------|
| S13 | s13_pandas_intro_reading.ipynb | Intro to Pandas + Reading Data |
| S14 | s14_practice_pandas_basics.ipynb | Practice - Pandas Basics |
| S15 | s15_pandas_filtering_aggregation.ipynb | Filtering + Aggregation |
| S16 | s16_practice_data_manipulation.ipynb | Practice - Data Manipulation |
| S17 | s17_pandas_combining_quality.ipynb | Combining + Data Quality |
| S18 | s18_practice_cleaning_merging.ipynb | Practice - Cleaning and Merging |
| S19 | s19_final_practice_100_exercises.ipynb | **UPDATED** - 95 comprehensive exercises |
| S19 | s19_final_practice_100_exercises_solved.ipynb | **UPDATED** - Solved version |
| S20 | s20_final_exam/ | Folder created for exam materials |

### 5. Created Homework Notebooks (20/20) ✅

All 10 lecture sessions now have homework and solved versions:

| Session | Homework File | Solved File |
|---------|--------------|-------------|
| S01 | s01_variables_homework.ipynb | s01_variables_homework_solved.ipynb |
| S03 | s03_data_structures_1_homework.ipynb | s03_data_structures_1_homework_solved.ipynb |
| S04 | s04_data_structures_2_homework.ipynb | s04_data_structures_2_homework_solved.ipynb |
| S05 | s05_strings_homework.ipynb | s05_strings_homework_solved.ipynb |
| S07 | s07_conditionals_homework.ipynb | s07_conditionals_homework_solved.ipynb |
| S08 | s08_loops_homework.ipynb | s08_loops_homework_solved.ipynb |
| S10 | s10_functions_homework.ipynb | s10_functions_homework_solved.ipynb |
| S13 | s13_pandas_intro_homework.ipynb | s13_pandas_intro_homework_solved.ipynb |
| S15 | s15_pandas_filtering_homework.ipynb | s15_pandas_filtering_homework_solved.ipynb |
| S17 | s17_pandas_combining_homework.ipynb | s17_pandas_combining_homework_solved.ipynb |

### 6. Created Midterm Exam ✅

- **File**: `pda1_test/exams/midterm_exam.ipynb`
- 6 substantial implementation exercises (12 points scaled to 10)
- Covers S01-S10 concepts
- Progressive difficulty to ensure 90% of students pass (5/10 points)

---

## Remaining Tasks

### 1. S20 - Final Exam Materials
- Folder created: `s20_final_exam/`
- Exam content TBD (to be designed based on course coverage)

### 2. Optional: Rename S19 notebooks
- Current files still named `s19_final_practice_100_exercises*.ipynb`
- Could rename to `s19_final_practice_95_exercises*.ipynb` for consistency

---

## New Course Structure Summary

### Block 1: Python Fundamentals (Sessions 1-12)

| Session | Topic | Format | Homework |
|---------|-------|--------|----------|
| 1 | Variables, Types, and Basic Operations | Lecture | ✅ |
| 2 | Practice: Variables and Operations | Hands-on | - |
| 3 | Data Structures I: Lists and Tuples | Lecture | ✅ |
| 4 | Data Structures II: Dictionaries and Sets | Lecture | ✅ |
| 5 | Strings and Text Processing | Lecture | ✅ |
| 6 | Practice: Data Structures and Strings | Hands-on | - |
| 7 | Conditionals and Boolean Logic | Lecture | ✅ |
| 8 | Loops and Iteration | Lecture | ✅ |
| 9 | Practice: Conditionals, Loops, and Comprehensions | Hands-on | - |
| 10 | Functions and Code Organization | Lecture | ✅ |
| 11 | Practice: Flow Control and Functions | Hands-on | - |
| 12 | **MIDTERM EXAM** | Exam | - |

### Block 2: Pandas for Data Analytics (Sessions 13-20)

| Session | Topic | Format | Homework |
|---------|-------|--------|----------|
| 13 | Introduction to Pandas and Reading Data | Lecture | ✅ |
| 14 | Practice: Pandas Basics | Hands-on | - |
| 15 | Filtering, Selecting, and Aggregation | Lecture | ✅ |
| 16 | Practice: Data Manipulation | Hands-on | - |
| 17 | Combining DataFrames and Data Quality | Lecture | ✅ |
| 18 | Practice: Data Cleaning and Merging | Hands-on | - |
| 19 | Final Practice: 95 Comprehensive Exercises | Hands-on | - |
| 20 | **FINAL EXAM** | Exam | - |

---

## Key Design Decisions

1. **Strings moved after Data Structures** (S5 instead of S3)
   - Students learn indexing/slicing on lists first, then apply to strings

2. **Comprehensions introduced through practice** (S9)
   - After loops lecture, practice session introduces comprehensions hands-on

3. **Mid-term exam restored** (S12)
   - Covers S01-S10 Python fundamentals
   - 6 substantial implementation exercises
   - Designed so 90% of students achieve 5/10 points

4. **Pandas restructured with interleaved practice**
   - 3 lecture sessions with practice sessions between each
   - More hands-on time for complex concepts

5. **95 exercises final practice** (S19)
   - Comprehensive review before final exam
   - File I/O exercises removed (topic no longer in course)

---

## Folder Structure

```
pda1_test/
├── syllabus.md
├── notebooks/
│   ├── s01_variables_and_types.ipynb
│   ├── s02_practice.ipynb
│   ├── s03_data_structures_lists_tuples.ipynb
│   ├── s04_data_structures_dicts_sets.ipynb
│   ├── s05_strings.ipynb
│   ├── s06_practice.ipynb
│   ├── s07_conditionals.ipynb
│   ├── s08_loops.ipynb
│   ├── s09_practice_comprehensions.ipynb
│   ├── s10_functions.ipynb
│   ├── s11_practice.ipynb
│   ├── s13_pandas_intro_reading.ipynb
│   ├── s14_practice_pandas_basics.ipynb
│   ├── s15_pandas_filtering_aggregation.ipynb
│   ├── s16_practice_data_manipulation.ipynb
│   ├── s17_pandas_combining_quality.ipynb
│   ├── s18_practice_cleaning_merging.ipynb
│   ├── s19_final_practice_100_exercises.ipynb ✅
│   ├── s19_final_practice_100_exercises_solved.ipynb ✅
│   └── s20_final_exam/ ✅
├── homework/ ✅ (20 notebooks)
│   ├── s01_variables_homework.ipynb
│   ├── s01_variables_homework_solved.ipynb
│   ├── s03_data_structures_1_homework.ipynb
│   ├── s03_data_structures_1_homework_solved.ipynb
│   ├── s04_data_structures_2_homework.ipynb
│   ├── s04_data_structures_2_homework_solved.ipynb
│   ├── s05_strings_homework.ipynb
│   ├── s05_strings_homework_solved.ipynb
│   ├── s07_conditionals_homework.ipynb
│   ├── s07_conditionals_homework_solved.ipynb
│   ├── s08_loops_homework.ipynb
│   ├── s08_loops_homework_solved.ipynb
│   ├── s10_functions_homework.ipynb
│   ├── s10_functions_homework_solved.ipynb
│   ├── s13_pandas_intro_homework.ipynb
│   ├── s13_pandas_intro_homework_solved.ipynb
│   ├── s15_pandas_filtering_homework.ipynb
│   ├── s15_pandas_filtering_homework_solved.ipynb
│   ├── s17_pandas_combining_homework.ipynb
│   └── s17_pandas_combining_homework_solved.ipynb
├── data/
└── exams/
    ├── midterm_exam.ipynb ✅
    └── midterm_exam_solved.ipynb ✅
```

---

## Notes

- All notebooks use standard Jupyter format (.ipynb)
- Naming convention: `s##_topic_name.ipynb`
- Practice sessions have exercises with empty code cells
- Lecture sessions include inline practice at the end
- Solved versions use `_solved` suffix
- S19 contains 95 exercises covering all course topics (File I/O removed)
- Homework notebooks have 7-8 exercises each with a bonus exercise

---

## Session Log

### Session: 2026-01-31

**Tasks Completed:**

1. **Created S19 Final Practice Notebooks**
   - `s19_final_practice_100_exercises.ipynb` - 100 exercises (unsolved)
   - `s19_final_practice_100_exercises_solved.ipynb` - Complete solutions
   - Exercise distribution:
     - Variables and Types: 8
     - Lists and Tuples: 10
     - Dictionaries and Sets: 10
     - Strings: 8
     - Conditionals: 8
     - Loops: 10
     - Comprehensions: 8
     - Functions: 10
     - File I/O: 5
     - Pandas Basics: 8
     - Filtering and Selecting: 5
     - Aggregation and Grouping: 5
     - Combining DataFrames: 3
     - Data Quality: 2

2. **Created S20 Final Exam Folder**
   - Created `pda1_test/notebooks/s20_final_exam/`
   - Exam content to be designed

3. **Created All 22 Homework Notebooks**
   - Location: `pda1_test/homework/`
   - 11 pairs (unsolved + solved) for lecture sessions:
     - S01: Variables (7 exercises + bonus)
     - S03: Lists/Tuples (7 exercises + bonus)
     - S04: Dicts/Sets (7 exercises + bonus)
     - S05: Strings (7 exercises + bonus)
     - S07: Conditionals (7 exercises + bonus)
     - S08: Loops (8 exercises + bonus)
     - S10: Functions (8 exercises + bonus)
     - S12: File I/O (7 exercises + bonus)
     - S13: Pandas Intro (7 exercises + bonus)
     - S15: Pandas Filtering (7 exercises + bonus)
     - S17: Pandas Combining (7 exercises + bonus)

**Files Created This Session:**
```
pda1_test/notebooks/
├── s19_final_practice_100_exercises.ipynb
├── s19_final_practice_100_exercises_solved.ipynb
└── s20_final_exam/

pda1_test/homework/
├── s01_variables_homework.ipynb
├── s01_variables_homework_solved.ipynb
├── s03_data_structures_1_homework.ipynb
├── s03_data_structures_1_homework_solved.ipynb
├── s04_data_structures_2_homework.ipynb
├── s04_data_structures_2_homework_solved.ipynb
├── s05_strings_homework.ipynb
├── s05_strings_homework_solved.ipynb
├── s07_conditionals_homework.ipynb
├── s07_conditionals_homework_solved.ipynb
├── s08_loops_homework.ipynb
├── s08_loops_homework_solved.ipynb
├── s10_functions_homework.ipynb
├── s10_functions_homework_solved.ipynb
├── s12_file_io_homework.ipynb
├── s12_file_io_homework_solved.ipynb
├── s13_pandas_intro_homework.ipynb
├── s13_pandas_intro_homework_solved.ipynb
├── s15_pandas_filtering_homework.ipynb
├── s15_pandas_filtering_homework_solved.ipynb
├── s17_pandas_combining_homework.ipynb
└── s17_pandas_combining_homework_solved.ipynb
```

**Status:** All planned materials complete except S20 final exam content

---

### Session: 2026-01-31 (Midterm Addition)

**Tasks Completed:**

1. **Added Midterm Exam**
   - S12 changed from "File I/O" to "Midterm Exam"
   - Created `pda1_test/exams/midterm_exam.ipynb`
   - 6 substantial implementation exercises:
     - Exercise 1 (1.5 pts): Sales Commission Calculator
     - Exercise 2 (1.5 pts): Product Inventory Management
     - Exercise 3 (2 pts): Customer Segmentation
     - Exercise 4 (2 pts): Log File Parser
     - Exercise 5 (2 pts): Grade Analysis System
     - Exercise 6 (3 pts): E-Commerce Order Processor
   - Total: 12 points scaled to 10
   - Progressive difficulty designed so 90% achieve 5/10

2. **Removed File I/O Materials**
   - Deleted `s12_file_io.ipynb`
   - Deleted `s12_file_io_homework.ipynb` and solved version
   - File I/O section removed from S19 exercises

3. **Updated S19 Final Practice**
   - Reduced from 100 to 95 exercises
   - Removed File I/O section (exercises 73-77)
   - Renumbered remaining sections

4. **Updated Syllabus**
   - S12 now shows Midterm Exam
   - Assessment structure updated with midterm
   - Homework count reduced to 10

**Files Modified:**
- `pda1_test/syllabus.md` - Updated course structure
- `pda1_test/notebooks/s19_final_practice_100_exercises.ipynb` - Now 95 exercises
- `pda1_test/notebooks/s19_final_practice_100_exercises_solved.ipynb` - Now 95 exercises

**Files Created:**
- `pda1_test/exams/midterm_exam.ipynb`

**Files Deleted:**
- `pda1_test/notebooks/s12_file_io.ipynb`
- `pda1_test/homework/s12_file_io_homework.ipynb`
- `pda1_test/homework/s12_file_io_homework_solved.ipynb`

**Status:** All materials complete except S20 final exam content

---

### Session: 2026-01-31 (Midterm Solutions)

**Tasks Completed:**

1. **Added Self-Check Solutions to Midterm Exam**
   - Updated `pda1_test/exams/midterm_exam.ipynb`
   - Each exercise now has collapsible "Expected Output" section
   - Uses `<details>` HTML tags for click-to-reveal functionality
   - Includes calculation breakdowns for verification

2. **Created Midterm Exam Solved Version**
   - Created `pda1_test/exams/midterm_exam_solved.ipynb`
   - Complete working solutions for all 6 exercises
   - Ready for instructor reference

**Files Created:**
- `pda1_test/exams/midterm_exam_solved.ipynb`

**Files Modified:**
- `pda1_test/exams/midterm_exam.ipynb` - Added expected outputs

**Status:** All materials complete except S20 final exam content

---

### Session: 2026-01-31 (Midterm Revision)

**Tasks Completed:**

1. **Revised Midterm Exam to Match PDA1 Style**
   - Completely rewrote both `midterm_exam.ipynb` and `midterm_exam_solved.ipynb`
   - New format matches the wine exam from pda1/exams/mid_term/
   - Single dataset approach (movies.json) instead of multiple separate datasets
   - Simpler, 1-point questions (12 questions total) instead of complex multi-step exercises
   - 80 minute duration
   - Questions build on each other with unlock mechanism

2. **Created Movies Dataset**
   - Created `movies.json` with 1000 movie entries
   - Fields: title, year, genre, director, rating, votes, runtime, country, language, budget, revenue
   - Includes None values for budget (~20%) and revenue (~25%)
   - Good variety in genres, countries, and decades
   - Suitable for all exam question types

**New Exam Structure:**

| Question | Topic | Points |
|----------|-------|--------|
| 0 | Load JSON data | - (given) |
| 1 | Count items in list | 1 |
| 2 | Add new key to dictionaries | 1 |
| 3 | Count unique values (sets) | 1 |
| 4 | Build count dictionary | 1 |
| 5 | Build average dictionary | 1 |
| 6 | Find max in dictionary | 1 |
| 7 | Create derived field (decade) | 1 |
| 8 | Calculate percentage | 1 |
| 9 | Create two functions | 1 |
| 10 | Analytics (max values) | 1 |
| 11 | Lambda + filter | 1 |
| 12 | Group analysis | 1 |
| **Total** | | **12** |

**Files Modified:**
- `pda1_test/exams/midterm_exam.ipynb` - Complete rewrite
- `pda1_test/exams/midterm_exam_solved.ipynb` - Complete rewrite

**Files Created:**
- `pda1_test/exams/movies.json` - 1000 movies dataset

**Key Differences from Previous Version:**
- Changed from enterprise-style scenarios to data analysis with single dataset
- Reduced complexity significantly (no log parsing, order validation, etc.)
- More aligned with course content (JSON, loops, dictionaries, sets, functions, lambda)
- Better match to pda1 wine exam difficulty level
