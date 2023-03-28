import yahooquery
from domain.asset.asset import Asset


class AssetFactory:
    def make_new(self, ticker: str) -> Asset:
        # Todo error handling & tests
        t = yahooquery.Ticker(ticker)
        print(t.summary_detail)
        print(t.summary_profile)
        profile = t.summary_profile[ticker]
        name = profile["longBusinessSummary"].split(" ")[0:2]
        country = profile["country"]
        sector = profile["sector"]
        return Asset(
            ticker=ticker,
            nr=0,
            name=name,
            country=country,
            sector=sector,
        )
