Project 2 – Research / Social Impact Data Analysis

# Violence and College Enrollment: County-Level Analysis (Maryland)

## Motivation
Educational participation is shaped by both school-level and neighborhood-level conditions. This project looks into whether community violence (measured via violent crime rates) is associated with college enrollment levels at the county level.

## Research Question
**Does neighborhood violence relate to college enrollment per capita?**

## Data Sources
This project integrates public crime data with public education/enrollment data and county population estimates.

- Crime data: [(https://catalog.data.gov/dataset/violent-crime-property-crime-by-county-1975-to-present) - U.S. county-level violent and property crime statistics compiled from the FBI Uniform Crime Reporting (UCR) Program and published via Data.gov. The dataset includes annual counts and rates of major crime categories by county, along with county population estimates used to compute per-capita crime rates (1975–present)]
- College enrollment data: [(https://opendata.maryland.gov/api/views/63pe-mygy/rows.csv) - Maryland Open Data portal dataset providing county-level totals of postsecondary enrollment across public institutions in Maryland, maintained by the Maryland Higher Education Commission. The data includes aggregate enrollment counts by county and year.]
- Geography unit: Maryland counties. Crime and education datasets were aggregated and merged using county identifiers to create a unified regional analysis dataset.

## Methods
### Phase 1–3: Data Pipeline
- Ingested raw datasets and saved reproducible copies to `data/raw/`
- Cleaned and standardized column names and geographic identifiers
- Merged datasets into a unified county-level dataset saved to `data/processed/merged_data.csv`

### Phase 4: Exploratory Data Analysis (EDA)
- Examined distributions, skewness, and outliers for violent crime rates and enrollment
- Visualized the relationship between violent crime rate and college enrollment per capita
- Generated correlation matrices
- Key figures are saved in `figures/`.

### Phase 5: Statistical Testing
We conducted Pearson and Spearman correlation tests and an OLS regression coefficient test using SciPy.

**Results (n = 24 counties):**
- Pearson correlation: r = **0.373**, p = **0.072**
- Spearman correlation: ρ = **0.237**, p = **0.265**

**Robustness check (trimmed extremes; n = 22):**
- Pearson correlation (trimmed): r = **0.422**, p = **0.050**
- Spearman correlation (trimmed): ρ = **0.129**, p = **0.568**

Overall, results suggest a **moderate positive association** between violent crime rate and college enrollment per capita, though statistical strength is limited and sensitive to outliers.

### Phase 6: Classification Modeling
We framed enrollment per capita as a binary classification task (low vs high enrollment using a median split) and trained:

- Logistic Regression (baseline)
- Random Forest (nonlinear model)

**Model performance:**
- Logistic Regression — Accuracy: **0.167**, ROC-AUC: **0.111**
- Random Forest — Accuracy: **0.667**, ROC-AUC: **0.667**

These results suggest limited linear predictive signal, while nonlinear modeling yields moderate performance using crime rate and population alone.

## Key Outputs
- Processed dataset: `data/processed/merged_data.csv`
- Statistical test results: `data/processed/statistical_results.csv`
- Model results: `data/processed/model_results.csv`
- Figures: `figures/*.png`

## Repository Structure
README.md/
project-2-research/
  data/
    raw/
    processed/
  figures/
  notebooks/
  src/
  README.md
  requirements.txt


