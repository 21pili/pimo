# pimo/main.py

from pimo.labor_market import LaborMarket

def main():
    market = LaborMarket(s=1, theta=2.0, sigma=3.0, duration=4.0)
    print("Matching flow probability:", market.matching())
    print("Finding flow probability:", market.find())

if __name__ == "__main__":
    main()
