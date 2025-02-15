import os
import re
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Compile all Key Facts sections for a specified class from Markdown presentations."
    )
    parser.add_argument("class_name", help="Class name to filter presentations (e.g., '2e')")
    parser.add_argument(
        "--input-dir", default="presentations", help="Directory containing Markdown presentation files"
    )
    parser.add_argument(
        "--output-dir", default="summaries", help="Directory to save the compiled summary"
    )
    args = parser.parse_args()

    PRESENTATIONS_DIR = args.input_dir
    OUTPUT_DIR = args.output_dir
    CLASS_NAME = args.class_name

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_file = os.path.join(OUTPUT_DIR, f"key_facts_{CLASS_NAME}.md")

    # Find all relevant Markdown files for the specified class
    files = [f for f in os.listdir(PRESENTATIONS_DIR) if f.endswith(".md") and f" {CLASS_NAME} " in f]
    files.sort()  # Sort files to maintain chronological order

    key_facts_content = []

    # Regex pattern to match the "Key Facts" section
    key_facts_pattern = re.compile(
        r"^# Key Facts(?: about (.*))?\n([\s\S]+?)(?=\n# |\Z)", re.MULTILINE
    )

    for file in files:
        file_path = os.path.join(PRESENTATIONS_DIR, file)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract the "Key Facts" section
        match = key_facts_pattern.search(content)
        if match:
            topic = match.group(1) or file.split(" ", 2)[-1].replace(".md", "")
            key_facts_text = match.group(2).strip()
            key_facts_content.append(f"# {topic}\n{key_facts_text}\n")

    # Write the compiled Key Facts summary to file
    if key_facts_content:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(key_facts_content))
        print(f"Generated {output_file}")
    else:
        print("No Key Facts sections found for class:", CLASS_NAME)

if __name__ == "__main__":
    main()
