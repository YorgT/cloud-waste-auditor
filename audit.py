#!/usr/bin/env python3
"""Explainable cloud-cost CSV auditor prototype. Standard library only."""
import argparse, csv, json
from collections import defaultdict
from pathlib import Path

REQUIRED = {"service", "cost"}

def audit(path):
    totals = defaultdict(float)
    rows = 0
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fields = {x.strip().lower() for x in (reader.fieldnames or [])}
        if not REQUIRED <= fields:
            raise ValueError("CSV must contain at least 'service' and 'cost' columns")
        for row in reader:
            normalized = {str(k).strip().lower(): v for k, v in row.items() if k}
            service = (normalized.get("service") or "Unknown service").strip() or "Unknown service"
            try:
                cost = float((normalized.get("cost") or "").replace(",", ""))
            except ValueError:
                continue
            if cost < 0:
                continue
            totals[service] += cost
            rows += 1
    grand_total = sum(totals.values())
    return {"rows_analyzed": rows, "total_cost": round(grand_total, 2), "services": [{"service": k, "cost": round(v, 2), "share_percent": round((v / grand_total * 100), 2) if grand_total else 0} for k, v in sorted(totals.items(), key=lambda x: x[1], reverse=True)], "limitations": ["This report summarizes provided CSV data only.", "It does not identify idle resources or prove savings without resource-level evidence.", "Review billing currency, date range, and completeness before acting."]}

def main():
    p = argparse.ArgumentParser(description="Summarize a cloud billing CSV safely")
    p.add_argument("csv_file", help="CSV with service,cost columns")
    p.add_argument("--out", help="Optional JSON output path")
    a = p.parse_args()
    result = audit(a.csv_file)
    rendered = json.dumps(result, indent=2)
    if a.out: Path(a.out).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)

if __name__ == "__main__": main()
