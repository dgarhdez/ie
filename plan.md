# PDA1 Course Restructuring Plan

## Current Structure Analysis

### Existing Syllabus (20 sessions)

**Block 1: Python Fundamentals (Sessions 1-13)**
1. Variables and Types
2. Practice
3. String Operations
4. Data Structures I (Lists, Tuples, Sets)
5. Data Structures II (Dictionaries, Range, Zip, Enumerate)
6. Practice
7. Flow Control I (Conditionals)
8. Flow Control II (Loops)
9. Python Comprehensions
10. Practice
11. Functions (including Lambda, Map, Filter, Reduce)
12. Practice (Exam prep)
13. **MID-TERM EXAM**

**Block 2: Pandas for Data Analytics (Sessions 14-20)**
14. Introduction to Pandas
15. Reading Files, Aggregation and Grouping
16. Putting Together Several DataFrames (Join, Merge, Concat)
17. Data Quality with Pandas
18. Practice
19. **GROUP ASSIGNMENT PRESENTATION**
20. **FINAL EXAM**

### Issues Identified

1. **Strings before Data Structures**: Students learn string slicing/indexing before seeing it applied to lists, which can feel disconnected
2. **Comprehensions separated from loops**: These are tightly coupled concepts that benefit from being taught together
3. **Functions too late**: Functions are foundational and should appear earlier to enable better practice exercises
4. **Heavy Block 1, Light Block 2**: 13 sessions for fundamentals vs only 7 for Pandas (including exams/presentations)
5. **Practice sessions not evenly distributed**: Some concepts get dedicated practice, others don't
6. **Missing file I/O in Block 1**: Students should learn basic file operations before Pandas
7. **Too much Pandas content without practice**: Students need hands-on time between concepts

---

## Proposed New Structure

### Design Principles

1. **Comprehensions through practice**: Introduce comprehensions in a practice session after loops, reinforcing the connection
2. **Balanced practice**: Practice sessions after every 2-3 lecture sessions
3. **I/O before Pandas**: Dedicated session for file operations and context managers
4. **Pandas with practice**: Alternate between lecture and practice in Block 2
5. **Homework for reinforcement**: Every lecture session has a homework assignment with solutions
6. **Comprehensive final practice**: 100 exercises covering all course topics

### New Syllabus (20 sessions)

**Block 1: Python Fundamentals (Sessions 1-12)**

| Session | Topic | Format | Homework |
|---------|-------|--------|----------|
| 1 | Variables, Types, and Basic Operations | Lecture + Practice | Yes |
| 2 | Practice: Variables and Operations | Hands-on | - |
| 3 | Data Structures I: Lists and Tuples | Lecture + Practice | Yes |
| 4 | Data Structures II: Dictionaries and Sets | Lecture + Practice | Yes |
| 5 | Strings and Text Processing | Lecture + Practice | Yes |
| 6 | Practice: Data Structures and Strings | Hands-on | - |
| 7 | Conditionals and Boolean Logic | Lecture + Practice | Yes |
| 8 | Loops and Iteration | Lecture + Practice | Yes |
| 9 | Practice: Conditionals, Loops, and Comprehensions | Hands-on | - |
| 10 | Functions and Code Organization | Lecture + Practice | Yes |
| 11 | Practice: Flow Control and Functions | Hands-on | - |
| 12 | File I/O and Context Managers | Lecture + Practice | Yes |

**Block 2: Pandas for Data Analytics (Sessions 13-20)**

| Session | Topic | Format | Homework |
|---------|-------|--------|----------|
| 13 | Introduction to Pandas and Reading Data | Lecture + Practice | Yes |
| 14 | Practice: Pandas Basics | Hands-on | - |
| 15 | Filtering, Selecting, and Aggregation | Lecture + Practice | Yes |
| 16 | Practice: Data Manipulation | Hands-on | - |
| 17 | Combining DataFrames and Data Quality | Lecture + Practice | Yes |
| 18 | Practice: Data Cleaning and Merging | Hands-on | - |
| 19 | Final Practice: 100 Comprehensive Exercises | Hands-on | - |
| 20 | **FINAL EXAM** | Exam | - |

---

## Key Changes Explained

### 1. Moved Strings After Data Structures
**Rationale**: Lists introduce indexing and slicing concepts. When students then see strings, they recognize the same patterns, reinforcing learning.

### 2. Comprehensions Introduced Through Practice (Session 9)
**Rationale**: After learning loops in Session 8, students practice them while being introduced to comprehensions as a more Pythonic alternative. This hands-on approach helps them see when each is appropriate.

### 3. File I/O and Context Managers (Session 12)
**Rationale**: Replaces the mid-term exam. Students learn to read/write files and use context managers (`with` statement) before moving to Pandas. This is essential knowledge for real-world data work.

### 4. Consolidated Pandas Sessions with Interleaved Practice
**Rationale**: Instead of 6 consecutive lecture sessions, Pandas is now taught in 3 focused lectures with practice sessions between each:
- **S13**: Intro + Reading (foundations)
- **S15**: Filtering + Aggregation (core operations)
- **S17**: Combining + Quality (advanced operations)

### 5. Homework Assignments for All Lecture Sessions
**Rationale**: Every lecture session (11 total) includes:
- `sXX_topic_homework.ipynb` - Assignment for students
- `sXX_topic_homework_solved.ipynb` - Solutions for self-checking

### 6. Final Practice with 100 Exercises (Session 19)
**Rationale**: Comprehensive review covering all course topics, preparing students for the final exam.

---

## Folder Structure for pda1_test

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
│   ├── s12_file_io.ipynb
│   ├── s13_pandas_intro_reading.ipynb
│   ├── s14_practice_pandas_basics.ipynb
│   ├── s15_pandas_filtering_aggregation.ipynb
│   ├── s16_practice_data_manipulation.ipynb
│   ├── s17_pandas_combining_quality.ipynb
│   ├── s18_practice_cleaning_merging.ipynb
│   ├── s19_final_practice_100_exercises.ipynb
│   └── s20_final_exam/
├── homework/
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
│   ├── s12_file_io_homework.ipynb
│   ├── s12_file_io_homework_solved.ipynb
│   ├── s13_pandas_intro_homework.ipynb
│   ├── s13_pandas_intro_homework_solved.ipynb
│   ├── s15_pandas_filtering_homework.ipynb
│   ├── s15_pandas_filtering_homework_solved.ipynb
│   ├── s17_pandas_combining_homework.ipynb
│   └── s17_pandas_combining_homework_solved.ipynb
├── data/
└── exams/
    └── s20_final_exam/
```

---

## Notebook Inventory

### Session Notebooks (20)

| Session | Filename | Type |
|---------|----------|------|
| 1 | s01_variables_and_types.ipynb | Lecture |
| 2 | s02_practice.ipynb | Practice |
| 3 | s03_data_structures_lists_tuples.ipynb | Lecture |
| 4 | s04_data_structures_dicts_sets.ipynb | Lecture |
| 5 | s05_strings.ipynb | Lecture |
| 6 | s06_practice.ipynb | Practice |
| 7 | s07_conditionals.ipynb | Lecture |
| 8 | s08_loops.ipynb | Lecture |
| 9 | s09_practice_comprehensions.ipynb | Practice |
| 10 | s10_functions.ipynb | Lecture |
| 11 | s11_practice.ipynb | Practice |
| 12 | s12_file_io.ipynb | Lecture |
| 13 | s13_pandas_intro_reading.ipynb | Lecture |
| 14 | s14_practice_pandas_basics.ipynb | Practice |
| 15 | s15_pandas_filtering_aggregation.ipynb | Lecture |
| 16 | s16_practice_data_manipulation.ipynb | Practice |
| 17 | s17_pandas_combining_quality.ipynb | Lecture |
| 18 | s18_practice_cleaning_merging.ipynb | Practice |
| 19 | s19_final_practice_100_exercises.ipynb | Practice (100 exercises) |
| 20 | s20_final_exam/ | Exam |

### Homework Notebooks (22)

11 lecture sessions x 2 (unsolved + solved) = 22 homework notebooks

| Session | Homework | Solved |
|---------|----------|--------|
| 1 | s01_variables_homework.ipynb | s01_variables_homework_solved.ipynb |
| 3 | s03_data_structures_1_homework.ipynb | s03_data_structures_1_homework_solved.ipynb |
| 4 | s04_data_structures_2_homework.ipynb | s04_data_structures_2_homework_solved.ipynb |
| 5 | s05_strings_homework.ipynb | s05_strings_homework_solved.ipynb |
| 7 | s07_conditionals_homework.ipynb | s07_conditionals_homework_solved.ipynb |
| 8 | s08_loops_homework.ipynb | s08_loops_homework_solved.ipynb |
| 10 | s10_functions_homework.ipynb | s10_functions_homework_solved.ipynb |
| 12 | s12_file_io_homework.ipynb | s12_file_io_homework_solved.ipynb |
| 13 | s13_pandas_intro_homework.ipynb | s13_pandas_intro_homework_solved.ipynb |
| 15 | s15_pandas_filtering_homework.ipynb | s15_pandas_filtering_homework_solved.ipynb |
| 17 | s17_pandas_combining_homework.ipynb | s17_pandas_combining_homework_solved.ipynb |

### Special Notebooks

| Notebook | Description |
|----------|-------------|
| s19_final_practice_100_exercises.ipynb | 100 exercises covering all course topics |
| s19_final_practice_100_exercises_solved.ipynb | Solutions to all 100 exercises |

**Total notebooks to create: 44**
- 20 session notebooks
- 22 homework notebooks (11 pairs)
- 2 final practice notebooks (unsolved + solved)

---

## Implementation Tasks

### Phase 1: Structure Setup
- [x] Create `pda1_test/` directory structure
- [x] Write new `syllabus.md` with detailed session descriptions
- [ ] Update syllabus.md with revised structure

### Phase 2: Block 1 Notebooks (Sessions 1-12)
- [ ] S01: Variables and Types (migrate from existing)
- [ ] S02: Practice (migrate from existing)
- [ ] S03: Data Structures - Lists and Tuples (adapt from existing s04)
- [ ] S04: Data Structures - Dicts and Sets (adapt from existing s05)
- [ ] S05: Strings (adapt from existing s03)
- [ ] S06: Practice (migrate from existing)
- [ ] S07: Conditionals (migrate from existing)
- [ ] S08: Loops (adapt from existing s08)
- [ ] S09: Practice with Comprehensions (new - introduce comprehensions)
- [ ] S10: Functions (adapt from existing s10)
- [ ] S11: Practice (create new)
- [ ] S12: File I/O and Context Managers (new)

### Phase 3: Block 2 Notebooks (Sessions 13-20)
- [ ] S13: Pandas Intro + Reading (consolidate existing content)
- [ ] S14: Practice - Pandas Basics (new)
- [ ] S15: Filtering + Aggregation (consolidate existing content)
- [ ] S16: Practice - Data Manipulation (new)
- [ ] S17: Combining + Data Quality (consolidate existing content)
- [ ] S18: Practice - Cleaning and Merging (new)
- [ ] S19: Final Practice - 100 Exercises (new)
- [ ] S20: Final Exam materials

### Phase 4: Homework Notebooks
- [ ] Create 11 homework notebooks (unsolved)
- [ ] Create 11 homework notebooks (solved)

### Phase 5: Final Practice
- [ ] Create s19_final_practice_100_exercises.ipynb with 100 exercises
- [ ] Create s19_final_practice_100_exercises_solved.ipynb with solutions

---

## Session 9: Comprehensions Through Practice - Outline

This practice session introduces comprehensions while reinforcing loops:

1. **Warm-up**: Loop exercises (5-6 problems)
2. **Introduction to Comprehensions**: Show how loops can be rewritten
3. **List Comprehensions**: Practice converting loops to comprehensions (10 problems)
4. **Conditional Comprehensions**: Adding filters (5 problems)
5. **Dictionary Comprehensions**: Key-value transformations (5 problems)
6. **Set Comprehensions**: Unique values (3 problems)
7. **When to Use What**: Guidelines on choosing loops vs comprehensions
8. **Mixed Practice**: Problems where students choose the best approach (5 problems)

---

## Session 19: 100 Exercises - Topic Distribution

| Block | Topic | # Exercises |
|-------|-------|-------------|
| 1 | Variables and Types | 8 |
| 1 | Data Structures (Lists, Tuples) | 10 |
| 1 | Data Structures (Dicts, Sets) | 10 |
| 1 | Strings | 8 |
| 1 | Conditionals | 8 |
| 1 | Loops | 10 |
| 1 | Comprehensions | 8 |
| 1 | Functions | 10 |
| 1 | File I/O | 5 |
| 2 | Pandas Basics (Series, DataFrame, Reading) | 8 |
| 2 | Filtering and Selecting | 5 |
| 2 | Aggregation and Grouping | 5 |
| 2 | Combining DataFrames | 3 |
| 2 | Data Quality | 2 |
| **Total** | | **100** |

---

## Assessment Structure (Updated)

| Assessment | Type | Content |
|------------|------|---------|
| Homework | Individual | 11 assignments throughout the course |
| Group Assignment | Group | Data analytics project (presented separately) |
| Final Exam (S20) | Individual | Comprehensive Python and Pandas |

*Note: Mid-term exam removed; replaced with homework-based continuous assessment*

---

## Next Steps

1. Review and approve this updated plan
2. Update `pda1_test/syllabus.md` with new structure
3. Begin creating notebooks in phases
4. Start with Block 1, then Block 2, then homework, then final practice
