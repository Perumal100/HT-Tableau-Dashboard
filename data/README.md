# Tableau-ready source data

`heat_signal_tableau_data.csv` holds 17,830 aggregate records representing 264,750 NYC 311 HEAT/HOT WATER reports for calendar year 2024.

Use `SUM(Requests)` in Tableau, never a raw row count. See [`../docs/DATA_DICTIONARY.md`](../docs/DATA_DICTIONARY.md) for fields and definitions.

To rebuild it, clone the [Heat-Signal](https://github.com/Perumal100/Heat-Signal) repository next to this one and run `python scripts/build_tableau_source.py`. The script stops if the exported total does not equal 264,750.
