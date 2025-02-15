import os
import re

# Configuration
PRESENTATIONS_DIR = "presentations"
OUTPUT_DIR = "summaries"
CLASS_NAME = "2e"  # Change this to filter a different class

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Output file
output_file = os.path.join(OUTPUT_DIR, f"key_facts_{CLASS_NAME}.md")

# Find all relevant Markdown files for the class
files = [f for f in os.listdir(PRESENTATIONS_DIR) if f.endswith(".md") and f" {CLASS_NAME} " in f]
files.sort()  # Sort to maintain chronological order

key_facts_content = []

# Regex pattern to match "Key Facts" sections
key_facts_pattern = re.compile(r"^# Key Facts(?: about (.*))?\n([\s\S]+?)(?=\n# |\Z)", re.MULTILINE)

for file in files:
    file_path = os.path.join(PRESENTATIONS_DIR, file)
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract the "Key Facts" section
    match = key_facts_pattern.search(content)
    if match:
        topic = match.group(1) or file.split(" ", 2)[-1].replace(".md", "")  # Use topic from slide or filename
        key_facts_text = match.group(2).strip()
        
        key_facts_content.append(f"# {topic}\n{key_facts_text}\n")

# Write the compiled Key Facts summary
if key_facts_content:
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(key_facts_content))
    print(f"Generated {output_file}")
else:
    print("No Key Facts sections found!")
