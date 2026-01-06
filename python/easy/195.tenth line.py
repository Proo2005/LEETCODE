# Read from the file file.txt and output the tenth line to stdout.
STARTING=10; NLINES=1; cat file.txt | tail -n+${STARTING} | head -n${NLINES}