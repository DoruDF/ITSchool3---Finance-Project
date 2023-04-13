import yfinance


class Asset:
    def __init__(self, ticker: str, nr: float, name: str, country: str, sector: str):
        self.__ticker = ticker
        self.__nr = nr
        self.__name = name
        self.__country = country
        self.__sector = sector
        yfin = yfinance.Ticker(ticker)
        self.__info = yfin.fast_info

    @property
    def ticker(self) -> str:
        return self.__ticker

    @property
    def units(self) -> float:
        return self.__nr

    @property
    def name(self) -> str:
        return self.__name

    @property
    def country(self) -> str:
        return self.__country

    @property
    def sector(self) -> str:
        return self.__sector

    @property
    def current_price(self) -> float:
        # TODO extract the call self.__yfin.fast_info to not have duplicate code
        # Recommended, extract to a variable attached to the object
        price = self.__info["lastPrice"]
        return round(price, 2)

    @property
    def currency(self) -> str:
        currency = self.__info["currency"]
        return currency

    @property
    def closed_price(self) -> float:
        return self.__info["previousClose"]

    @property
    def fifty_day_price(self) -> float:
        return round(self.__info["fiftyDayAverage"], 2)

    # TODO: homework from models

    @property
    def today_low_price(self) -> float:
        today_low_price = self.__info["dayLow"]
        return round(today_low_price, 2)

    @property
    def today_high_price(self) -> float:
        today_high_price = self.__info["dayHigh"]
        return round(today_high_price, 2)

    @property
    def open_price(self) -> float:
        open_price = self.__info["open"]
        return round(open_price, 2)

    # TODO property, in percentage how much the price went up or down
    # current_price & closed_price

    @property
    def price_evolution(self) -> str:
        price_evolution = (
            (self.closed_price - self.current_price) / self.closed_price * 100
        )
        return f"{round(price_evolution, 2)}%"
