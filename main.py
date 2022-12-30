import yfinance as yf
import boto3
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/updateData', methods=['POST'])
def updateData():

    if request.method == 'POST':
        ticker = request.form['ticker']
        db = boto3.resource('dynamodb', region_name='us-west-2')
        table = db.Table('Financials')

        info = yf.Ticker(ticker).info
        for key, val in info.items():
            info[key] = str(val)

        table.put_item(Item={
            'ticker': ticker,
            'exchange': info['exchange'],
            'sector': info['sector'],
            'fullTimeEmployees': info['fullTimeEmployees'],
            'longBusinessSummary': info['longBusinessSummary'],
            'city': info['city'],
            'state': info['state'],
            'country': info['country'],
            'website': info['website'],
            'address1': info['address1'],
            'industry': info['industry'],
            'ebitdaMargins': info['ebitdaMargins'],
            'profitMargins': info['profitMargins'],
            'grossMargins': info['grossMargins'],
            'operatingMargins': info['operatingMargins'],
            'operatingCashflow': info['operatingCashflow'],
            'revenueGrowth': info['revenueGrowth'],
            'ebitda': info['ebitda'],
            'grossProfits': info['grossProfits'],
            'freeCashflow': info['freeCashflow'],
            'currentPrice': info['currentPrice'],
            'earningsGrowth': info['earningsGrowth'],
            'currentRatio': info['currentRatio'],
            'returnOnAssets': info['returnOnAssets'],
            'debtToEquity': info['debtToEquity'],
            'returnOnEquity': info['returnOnEquity'],
            'totalCash': info['totalCash'],
            'totalDebt': info['totalDebt'],
            'totalRevenue': info['totalRevenue'],
            'totalCashPerShare': info['totalCashPerShare'],
            'financialCurrency': info['financialCurrency'],
            'revenuePerShare': info['revenuePerShare'],
            'quickRatio': info['quickRatio'],
            'shortName': info['shortName'],
            'longName': info['longName'],
            'exchangeTimezoneName': info['exchangeTimezoneName'],
            'exchangeTimezoneShortName': info['exchangeTimezoneShortName'],
            'market': info['market'],
            'enterpriseToRevenue': info['enterpriseToRevenue'],
            'enterpriseToEbitda': info['enterpriseToEbitda'],
            '52WeekChange': info['52WeekChange'],
            'forwardEps': info['forwardEps'],
            'sharesOutstanding': info['sharesOutstanding'],
            'bookValue': info['bookValue'],
            'sharesShort': info['sharesShort'],
            'sharesPercentSharesOut': info['sharesPercentSharesOut'],
            'heldPercentInstitutions': info['heldPercentInstitutions'],
            'netIncomeToCommon': info['netIncomeToCommon'],
            'trailingEps': info['trailingEps'],
            'lastDividendValue': info['lastDividendValue'],
            'priceToBook': info['priceToBook'],
            'heldPercentInsiders': info['heldPercentInsiders'],
            'yield': info['yield'],
            'shortRatio': info['shortRatio'],
            'sharesShortPreviousMonthDate': info['sharesShortPreviousMonthDate'],
            'floatShares': info['floatShares'],
            'beta': info['beta'],
            'enterpriseValue': info['enterpriseValue'],
            'earningsQuarterlyGrowth': info['earningsQuarterlyGrowth'],
            'priceToSalesTrailing12Months': info['priceToSalesTrailing12Months'],
            'forwardPE': info['forwardPE'],
            'shortPercentOfFloat': info['shortPercentOfFloat'],
            'trailingAnnualDividendRate': info['trailingAnnualDividendRate'],
            'dividendRate': info['dividendRate'],
            'exDividendDate': info['exDividendDate'],
            'trailingPE': info['trailingPE'],
            'marketCap': info['marketCap'],
            'fiftyTwoWeekHigh': info['fiftyTwoWeekHigh'],
            'fiftyTwoWeekLow': info['fiftyTwoWeekLow'],
            'dividendYield': info['dividendYield'],
            'logo_url': info['logo_url'],
            'regularMarketPrice': info['regularMarketPrice'],
            'trailingPegRatio': info['trailingPegRatio'],
            'pegRatio': info['pegRatio'],
        })
        return {}


if __name__ == '__main__':
    app.run()
