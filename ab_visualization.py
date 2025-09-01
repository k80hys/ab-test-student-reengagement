import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("ab_test_student_outreach.csv")

# Prepare funnel metrics per group
funnel = df.groupby('email_group').agg(
    total=('student_id', 'count'),
    clicked=('clicked_link', 'sum'),
    booked=('booked_call', 'sum'),
    reenrolled=('reenrolled', 'sum')
).reset_index()

# Calculate rates (%)
funnel['click_rate'] = funnel['clicked'] / funnel['total'] * 100
funnel['booking_rate'] = funnel['booked'] / funnel['clicked'] * 100
funnel['reenroll_rate'] = funnel['reenrolled'] / funnel['booked'] * 100

# Set plot style
sns.set(style="whitegrid")

# Plot conversion funnel
fig, ax = plt.subplots(figsize=(10, 6))

width = 0.35  # bar width
x = range(len(funnel['email_group']))

# Bars for each stage
ax.bar(x, funnel['click_rate'], width, label='Click Through Rate')
ax.bar(x, funnel['booking_rate'], width, bottom=funnel['click_rate'], label='Booking Rate')
ax.bar(x, funnel['reenroll_rate'], width, bottom=funnel['click_rate'] + funnel['booking_rate'], label='Re-enroll Rate')

# Labels and titles
ax.set_xticks(x)
ax.set_xticklabels(['Group A (Control)', 'Group B (Personalized)'])
ax.set_ylabel('Percentage (%)')
ax.set_title('A/B Test Conversion Funnel by Email Group')
ax.legend()

# Show values on bars
for i in x:
    ax.text(i, funnel['click_rate'][i] / 2, f"{funnel['click_rate'][i]:.1f}%", ha='center', color='white', fontweight='bold')
    ax.text(i, funnel['click_rate'][i] + funnel['booking_rate'][i] / 2, f"{funnel['booking_rate'][i]:.1f}%", ha='center', color='white', fontweight='bold')
    ax.text(i, funnel['click_rate'][i] + funnel['booking_rate'][i] + funnel['reenroll_rate'][i] / 2, f"{funnel['reenroll_rate'][i]:.1f}%", ha='center', color='white', fontweight='bold')

plt.tight_layout()
plt.show()
