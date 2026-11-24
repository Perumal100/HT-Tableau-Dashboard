"""Export the verified Heat Signal compact request cube to Tableau CSV."""
from __future__ import annotations
import csv
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent / "Heat-Signal"
DATA = ROOT / "dist" / "data"
OUTPUT = Path(__file__).parent.parent / "data" / "heat_signal_tableau_data.csv"

def main() -> None:
    meta = json.loads((DATA / "meta.json").read_text(encoding="utf-8"))
    cube = json.loads((DATA / "requests.json").read_text(encoding="utf-8"))
    headers = ["Month Date", "Month Number", "Month", "Borough", "Reported Scope",
               "Weekday Number", "Weekday", "Hour", "Hour Label", "Status", "Requests"]
    total = 0
    with OUTPUT.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for month, borough, scope, weekday, hour, status, requests in cube:
            total += requests
            writer.writerow([f"2024-{month:02d}-01", month,
                ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")[month-1],
                meta["boroughs"][borough], meta["scopes"][scope], weekday+1,
                meta["weekdays"][weekday], hour, f"{hour:02d}:00", meta["statuses"][status], requests])
    if total != meta["records"]:
        raise ValueError(f"Expected {meta['records']:,}; wrote {total:,}.")
    print(f"Wrote {len(cube):,} aggregate rows / {total:,} requests.")

if __name__ == "__main__":
    main()
