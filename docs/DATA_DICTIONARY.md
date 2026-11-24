# Data Dictionary

`data/heat_signal_tableau_data.csv` contains 17,830 aggregate rows representing 264,750 NYC 311 HEAT/HOT WATER service reports during calendar year 2024.

| Column | Tableau use |
| --- | --- |
| Month Date | Continuous date for the monthly trend. |
| Month Number / Month | Sort and label monthly views. |
| Borough | Geographic comparison and dashboard filter. |
| Reported Scope | Detail/extension dimension. |
| Weekday Number / Weekday | Day-of-week analysis. |
| Hour / Hour Label | Hour-of-day analysis. |
| Status | Request-status segmentation. |
| Requests | **Aggregate count; always use SUM(Requests).** |
