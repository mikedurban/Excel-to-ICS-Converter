import pandas as pd
import uuid
from datetime import datetime

def excel_to_ics(input_excel, output_ics):
    # Read Excel file
    df = pd.read_excel(input_excel)

    # Validate required columns
    required_columns = [
        "Subject", "Start Date", "Start Time", "End Date", "End Time",
        "All Day Event", "Description", "Location"
    ]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Prepare .ics file content
    ics_lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//DurbanIT//FOG Mitte 2025//DE",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:FOG Mitte",
        "X-WR-TIMEZONE:Europe/Berlin",
        "BEGIN:VTIMEZONE",
        "TZID:Europe/Berlin",
        "X-LIC-LOCATION:Europe/Berlin",
        "BEGIN:STANDARD",
        "TZOFFSETFROM:+0200",
        "TZOFFSETTO:+0100",
        "TZNAME:CET",
        "DTSTART:19701025T030000",
        "RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU",
        "END:STANDARD",
        "BEGIN:DAYLIGHT",
        "TZOFFSETFROM:+0100",
        "TZOFFSETTO:+0200",
        "TZNAME:CEST",
        "DTSTART:19700329T020000",
        "RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU",
        "END:DAYLIGHT",
        "END:VTIMEZONE"
    ]

    for index, row in df.iterrows():
        try:
            # Parse event details
            summary = row["Subject"]
            description = str(row["Description"]) if pd.notnull(row["Description"]) else "nan"
            location = str(row["Location"]) if pd.notnull(row["Location"]) else "nan"

            # Parse dates and times
            start_date = datetime.strptime(row["Start Date"], "%d.%m.%Y")
            start_time = row["Start Time"] if pd.notnull(row["Start Time"]) else "00:00"
            start_datetime = datetime.strptime(
                f"{row['Start Date']} {start_time}", "%d.%m.%Y %H:%M"
            )

            if pd.notnull(row["End Date"]):
                end_date = datetime.strptime(row["End Date"], "%d.%m.%Y")
            else:
                end_date = start_date

            end_time = row["End Time"] if pd.notnull(row["End Time"]) else "23:59"
            end_datetime = datetime.strptime(
                f"{row['End Date']} {end_time}", "%d.%m.%Y %H:%M"
            )

            # Handle all-day events
            all_day_event = str(row["All Day Event"]).strip().lower() == "true"
            if all_day_event:
                dtstart = f"DTSTART;VALUE=DATE:{start_date.strftime('%Y%m%d')}"
                dtend = f"DTEND;VALUE=DATE:{(end_date + pd.Timedelta(days=1)).strftime('%Y%m%d')}"
            else:
                dtstart = f"DTSTART;TZID=Europe/Berlin:{start_datetime.strftime('%Y%m%dT%H%M%S')}"
                dtend = f"DTEND;TZID=Europe/Berlin:{end_datetime.strftime('%Y%m%dT%H%M%S')}"

            # Generate a unique UID
            uid = f"{uuid.uuid4()}@durban.it.de"

            # Add event to .ics
            ics_lines.extend([
                "BEGIN:VEVENT",
                f"UID:{uid}",
                f"DTSTAMP:{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}",
                dtstart,
                dtend,
                f"SUMMARY:{summary}",
                f"LOCATION:{location}",
                f"DESCRIPTION:{description}",
                "STATUS:CONFIRMED",
                "TRANSP:OPAQUE",
                "END:VEVENT"
            ])
        except Exception as e:
            print(f"Error processing row {index}: {e}")

    # End .ics file
    ics_lines.append("END:VCALENDAR")

    # Write to output file
    with open(output_ics, "w", encoding="utf-8") as f:
        f.write("\n".join(ics_lines))
    print(f".ics file successfully created at {output_ics}")


# Example usage
input_excel_file = "events.xlsx"
output_ics_file = "calendar.ics"
excel_to_ics(input_excel_file, output_ics_file)
