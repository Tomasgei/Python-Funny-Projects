import pandas as pd
import numpy_financial as npf
from datetime import date

print("Zadejte výši úvěru v Kč:")
mortgage = int(input())
print("Zadejte splatnost úvěru v letech:")
years = int(input())
print("Zadejte úrokovou sazbu p.a.(např. 2.29):")
interest_input = float(input())

interest = interest_input/100
payments_year = 12
start_date = (date(2021, 1, 1))


maturity = pd.date_range(start_date, periods=years * payments_year, freq='MS')
maturity.name = "Datum"
df = pd.DataFrame(index=maturity, columns=['Měsíční Splátka', 'Splátka Jistiny', 'Splátka Úroků', 'Zbývá Doplatit'], dtype='float')
df.reset_index(inplace=True)
df.index += 1
df.index.name = "Splátka"

df["Měsíční Splátka"] = -1 * npf.pmt(interest/12, years*payments_year,mortgage)
df["Splátka Jistiny"] = -1 * npf.ppmt(interest/payments_year, df.index, years * payments_year,mortgage)
df["Splátka Úroků"]   = -1 * npf.ipmt(interest/payments_year, df.index,years * payments_year,mortgage)
df = df.round(2)

df.loc[1,"Zbývá Doplatit"] = mortgage - df.loc[1,"Splátka Jistiny"] 

for i in range(2,len(df)):
    previous_balance = df.loc[i-1,"Zbývá Doplatit"]
    principal_paid = df.loc[i,"Splátka Jistiny"]
    df.loc[i,"Zbývá Doplatit"] = previous_balance - principal_paid
    last_column = df.loc[len(df) ,"Zbývá Doplatit"] =0

print(df)
