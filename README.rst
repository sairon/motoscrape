Motoscrape
==========

This project is a simple Scrapy-based tool that crawls a few websites
that publish motorcycle advertisements and sends periodic reports
through email.

The code style and other aspects of the code are probably far away from
the best practices. Its purpose is just to do the job it was made for
and maybe - show how it's easy to make a working Scrapy crawler.

Sidenote: Yeah, I know, there's a lot of stuff hardcoded in the scripts.

Usage
-----

At first initialize the database of existing advertisements. To do so, create
a directory called "scrapes" and run the initial scraping::

    mkdir scrapes
    ./run.sh init

Then, if you want to get a report of the new advertisements, simply run the run
command::

    ./run.sh

Each time this command is executed, a new "database" file is created. To get
the new advertisements through email, you can use the ``reporter.sh`` script.
It either sends new ads through email or sends the whole stderr in case of a
failure. Mail text is constructed in the ``makereport.py``; ``sendreport.py``
is a helper script that sends the email through the local SMTP server.

License
-------

This software is published under the the Unlicense license. Basically,
you can do whatever you want to do with it. I'm just not liable for any
damages made.
