"""Verify the archived file hashes and recompute selected results from individual records."""
import argparse
import csv
import hashlib
import math
from collections import defaultdict
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent


def rows(name):
    with (ROOT / "data" / name).open(encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source))


def check(same, label):
    if not same:
        raise ValueError(label)


def near(actual, expected, label):
    check(math.isclose(actual, float(expected), abs_tol=1e-9, rel_tol=1e-10), label)


def verify_results():
    groups = defaultdict(dict)
    for r in rows("branch_pairs.csv"):
        if int(r["step"]) == 16:
            key = (r["shape"], r["engine"], r["view"], r["model"])
            check(r["scene"] not in groups[key], key)
            groups[key][r["scene"]] = float(r["passive_mae_mm"])
    summaries = rows("branch_summary.csv")
    check(len(summaries) == 8, "fork/packing comparison groups")
    for r in summaries:
        design = (r["shape"], r["engine"], r["view"])
        for model in ["Zero", "Graph", "Events", "Corrected"]:
            values = groups[(*design, model)]
            check(len(values) == 240, design)
            near(mean(values.values()), r[model.lower()], (design, model))
        corrected, events = (groups[(*design, m)] for m in ["Corrected", "Events"])
        check(corrected.keys() == events.keys(), design)
        near(mean(corrected[k] - events[k] for k in events), r["paired_delta"], design)
    print("contact-response: eight paired 240-scene comparisons agree")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results-only", action="store_true",
                        help="Check the numerical summaries without checking the original file digests.")
    args = parser.parse_args()
    if not args.results_only:
        for line in (ROOT / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
            expected, name = line.split("  ", 1)
            check(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name)
    verify_results()


if __name__ == "__main__":
    main()
