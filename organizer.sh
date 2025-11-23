#!/bin/bash

# Create archive folder if it doesn't exist
mkdir -p archive

# Find all CSV files in the current directory
for file in *.csv; do
    # Skip if no CSV files exist
    [ -e "$file" ] || continue

    # Create a timestamp
    timestamp=$(date +%Y%m%d-%H%M%S)

    # Define new file name with timestamp
    base="${file%.csv}"
    newfile="${base}-${timestamp}.csv"

    # Log the action in organizer.log
    echo "Archiving $file as $newfile at $(date)" >> organizer.log
    cat "$file" >> organizer.log
    echo "---------------------------------" >> organizer.log

    # Move and rename the file to the archive folder
    mv "$file" archive/"$newfile"

    # Optional: Print a message to the console
    echo "Archived $file -> archive/$newfile"
done

