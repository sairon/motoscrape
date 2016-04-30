#!/bin/sh


if [ "$1" = "init" ]; then
    for spider in $(scrapy list); do
        scrapy crawl "$spider" -o "scrapes/${spider}_init.json"
    done
    exit 0
fi

timestamp=$(date +%s)

for spider in $(scrapy list); do
    scrapy crawl "$spider" -o "scrapes/${spider}_${timestamp}.json"
    find scrapes -size 1c -delete
done

for f in scrapes/*_${timestamp}.json; do
    [ -f "$f" ] && ./makereport.py "$f" || true
done
