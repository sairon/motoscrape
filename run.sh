#!/bin/sh

# Initial run - create JSON databases and exit
if [ "$1" = "init" ]; then
    for spider in $(scrapy list); do
        scrapy crawl "$spider" -o "scrapes/${spider}_init.json"
    done
    exit 0
fi

# Standard run - create JSON database ...
timestamp=$(date +%s)

for spider in $(scrapy list); do
    scrapy crawl "$spider" -o "scrapes/${spider}_${timestamp}.json"
    find scrapes -size 1c -delete
done

# ... and create a report, if there are new ads
for f in scrapes/*_${timestamp}.json; do
    [ -f "$f" ] && ./makereport.py "$f" || true
done
