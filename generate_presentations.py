import csv
import os
import re
from datetime import datetime
from jinja2 import Template

# Path to your template file and CSV manifest
TEMPLATE_FILE = 'template.md'
CSV_FILE = 'manifest.csv'
OUTPUT_DIR = 'presentations'

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load the template
with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
    template_content = f.read()
template = Template(template_content)

# A function to clean up the title for filenames (remove problematic characters)
def slugify(value):
    value = value.lower()
    value = re.sub(r'[^\w\s-]', '', value)  # remove non-alphanumeric characters
    value = re.sub(r'[\s_-]+', ' ', value).strip()
    value = re.sub(r'\s', '-', value)
    return value

# Read the CSV manifest
with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Clean up the title for the filename
        title_slug = slugify(row['title'])
        # Generate the output filename using date, class, and the title slug
        # Format: "YYYYMMDD <class> <title slug>.md"
        filename = f"{row['date']} {row['class']} {title_slug}.md"
        output_path = os.path.join(OUTPUT_DIR, filename)

        # Skip file generation if it already exists
        if os.path.exists(output_path):
            print(f"Skipped (already exists): {output_path}")
            continue
        
        # Convert the date from YYYYMMDD to DD/MM/YY for display in the presentation
        try:
            date_obj = datetime.strptime(row['date'], "%Y%m%d")
            formatted_date = date_obj.strftime("%d/%m/%y")
        except Exception as e:
            formatted_date = row['date']  # fallback in case of error
        
        # Add the formatted_date to the row data for use in the template
        row['formatted_date'] = formatted_date
        
        # Render the template with row data
        rendered_content = template.render(**row)
        
        # Write the rendered content to a Markdown file
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(rendered_content)
        print(f"Generated {output_path}")
