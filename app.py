from datetime import datetime
import os

def convert_to_ics(input_file, output_file):
    # Header for ICS file
    ics_header = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Python Script//Calendar Converter//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
"""
    
    # Footer for ICS file
    ics_footer = "END:VCALENDAR"
    
    # Read the input file and create events
    events = []
    with open(input_file, 'r', encoding='utf-8') as f:
        # Skip header row if exists
        header = f.readline().strip().split('\t')
        
        for line in f:
            # Split the tab-delimited line
            fields = line.strip().split('\t')
            
            # Assuming the format of input file is:
            # Subject    Start Date    Start Time    End Date    End Time    Description    Location
            if len(fields) >= 7:
                subject = fields[0]
                start_date = fields[1]
                start_time = fields[2]
                end_date = fields[3]
                end_time = fields[4]
                description = fields[5]
                location = fields[6]
                
                # Convert dates to ICS format (YYYYMMDDTHHmmss)
                try:
                    start_datetime = datetime.strptime(f"{start_date} {start_time}", "%Y-%m-%d %H:%M")
                    end_datetime = datetime.strptime(f"{end_date} {end_time}", "%Y-%m-%d %H:%M")
                    
                    event = f"""BEGIN:VEVENT
SUMMARY:{subject}
DTSTART:{start_datetime.strftime("%Y%m%dT%H%M%S")}
DTEND:{end_datetime.strftime("%Y%m%dT%H%M%S")}
DESCRIPTION:{description}
LOCATION:{location}
END:VEVENT
"""
                    events.append(event)
                except ValueError as e:
                    print(f"Error processing line: {line.strip()}")
                    print(f"Error message: {str(e)}")
    
    # Write the ICS file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(ics_header)
        for event in events:
            f.write(event)
        f.write(ics_footer)

def main():
    # Example usage
    input_file = "calendar_events.txt"
    output_file = "calendar_events.ics"
    
    if os.path.exists(input_file):
        convert_to_ics(input_file, output_file)
        print(f"Conversion complete! Calendar file saved as: {output_file}")
    else:
        print(f"Input file '{input_file}' not found!")

if __name__ == "__main__":
    main()