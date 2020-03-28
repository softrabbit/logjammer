# logjammer
Tail and combine Apache access and error log

## The problem
Ever needed to watch the Apache error log scroll by? Ever had trouble guessing which request an error message comes from? Looks like the best way to do that is using a [request id](https://serverfault.com/questions/598525/adding-url-accessed-to-apache-error-log), which you then need to match between the error and access logs. Not too convenient.

## A solution
This piece of Python opens an access log and an error log, keeps reading whatever is added to the end of the file (```tail -f``` in unix speak), and combines the output with the access log line first and any related error log output under it.

## Configuration
1. Configure your Apache logs to output the request id (```%L``` in ```ErrorLogFormat``` and ```LogFormat```. NB! Put the ID before any free-format fields, like the error message, as the logic here is geared towards space-separated lines.
2. (for now) Edit the logjammer source, adjust the locations of the log files and places of the ID fields in them to match your logs.
3. Run logjammer in a terminal of your choice.

## Limitations
* Only live log updates, no after-the-fact analysis. There are probably other tools to do that.
* No filtering of lines, might add that at some point.
* No filtering of fields, that might be useful as well.
