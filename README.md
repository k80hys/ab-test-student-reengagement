# 🎓 A/B Test Framework: Student Re-Engagement via Email Outreach

This project demonstrates a **theoretical A/B testing framework** designed to analyze the impact of personalized email outreach on student re-engagement and re-enrollment. It simulates how an education technology company might structure a data-driven experiment targeting students who have stopped out of college.

---

## 💡 Project Overview

- **Objective:** Determine whether personalized emails increase student engagement and re-enrollment rates.
- **Approach:** Simulate student data, assign A/B groups, and track their progress through a 3-step funnel: 
  - Link Click → Call Booking → Re-Enrollment
- **Tools:** Python, pandas, seaborn, matplotlib, scipy

---

## 📁 Project Structure
AB_test_project/
- dataset.py # Simulates student data and writes CSV
- ab_test.py # Performs funnel analysis and statistical testing
- ab_visualization.py # Generates funnel conversion chart
- ab_test_student_outreach.csv # Simulated dataset
- requirements.txt # Python packages used
- .gitignore # Excludes venv, cache, etc.
- README.md # Project description

---

## 📊 Key Features

- 🧪 **A/B Experiment Design**  
  Simulates two groups:  
  - **Group A (Control):** Standard email  
  - **Group B (Test):** Personalized email  

- 🧬 **Synthetic Data Generation**  
  Generates attributes like age, major, credits completed, and enrollment status using `numpy` and `pandas`.

- 📈 **Funnel Metrics Calculated**
  - Click-through Rate (CTR)
  - Booking Rate (from clicks)
  - Re-Enrollment Rate (from bookings)

- 📉 **Statistical Significance Testing**  
  - Uses Chi-Square tests to evaluate if group differences are statistically significant.

- 📊 **Data Visualization**  
  - Creates a funnel-style stacked bar chart comparing both groups across each stage.

---

## 🧪 Sample Theoretical Results

| Metric             | Group A (Standard Email) | Group B (Personalized Email) |
|--------------------|--------------------------|-------------------------------|
| Click-Through Rate | 24.6%                    | 29.3%                         |
| Booking Rate       | 45.0%                    | 44.0%                         |
| Re-Enrollment Rate | 63.0%                    | 48.5%                         |

> 🔍 These results suggest that personalized emails may drive more initial engagement (clicks), but further analysis would be needed to understand downstream effects.

---

## 📦 Requirements

To install the necessary Python libraries:

```bash
pip install -r requirements.txt
```

## 🚀 How to Run

- Clone this repo
- Run dataset.py to generate the CSV
- Run ab_test.py to analyze the dataset
- Run ab_visualization.py to generate the funnel chart

## 📌 Notes

- This is a theoretical project created for portfolio purposes and does not reflect real student data.
- Inspired by challenges in education technology related to student retention and re-enrollment.
