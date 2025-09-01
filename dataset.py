import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

data = pd.DataFrame({
    'student_id': np.arange(10001, 10001 + n),
    'email_group': np.random.choice(['A', 'B'], size=n),
    'age': np.random.randint(24, 55, size=n),
    'major': np.random.choice(['Psychology', 'Computer Science', 'Business Admin', 'Nursing', 'Marketing', 'History', 'Sociology'], size=n),
    'credits_completed': np.random.randint(30, 120, size=n),
    'days_since_last_enroll': np.random.randint(90, 1000, size=n),
})

# Simulate behavior based on email_group
data['clicked_link'] = np.where(
    (data['email_group'] == 'B') & (np.random.rand(n) < 0.30) |
    (data['email_group'] == 'A') & (np.random.rand(n) < 0.20), 1, 0
)

data['booked_call'] = np.where(
    (data['clicked_link'] == 1) & (np.random.rand(n) < 0.50), 1, 0
)

data['reenrolled'] = np.where(
    (data['booked_call'] == 1) & (np.random.rand(n) < 0.60), 1, 0
)

# Preview
print(data.head())

# Save to CSV
data.to_csv("ab_test_student_outreach.csv", index=False)
