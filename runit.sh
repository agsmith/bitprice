#!/bin/bash
echo $(date) >> ~/log/bash_cron_log.txt
python /Users/adamsmith/work/ccad/development/github/bitprice/bitprice.py >> bash_cron_log.txt
