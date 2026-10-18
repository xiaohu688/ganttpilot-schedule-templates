"""Validate the example CSV format and calculate an unlevelled FS timeline."""
import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"ID", "Phase", "Task Name", "Duration", "Predecessors", "Resource Names"}


def inspect_template(path):
    tasks = {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = REQUIRED - set(reader.fieldnames or [])
        if missing:
            raise ValueError("Missing columns: " + ", ".join(sorted(missing)))
        for row in reader:
            if not any(value for value in row.values()):
                continue
            task_id = int(row["ID"])
            duration = int(row["Duration"])
            if task_id <= 0 or task_id in tasks:
                raise ValueError(f"Invalid or duplicate task ID: {task_id}")
            if duration <= 0 or not row["Task Name"].strip():
                raise ValueError(f"Task {task_id} needs a name and positive whole-day duration")
            predecessors = [int(value.strip()) for value in row["Predecessors"].split(",") if value.strip()]
            if len(predecessors) != len(set(predecessors)):
                raise ValueError(f"Task {task_id} repeats a predecessor")
            tasks[task_id] = {"duration": duration, "predecessors": predecessors, "phase": row["Phase"]}
    if not tasks:
        raise ValueError("No tasks found")
    timings = {}
    visiting = set()

    def visit(task_id):
        if task_id not in tasks:
            raise ValueError(f"Missing predecessor task: {task_id}")
        if task_id in visiting:
            raise ValueError(f"Dependency cycle at task {task_id}")
        if task_id in timings:
            return timings[task_id]
        visiting.add(task_id)
        start = max((visit(predecessor)[1] for predecessor in tasks[task_id]["predecessors"]), default=0)
        timings[task_id] = (start, start + tasks[task_id]["duration"])
        visiting.remove(task_id)
        return timings[task_id]

    for task_id in tasks:
        visit(task_id)
    result = {
        "file": path.name,
        "tasks": len(tasks),
        "phases": len({task["phase"] for task in tasks.values()}),
        "dependencies": sum(len(task["predecessors"]) for task in tasks.values()),
        "calendar_days": max(finish for _, finish in timings.values()),
    }
    if path.resolve() == (ROOT / "templates/shutdown-turnaround-schedule-template.csv").resolve():
        if 8 not in timings or 26 not in timings:
            raise ValueError("Shutdown example needs tasks 8 and 26 for its outage measure")
        result["outage_days"] = timings[26][1] - timings[8][0]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path, help="CSV files; defaults to bundled templates")
    paths = parser.parse_args().files or sorted((ROOT / "templates").glob("*.csv"))
    try:
        results = [inspect_template(path) for path in paths]
    except (OSError, ValueError, TypeError, csv.Error) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        return 1
    print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
