# Binance Futures CLI Trading Bot

A Python-based Binance Futures Testnet Trading Bot built with the Binance API.

## Features

* Binance Futures Testnet integration
* Market Orders
* Limit Orders
* Command Line Interface (CLI)
* Environment Variable Security
* Logging System
* Order Validation
* Git & GitHub Integration

## Technologies Used

* Python 3.13
* python-binance
* python-dotenv
* Git
* GitHub

## Project Structure

trading_bot/

├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── account.py
│   ├── positions.py
│   └── logging_config.py

├── cli.py
├── requirements.txt
├── README.md

## Example Usage

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## Author

Priya Bariya

## Then run these commands in PowerShell:

git add README.md

git commit -m "Added project documentation"

git push
