import pandas as pd
import scipy.stats as stats

# Step 1: Load the CSV
df = pd.read_csv("ab_test_student_outreach.csv")

# Step 2: Basic exploration
print(df['email_group'].value_counts())
print(df.head())

# Step 3: Calculate conversion rates
summary = df.groupby('email_group')[['clicked_link', 'booked_call', 'reenrolled']].mean().round(3)
print("\n📊 Conversion Rates by Group:")
print(summary * 100)  # Show as percentages

# Step 4: Build contingency table for Chi-Square Test
# Example: A/B test on clicked_link (click-through rate)
contingency_clicks = pd.crosstab(df['email_group'], df['clicked_link'])
print("\n🧮 Contingency Table - Clicks:\n", contingency_clicks)

# Step 5: Chi-Square Test
chi2, p, dof, expected = stats.chi2_contingency(contingency_clicks)

print(f"\n📈 Chi-Square Test for Clicks:")
print(f"Chi² = {chi2:.4f}")
print(f"p-value = {p:.4f}")

# Optional: Interpret result
alpha = 0.05
if p < alpha:
    print("✅ Statistically significant difference in click-through rates.")
else:
    print("❌ No statistically significant difference in click-through rates.")

# Repeat for re-enrollment
contingency_reenroll = pd.crosstab(df['email_group'], df['reenrolled'])
chi2_re, p_re, _, _ = stats.chi2_contingency(contingency_reenroll)

print(f"\n📈 Chi-Square Test for Re-enrollment:")
print(f"Chi² = {chi2_re:.4f}")
print(f"p-value = {p_re:.4f}")
if p_re < alpha:
    print("✅ Statistically significant difference in re-enrollment rates.")
else:
    print("❌ No statistically significant difference in re-enrollment rates.")
