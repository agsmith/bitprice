Script to read aloud the current price of bitcoin in USD

crontab entry to run at the top of the hour

```
› crontab -l
0 * * * * python ~/.bitprice.py
```
