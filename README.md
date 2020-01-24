# Simple Dynamic Crawler
This project is a simple crawler for extracting the price of some stocks from [TGJU](http://www.tgju.org) webiste.

In order to run this project, you need:
- Python v3.5+
- ChromeDriver (You can get this driver for your operating system from the [Chromium](https://chromedriver.chromium.org/downloads) website)

then run:
```bash
pip install -r requirements.txt
```

Now you can run this project by adding the desired links to `urls` list, and setting the time interval by editing `start_time` and `end_time` in [`main.py`](./main.py).
