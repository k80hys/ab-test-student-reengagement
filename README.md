# A/B Test Student Outreach Analysis

This project analyzes the effectiveness of different email campaigns for student re-enrollment using A/B testing methodology.

## Project Structure

- `dataset.py` - Generates synthetic A/B test data for student email campaigns
- `ab_test.py` - Performs statistical analysis on the A/B test results
- `environment.yml` - Conda environment specification
- `requirements.txt` - Python package dependencies

## Setup with Anaconda

### Option 1: Using Conda Environment (Recommended)

1. **Create the conda environment:**
   ```bash
   conda env create -f environment.yml
   ```

2. **Activate the environment:**
   ```bash
   conda activate ab-test-project
   ```

3. **Run the analysis:**
   ```bash
   python dataset.py  # Generate the data
   python ab_test.py  # Run the A/B test analysis
   ```

### Option 2: Using Base Anaconda Environment

1. **Install required packages:**
   ```bash
   conda install pandas numpy scipy matplotlib seaborn jupyter
   ```

2. **Or install from requirements.txt:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the analysis:**
   ```bash
   python dataset.py  # Generate the data
   python ab_test.py  # Run the A/B test analysis
   ```

### Option 3: Using Jupyter Notebook in Anaconda

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Create a new notebook and run the analysis interactively**

## Data Description

The dataset includes:
- Student demographics (age, major, credits completed)
- Email campaign assignment (Group A vs Group B)
- Conversion funnel metrics:
  - Clicked email link
  - Booked consultation call
  - Successfully re-enrolled

## Analysis Results

The A/B test analyzes:
- Click-through rates between email groups
- Conversion rates at each funnel stage
- Statistical significance using Chi-square tests
- Overall re-enrollment effectiveness

## Deactivating Environment

When finished, deactivate the conda environment:
```bash
conda deactivate
```
