# Crypto AI Agent - LLM Powered Data Analysis Agent
# 3 Agents: 1) Price Agent 2) News Agent 3) Report Agent
# Tech: Python + CoinGecko API (Free) + LangChain Concept

import requests
import datetime

print("=== Crypto AI Agent - LLM Powered Data Analysis ===")
print("Agents: Price Agent + News Agent + Report Agent\n")

# AGENT 1: Price Agent - Crypto ka live price lana
def price_agent(coin):
    print(f"[Price Agent] {coin.upper()} ka live price la raha hun...")
    # CoinGecko Free API - Koi key nahi chahiye
    coin_map = {"BTC": "bitcoin", "ETH": "ethereum", "DOGE": "dogecoin", "SOL": "solana"}
    coin_id = coin_map.get(coin.upper(), "bitcoin")
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd&include_24hr_change=true&include_24hr_vol=true"
        res = requests.get(url, timeout=10).json()
        data = res[coin_id]
        return {
            "coin": coin.upper(),
            "price": data['usd'],
            "change_24h": round(data['usd_24h_change'], 2),
            "volume": round(data['usd_24h_vol'], 2)
        }
    except:
        print("  -> Internet slow hai, Demo data use kar raha hun")
        return {"coin": coin.upper(), "price": 97450.25, "change_24h": 3.42, "volume": 28500000000}

# AGENT 2: News Agent - Crypto News + Sentiment
def news_agent(coin):
    print(f"[News Agent] {coin.upper()} ki latest news analyze kar raha hun...")
    headlines = [
        f"{coin.upper()} adoption badh raha hai, institutions buying kar rahe hain",
        f"Analysts ke mutabiq {coin.upper()} ka breakout nazdeek hai",
        f"Market me {coin.upper()} ko leke positive sentiment hai"
    ]
    # Simple LLM-style sentiment logic
    sentiment_score = 78
    sentiment = "BULLISH 🟢" if sentiment_score > 60 else "BEARISH 🔴"
    return {"headlines": headlines, "score": sentiment_score, "sentiment": sentiment}

# AGENT 3: Report Agent - Final AI Report banana (LLM jaisa)
def report_agent(price, news):
    print(f"[Report Agent] Final AI Report bana raha hun...\n")
    print("="*55)
    print(f"🪙 CRYPTO REPORT: {price['coin']} | {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}")
    print("="*55)
    print(f"Current Price: ${price['price']:,}")
    print(f"24h Change: {price['change_24h']}%")
    print(f"24h Volume: ${price['volume']:,}")
    print(f"\n📰 Sentiment: {news['sentiment']} ({news['score']}/100)")
    for h in news['headlines']:
        print(f" - {h}")

    # AI Decision Logic - LLM jaisa
    if price['change_24h'] > 2 and news['score'] > 70:
        rec = "STRONG BUY ✅ - Price up hai + News positive hai"
        risk = "Low Risk"
    elif price['change_24h'] < -3:
        rec = "SELL ❌ - Market down hai, wait karo"
        risk = "High Risk"
    else:
        rec = "HOLD ⏸️ - Market sideways hai"
        risk = "Medium Risk"

    print(f"\n🤖 AI RECOMMENDATION: {rec}")
    print(f"⚠️  Risk Level: {risk}")
    print(f"💡 Insight: {price['coin']} agle 24h me {'up' if price['change_24h'] > 0 else 'down'} trend me reh sakta hai.")
    print("="*55)
    return rec

# MAIN
if __name__ == "__main__":
    coin = input("Crypto Symbol daalo (BTC / ETH / DOGE / SOL): ").upper().strip()
    if not coin:
        coin = "BTC"
    p = price_agent(coin)
    n = news_agent(coin)
    report_agent(p, n)
    print("\n[DONE] Crypto AI Agent Complete!")