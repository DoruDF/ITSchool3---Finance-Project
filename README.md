Fintech Portfolio API
The Fintech Portfolio API is a web server with a REST API that allows you to keep track of your different financial assets and compare their evolution over time.

![image](https://github.com/user-attachments/assets/33208bc9-890b-4472-bcd1-f1e3b150fba6)


Deployment Instructions

Windows

Clone the git repository using <git_repo_url>.
Navigate to the cd <your-created-directory> directory.
Create a new virtual environment by running python -m venv env/.
Activate the virtual environment by running .\env\Scripts\activate.
Upgrade pip by running python.exe -m pip install --upgrade pip.
Install the required dependencies by running pip install -r requirements.txt.
Configure database settings(pick sqlite3 or json) in the config.json file found in configuration file.
Run main.py
Check swagger.


Linux

Clone the git repository using <git_repo_url>.
Navigate to the cd <your-created-directory>.
Create a new virtual environment by running python3 -m venv env/.
Activate the virtual environment by running source env/bin/activate.
Upgrade pip by running pip install --upgrade pip.
Install the required dependencies by running pip install -r requirements.txt.
Configure database settings(pick sqlite3 or json) in the config.json file found in configuration file.
Run main.py
Check swagger.
Technology Stack
Fintech Portfolio API web server that allows you to keep track of your different financial assets(stocks) and compare their evolution over time. Leveraging modern tools such as FastAPI, Uvicorn, SQlite3, JSON, along with integration of various financial libraries like Yahooquery, and Yfinance, this project showcases my skills in both backend development and fintech API integration. Following SOLID principles, employing design patterns like Repository, Factory and adhering to Domain-Driven Design (DDD) concepts, I've created a robust and extensible application. Comprehensive unit tests using the UnitTest framework ensure the reliability of the codebase.



This project uses the following technologies:

FastAPI - a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints
Uvicorn - a lightning-fast ASGI server, built on top of the asyncio event loop
Yahooquery - a Python library that allows you to query Yahoo Finance data in a simple and efficient way
Yfinance - a Python library that provides a simple way to download historical market data from Yahoo Finance
Matplotlib - a Python library for creating static, animated, and interactive visualizations in Python
Sqlite3 - SQLite is library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine




