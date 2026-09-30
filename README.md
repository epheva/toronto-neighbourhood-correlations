# Toronto Neighbourhoods Through 103 Public Indicators

This repository contains the data and Python notebooks used for my exploratory analysis of 140 historical Toronto neighbourhoods across 103 public indicators.

The full methodology, results, visualizations, interpretations, and limitations are available on the project website:

**[Read the full analysis](https://epheva.github.io/toronto-neighbourhood-correlations/)**

## Files

- **`df_preprocess.ipynb`**  
  Data cleaning, geographic processing, voter-turnout construction, neighbourhood mapping, rate creation, and merging of the source datasets.

- **`df_analysis.ipynb`**  
  Main analysis notebook containing the correlation analysis, FDR-corrected correlations, hierarchical clustering of variables, silhouette analysis, K-means neighbourhood clustering, and visualizations.

- `final_table.xlsx`  
  Cleaned final dataset containing 140 neighbourhoods and 103 numeric indicators, plus neighbourhood ID and name.

- `MasterList.xlsx`  
  Inventory of the original public datasets, including source links, descriptions, filenames, and internal dataset IDs.

- `CorrMatrix.csv`
  Numerical **103 × 103 Pearson correlation matrix**.

## Notes

The analysis is exploratory and neighbourhood-level. Correlations and clusters describe patterns across geographic areas and should not be interpreted as causal effects or as descriptions of individual residents.

The preprocessing notebook references the original raw data files and geographic layers used during development. These are documented in `MasterList.xlsx` but are not all included in this repository.