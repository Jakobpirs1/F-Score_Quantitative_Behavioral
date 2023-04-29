from alpha_vantage.fundamentaldata import FundamentalData
Key= 'CXSKPS11U4UYHKYI'
symbol = input( 'Ticker : ')
period= input('Period- annual, quarterly: ')
statement = input('Statement- balance sheet, income statement, cash flow : ')
fd = FundamentalData(Key, output_format = 'pandas')
import pandas as pd
                     
ticker = ['GOOGL']  # ticker

# income statement of the company |
IS1 = fd.get_income_statement_annual(ticker)
IS = IS1[0].T[2:]
IS.columns = list(IS1[0].T.iloc[0])
IS


#BALANCE SHEET OF THE COMPANY
BS1 = fd.get_balance_sheet_annual(ticker)
BS = BS1[0].T[2:]
BS.columns = list(BS1[0].T.iloc[0])
BS


#CASHFLOW STATEMENT OF THE COMPANY
CS1 = fd.get_cash_flow_annual(ticker)
CS = CS1[0].T[2:]
CS.columns = list(CS1[0].T.iloc[0])
CS

#DEF FUNCTONS FOR THE DELTA FACTORS

def net_income():
    df=IS
    return float(df.loc['netIncome'][0])

def ROA():
    df=BS
    p,q= float(df.loc['totalAssets'][0]), float(df.loc['totalAssets'][1])
    av_assets=(p+q)/2
    return net_income()/av_assets

def OCF():
    df=CS
    return float(df.loc['operatingCashflow'][0])

def LTdebt():
    df=BS
    p,q=float(df.loc['longTermDebt'][0]),float(df.loc['longTermDebt'][1])
    return q-p

def current_ratio():
    df=BS
    p,q=float(df.loc['totalCurrentAssets'][0]),float(df.loc['totalCurrentAssets'][1])
    r,s=float(df.loc['totalCurrentLiabilities'][0]),float(df.loc['totalCurrentLiabilities'][1])
    current_ratio1,current_ratio2=p/r,q/s
    return current_ratio1-current_ratio2

def new_shares():
    return float(BS.loc['commonStock'][0]) - float(BS.loc['commonStock'][1])

def gross_margin():
    df=IS
    gross_margin_this = float(IS.loc['grossProfit'][0])/float(IS.loc['totalRevenue'][0])
    gross_margin_last = float(IS.loc['grossProfit'][1])/float(IS.loc['totalRevenue'][1])
    return gross_margin_this - gross_margin_last

def Asset_Turnover_Ratio():
    df1=IS
    df2=BS
    p,q,s=float(df2.loc['totalAssets'][0]),float(df2.loc['totalAssets'][1]),float(df2.loc['totalAssets'][2])
    av_assets1=(p+q)/2
    av_assets2=(q+s)/2
    atr1=float(df1.loc['totalRevenue'][0])/av_assets1
    atr2=float(df1.loc['totalRevenue'][1])/av_assets2
    return atr1-atr2


#F-SCORE CALCULATION

def Pietroski_Score():
    Pscore=0
    if net_income()>0:
        Pscore+=1
    if ROA()>0:
        Pscore+=1
    if OCF()>0:
        Pscore+=1
    if LTdebt()>0:
        Pscore+=1
    if current_ratio()>0:
        Pscore+=1
    if new_shares()>0:
        Pscore+=1
    if gross_margin()>0:
        Pscore+=1
    if Asset_Turnover_Ratio()>0:
        Pscore+=1
    return Pscore

Pietroski_Score()