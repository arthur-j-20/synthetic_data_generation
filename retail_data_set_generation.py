import numpy as np
import pandas as pd
from graph_show import show_graph, scatter_income_spend

# Reproducibility: same random output each time
rng = np.random.default_rng(42)

# Number of customers
n = 1000

# Customer IDs
customer_id = np.arange(1, n + 1)

# Ages: integers from 18 to 80
age = rng.integers(18, 81, size=n)

# Countries: weighted probabilities
country = rng.choice(
    ["US", "CA", "UK", "AU"],
    size=n,
    p=[0.55, 0.20, 0.15, 0.10]
)

# Student rule:
# younger people are more likely to be students
student_prob = np.where(age <= 25, 0.45, 0.08)
is_student = rng.random(n) < student_prob

# Income base depends loosely on age
income = 18000 + age * 1200 + rng.normal(0, 12000, size=n)

# Students tend to earn less
income = np.where(is_student, income * 0.55, income)

# Keep income in a sensible range
income = np.clip(income, 8000, 200000)

# Spend score:
# depends on income, a little on age, plus noise
spend_score = (
    income / 2000
    + age * 0.15
    + rng.normal(0, 8, size=n)
)

# Clamp to a reasonable scale
spend_score = np.clip(spend_score, 1, 100)

# Build DataFrame
df = pd.DataFrame({
    "customer_id": customer_id,
    "age": age,
    "country": country,
    "is_student": is_student,
    "income": income.round(2),
    "spend_score": spend_score.round(2)
})

# print(df.head())
# print()
# print(df.describe(include="all"))


print("\nCountry distribution:")
print(df["country"].value_counts(normalize=True).round(3))

print("\nStudent rate:")
print(df["is_student"].mean().round(3))

print("\nAverage income by student status:")
print(df.groupby("is_student")["income"].mean().round(2))

print("\nAverage income by country:")
print(df.groupby("country")["income"].mean().round(2))

show_graph(df)

scatter_income_spend(df)