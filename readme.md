# Excel to ICS Converter

This Python project allows you to convert events stored in an Excel file into a `.ics` calendar file. The generated `.ics` file can be imported into calendar applications like Google Calendar, Outlook, or Apple Calendar.

## Features

- Converts events from an Excel file to a valid `.ics` file.
- Ensures unique `UID` values for each event.
- Supports timezone information (Europe/Berlin) with proper `VTIMEZONE` configuration.
- Handles all-day events and events with specific start and end times.
- Skips invalid rows and logs errors for debugging.
- Compatible with common calendar applications.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Input File Format](#input-file-format)
- [Output File](#output-file)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository
```bash
   git clone https://github.com/yourusername/excel-to-ics.git
   cd excel-to-ics
```

2. Set up a virtual environment (optional but recommended)
```bash 
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
    pip install pandas openpyxl
```

## Usage
1. Place your input Excel file in the project directory. The file should contain the required columns (see Input File Format).

2. Run the script
```bash 
    python xls2ics.py
```

3. The .ics file will be generated in the same directory as the script, named calendar.ics.

4. Import the generated .ics file into your preferred calendar application.

## Input File Format

The input Excel file must include the following columns:

| Column Name      | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Subject**      | The event title or name.                                                   |
| **Start Date**   | The start date of the event (format: `dd.mm.yyyy`).                        |
| **Start Time**   | The start time of the event (format: `HH:MM`). Leave blank for all-day events. |
| **End Date**     | The end date of the event (format: `dd.mm.yyyy`).                          |
| **End Time**     | The end time of the event (format: `HH:MM`). Leave blank for all-day events. |
| **All Day Event**| `True` or `False`. Indicates if the event is an all-day event.             |
| **Description**  | A description or additional details about the event.                      |
| **Location**     | The location of the event.                                                |

### Example Input

| Subject             | Start Date | Start Time | End Date   | End Time | All Day Event | Description       | Location      |
|---------------------|------------|------------|------------|----------|---------------|-------------------|---------------|
| Team Meeting        | 01.02.2025 | 14:00      | 01.02.2025 | 15:00    | False         | Discuss Q1 goals | Office Room A |
| Project Kickoff     | 15.02.2025 |            | 15.02.2025 |          | True          | Kickoff meeting   | HQ Building   |

## Output file
The script generates an .ics file named calendar.ics. This file includes all events from the input Excel file in the standard iCalendar format.


## Error Handling
The script skips rows with invalid or missing data and logs an error message to the console. Ensure that:

- Dates are in the dd.mm.yyyy format.
- Times are in the HH:MM format.
- The All Day Event column contains `True` or `False`.

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPLv3). 

You are free to:
- **Use**: You may use this software for any purpose, including commercial use.
- **Modify**: You may modify the software to suit your needs.
- **Distribute**: You may distribute copies of the original or modified software under the same license.

### Conditions:
- **Source Availability**: Any modifications or derived works must also be open source and made available under the AGPLv3 license.
- **Prominent Notices**: You must retain the copyright notice, license notice, and disclaimer in any copies or modifications.
- **Network Interaction**: If this software is used to provide a service over a network, the source code must also be made available to users of that service.

### Disclaimer:
This software is provided "as is", without any warranties or guarantees of any kind. Use it at your own risk.

For the full terms of the AGPLv3 license, refer to the [official license text](https://www.gnu.org/licenses/agpl-3.0.html).