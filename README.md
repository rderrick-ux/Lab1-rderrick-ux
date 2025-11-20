Grade Generator & Organizer

Overview
This project has two scripts:
grade-generator.py: This is a Python script that gathers the information about the assignment, computes grades, provides the summary, and then stores the findings in grades.csv
organizer.sh: Bash script which identifies the CSV files, renames them based on the timestamp, shifts the files to an archive folder and logs the operations.

How to use grade-generator.py
To run the script: ./grade-generator.py
Name of the assignment, type (FA or SA), grade (0-100) and weight.
Repeat until finished.
The program generates a summary and prepares grades.csv where all the information is stored.

How to use organizer.sh
Run it: ./organizer.sh
It will open an archive folder and transfer CSVs in it with time-named files and add information to organizer.log

Example project structure
Before running organizer.sh:
grade-generator.py
grades.csv
organizer.sh

After running organizer.sh:
archive/grades-YYYYMMDD-HHMMSS.csv
grade-generator.py
organizer.sh
organizer.log
