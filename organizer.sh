#!/bin/bash

# Create archive folder if it doesn't exist
mkdir -p archive

#ind all CSV files in current directory
for file in *.csv; do
    # skip if no CSV files exist
    [ -e "$file" ] || continue

    #reate timestamp
    timestamp=$(date +%Y%m%d-%H%M%S)

    #efine new file name with timestamp
    base="${file%.csv}"
    newfile="${base}-${timestamp}.csv"

    #og action
    echo "Archiving $file as $newfile at $(date)" >> organizer.log
    cat "$file" >> organizer.log
    echo "---------------------------------" >> organizer.log

    #ove & rename to archive
    mv "$file" archive/"$newfile"
done

