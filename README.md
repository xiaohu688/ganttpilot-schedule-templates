# GanttPilot Schedule Templates

Free project schedule templates for equipment installation and shutdown turnaround planning. Each CSV includes task IDs, phases, durations, predecessors and example resource names.

Maintained by [GanttPilot](https://ganttpilot.com), a workspace for importing Excel or Microsoft Project schedules, reviewing changes, and delivering an updated plan.

## Download a template

| Template | CSV | Tasks / phases | What it covers |
| --- | --- | --- | --- |
| Equipment installation | [Download CSV](templates/equipment-installation-schedule-template.csv) | 33 / 8 | Delivery, foundation readiness, lifting, mechanical completion, electrical work, commissioning and handover |
| Shutdown turnaround | [Download CSV](templates/shutdown-turnaround-schedule-template.csv) | 29 / 7 | Preparation, shutdown and isolation, inspection, repairs, reassembly, restart and closeout |

For a date-linked Excel workbook or a Gantt preview, use the corresponding page:

- [Equipment installation schedule template for Excel](https://ganttpilot.com/templates/equipment-installation-schedule-template)
- [Shutdown turnaround schedule template for Excel](https://ganttpilot.com/templates/shutdown-turnaround-schedule-template)

## Start with the task list

1. Open a CSV in Excel, LibreOffice Calc or another spreadsheet editor.
2. Replace the sample scope, durations and resource names with your project requirements.
3. Review the predecessor IDs before setting a baseline. A task starts after all its predecessors finish.
4. Use the linked Excel workbook for calculated dates, or [import your schedule into GanttPilot](https://ganttpilot.com/tools/excel-to-gantt-chart) for online review and editing.

CSV files contain task data. The Excel downloads on the website also contain date formulas and a weekly Gantt view. Public downloads need no signup. Online editing requires an account and is subject to the applicable plan.

## CSV columns

| Column | Meaning |
| --- | --- |
| `ID` | Unique task number used by predecessor references |
| `Phase` | Project phase |
| `Task Name` | Work item or review activity |
| `Duration` | Positive whole calendar days |
| `Predecessors` | Comma-separated task IDs; all links are finish-to-start with zero lag |
| `Resource Names` | Illustrative assigned crews, people or equipment |

Keep comma-containing fields quoted when editing raw CSV. Resource names describe assignments; they do not automatically balance crew capacity or resolve shared-access conflicts.

## Installation planning: two paths join before lifting

The example waits for equipment receipt, foundation release and approved lifting arrangements before the lift-readiness review. Mechanical completion, electrical records and controls setup later join at loop and interlock verification.

The sample dependency calculation spans **55 calendar days**. Vendor lead time, concrete and grout release, access and commissioning requirements must be replaced with project-specific inputs.

## Shutdown planning: project duration and outage duration

The example spans **47 calendar days**:

- 24 days of preparation before shutdown;
- a 20-day outage, from the start of task 8 through completion of task 26 at operations acceptance;
- 3 days of post-shutdown closeout.

Only approved work that does not block startup belongs after operations acceptance. Extending preparation can move the shutdown start; extending critical repair work can increase the outage.

These are illustrative, day-level planning allowances. They use calendar days including weekends, with no holidays or resource leveling. They are not installation instructions, approved isolation procedures or hourly shift execution plans.

## Check dependencies locally

The included Python utility checks IDs, durations, missing references and cycles, then calculates the finish-to-start timeline. It uses the Python 3 standard library and needs no package installation.

```sh
python3 scripts/validate_templates.py
```

To check an edited file:

```sh
python3 scripts/validate_templates.py path/to/your-template.csv
```

It reports task count, phase count, dependency count and calculated calendar-day duration. The bundled shutdown example also reports its outage duration. The utility calculates dependencies; it does not level resources or apply a work-week calendar.

## More scheduling resources

- [GanttPilot — import, review and deliver project schedules](https://ganttpilot.com)
- [Project schedule template library](https://ganttpilot.com/templates)
- [Excel to Gantt chart](https://ganttpilot.com/tools/excel-to-gantt-chart)
- [Microsoft Project XML viewer](https://ganttpilot.com/tools/ms-project-xml-viewer)

## Contributing and license

Corrections to task wording, missing dependencies and clearer planning examples are welcome through issues or pull requests. Keep examples fictional and avoid customer project data.

The [MIT license](LICENSE) covers the files in this repository. Source URLs and snapshot details are listed in [SOURCES.md](SOURCES.md).
