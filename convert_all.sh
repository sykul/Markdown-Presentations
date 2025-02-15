#!/bin/bash
# Create the output directory if it doesn't exist
mkdir -p pdf

# Loop over all Markdown files in the presentations directory
for file in presentations/*.md; do
  # Extract the base name (without the .md extension)
  filename=$(basename "$file" .md)
  # Convert the Markdown file to PDF with Marp, output to the pdf directory
  marp "$file" --pdf --output "pdf/${filename}.pdf"
done
