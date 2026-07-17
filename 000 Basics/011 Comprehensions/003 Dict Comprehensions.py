tea_prices_inr={
    "masala tea": 30,
    "ginger tea": 25,
    "cardamom tea": 35,
    "tulsi tea": 20,
    "lemon tea": 15,
    "green tea": 40
}

tea_prices_usd={tea: price/80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)