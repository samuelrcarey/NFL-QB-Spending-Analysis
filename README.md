# NFL QB Spending Analysis (2013–2025)

This project analyzes how quarterback (QB) spending relates to team success in the National Football League from 2013 through 2025. Team success is measured using regular-season win percentage and playoff appearances.

The analysis explores whether higher QB spending leads to better outcomes and whether teams with relatively low-cost quarterbacks are more or less likely to reach the playoffs.

---

## Data

The dataset includes one CSV file per season from 2013–2025, which are programmatically combined prior to analysis.

Each file contains team-level salary allocations by position, including quarterback spending, along with team performance metrics such as win percentage and playoff appearance.

---

## Methodology

1. **Data Preparation**
   - All seasonal CSV files are loaded and combined into a single dataset.
   - QB spending values are cleaned and converted to numeric format.
   - Win percentage is taken directly from the dataset to account for seasons with different numbers of games.
   - Playoff appearance is converted into a binary variable.

2. **Win Percentage Model**
   - A linear regression model is used to estimate the relationship between log-transformed QB spending and regular-season win percentage.

3. **Playoff Probability Model**
   - Logistic regression is used to estimate how QB spending affects the likelihood of making the playoffs.

4. **QB Cost Classification**
   - Teams are classified as **low-cost QB teams** if their QB spending falls in the bottom third of all observations.
   - This classification is used to compare playoff outcomes between low-cost and high-cost QB teams.

---

## Results Interpretation

- **Win Percentage**
  - Higher QB spending is associated with a small increase in regular-season win percentage.
  - The relationship is statistically positive but explains only a small share of overall team performance variation (R² ≈ 0.014).

- **Playoff Probability**
  - Increased QB spending is associated with higher odds of making the playoffs.
  - The playoff model estimates an odds ratio of approximately **1.29**, indicating a meaningful increase in postseason likelihood with higher QB investment.

- **Low-Cost vs High-Cost QB Teams**
  - High-cost QB teams made the playoffs approximately **43%** of the time.
  - Low-cost QB teams made the playoffs approximately **34%** of the time.
  - Low-cost QB teams have roughly **30% lower odds** of making the playoffs compared to high-cost QB teams.

---

## Files

- `analysis.py` — Main analysis script
- `qb_spending_vs_win_pct.png` — Visualization of QB spending vs win percentage
- `README.md` — Project documentation
- `salary_cap_team_success_YYYY.csv` — Seasonal datasets (2013–2025)

---

## How to Run

```bash
python3 analysis.py
