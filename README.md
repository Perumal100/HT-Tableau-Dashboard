# Heat Signal | NYC 311 Heat & Hot Water Reports (2024)

[![Open the live dashboard](https://img.shields.io/badge/Explore-Live%20Dashboard-F28E2B?style=for-the-badge)](https://perumal100.github.io/HT-Tableau-Dashboard/)

**Heat Signal** is a public-facing Tableau dashboard that turns NYC 311 **HEAT/HOT WATER** service-request data into an accessible operational story. It is built as a portfolio case study demonstrating data preparation, metric validation, visual design, and interactive analysis.

## Live experience

- **Tableau Public workbook:** https://public.tableau.com/views/HeatSignalNYC311HeatHotWaterReports2024/HeatSignal2024

> The landing page embeds the Tableau workbook directly, so visitors can explore the dashboard without leaving the project.

## What the dashboard answers

1. **When did heat and hot-water reports peak in 2024?**  
   The monthly trend makes the seasonality immediately visible.

2. **Which boroughs generated the largest share of reports?**  
   The borough comparison ranks five NYC boroughs with clear, distinguishable colors.

3. **How does seasonality vary by borough?**  
   Select any borough bar to filter the monthly trend interactively.

## Data snapshot

| Measure | Value |
| --- | ---: |
| Service reports represented | 264,750 |
| Aggregated data rows | 17,830 |
| Geography | 5 NYC boroughs |
| Time range | January–December 2024 |
| Source topic | NYC 311 HEAT/HOT WATER requests |

The analysis uses aggregated counts. In Tableau, all measures should use `SUM(Requests)`, not a raw row count.

## Repository structure

```
├── index.html              # GitHub Pages portfolio landing page + Tableau embed
├── data/
│   └── heat_signal_tableau_data.csv
├── docs/
│   └── DATA_DICTIONARY.md
└── scripts/
    └── build_tableau_source.py
```

## Reproduce in Tableau Public

1. Connect Tableau Public to `data/heat_signal_tableau_data.csv`.
2. Build a monthly line chart with `Month Date` and `SUM(Requests)`.
3. Build a borough bar chart with `Borough` and `SUM(Requests)`; color by `Borough` and show labels.
4. Place both sheets on a dashboard titled **Heat Signal | NYC Heat & Hot Water Reports, 2024**.
5. Set the borough comparison sheet to **Use as Filter**.

The source dataset retains additional fields for reported scope, weekday, hour, and status so that the analysis can be expanded.

## Data source and attribution

The Tableau-ready data was derived from the verified compact request cube in the original [Heat Signal repository](https://github.com/Perumal100/Heat-Signal). The underlying public topic is the NYC Open Data 311 Service Requests dataset.

## Design rationale

The visual system pairs a warm orange monthly trend with a multi-color borough comparison on a clean, high-contrast canvas. The goal is an executive-friendly first read: a viewer sees the overall demand pattern, understands geographic concentration, and can then drill into a borough in one click.

## Author

**Perumal Marimuthu**  
Data analytics portfolio project · Tableau Public · GitHub Pages
