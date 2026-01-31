import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression

# -----------------------------
# Load and prepare data
# -----------------------------
import glob

# -----------------------------
# Load and combine all seasons
# -----------------------------
files = glob.glob("data/salary_cap_team_success_*.csv")

df_list = []
for file in files:
    df = pd.read_csv(file)
    df_list.append(df)

data = pd.concat(df_list, ignore_index=True)

# Rename columns for consistency
data = data.rename(columns={
    "Winning %": "Win_Pct",
    "Playoff Appearance": "Playoff"
})

# Clean QB spending
data["QB"] = (
    data["QB"]
    .astype(str)
    .str.replace(r"[$,]", "", regex=True)
    .astype(int)
)

# Convert win percentage to numeric
data["Win_Pct"] = pd.to_numeric(data["Win_Pct"], errors="coerce")

# Create playoff binary
data["Playoff_Binary"] = data["Playoff"].map({"Yes": 1, "No": 0})

# Log-transform QB spending
data["Log_QB"] = np.log(data["QB"])

# -----------------------------
# Visualization
# -----------------------------
plt.figure()
plt.scatter(data["QB"], data["Win_Pct"], alpha=0.6)
plt.xlabel("QB Spending ($)")
plt.ylabel("Win Percentage")
plt.title("QB Spending vs Win Percentage (2013–2025)")
plt.savefig("qb_spending_vs_win_pct.png")
plt.close()

# -----------------------------
# Linear regression: Win %
# -----------------------------
X = data[["Log_QB"]]
y = data["Win_Pct"]

win_model = LinearRegression()
win_model.fit(X, y)

print("Win % model:")
print("Coefficient:", win_model.coef_[0])
print("R-squared:", win_model.score(X, y))

# -----------------------------
# Logistic regression: Playoffs
# -----------------------------
playoff_model = LogisticRegression(max_iter=1000)
playoff_model.fit(X, data["Playoff_Binary"])

odds_ratio = np.exp(playoff_model.coef_[0][0])

print("\nPlayoff model:")
print("Odds ratio:", odds_ratio)

# -----------------------------
# Low-cost QB classification
# -----------------------------
qb_cutoff = data["QB"].quantile(0.33)
data["LowCost_QB"] = (data["QB"] <= qb_cutoff).astype(int)

# Playoff probability comparison
playoff_rates = data.groupby("LowCost_QB")["Playoff_Binary"].mean()

print("\nPlayoff probability by QB cost group:")
print(playoff_rates)

# Logistic regression: Low-cost vs High-cost
cost_model = LogisticRegression(max_iter=1000)
cost_model.fit(data[["LowCost_QB"]], data["Playoff_Binary"])

cost_odds_ratio = np.exp(cost_model.coef_[0][0])

print("\nLow-cost vs High-cost QB:")
print("Odds ratio:", cost_odds_ratio)
