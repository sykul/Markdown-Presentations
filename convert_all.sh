#!/bin/bash

# Check if two arguments are provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <input_directory> <output_directory>"
  exit 1
fi

INPUT_DIR="$1"
OUTPUT_DIR="$2"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Loop over all Markdown files in the input directory
for file in "$INPUT_DIR"/*.md; do
  # Ensure we only process files
  [ -f "$file" ] || continue
  
  # Extract the base name (without the .md extension)
  filename=$(basename "$file" .md)
  
  # Convert the Markdown file to PDF with Marp, output to the output directory
  marp "$file" --pdf --output "$OUTPUT_DIR/${filename}.pdf"
done

echo "Conversion complete. PDFs are in '$OUTPUT_DIR'."
