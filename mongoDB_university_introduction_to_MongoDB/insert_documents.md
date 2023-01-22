db.accounts.insertMany(
 [
  {
    "account_id": 111333,
    "limit": 12000,
    "products": [
    "Commodity",
    "Brokerage"
    ],
    "last_updated": new Date()
  },
  {
    "account_id": 678943,
    "limit": 8000,
    "products": [
    "CurrencyService",
    "Brokerage",
    "InvestmentStock"
    ],
    "last_updated": new Date()
  },
  {
    "account_id": 321654,
    "limit": 10000,
    "products": [
    "Commodity",
    "CurrencyService"
    ],
    "last_updated": new Date()
  },
 ]
)