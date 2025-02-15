# Workflow for creating presentations
1. Compile a list of your upcoming lessons in `manifest.csv` with the title of the lesson, class group, and the date (YYYYMMDD).
2. Run `python3 generate_presentations.py`, which will population the presentations folder with template lessons in markdown format. The file name will be something like `YYYYMMDD class topic.md`.
3. Edit the content of the markdown files with the content of the lesson.
4. Run `./convert_all.sh`. This will populate the pdf folder with the lessons in PDF format.

If you need to create new lessons, add them to `manifest.csv` and run the `python3 generate_presentations.py` again. This will not overwrite any of your existing markdown files. After any edits to your markdown files, run `./convert_all.sh` again.

# Create summaries of key facts

1. How It Works

    The script:
        Finds all Markdown files in presentations/ for the specified class (e.g., 2e).
        Extracts the "Key Facts" section from each file.
        Appends them to a summary file in the correct order (sorted by date).
        Outputs a file like key_facts_2e.md.

2. How to Use It

    Run the script:

`python3 compile_key_facts.py`

The script will:

-   Look for all Markdown files in presentations/ matching the specified class.
-   Extract "Key Facts" sections.
-  Sort them chronologically.
3. Customization

    To extract Key Facts for a different class, change the CLASS_NAME variable in the script.
    To change the order, modify the sorting logic in files.sort().

To convert the output to PDF, run:

`marp summaries/key_facts_2e.md --pdf`