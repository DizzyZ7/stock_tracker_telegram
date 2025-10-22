import yfinance as yf
from telegram import Bot
import asyncio
import schedule
import time

# --- Настройки ---
# Замените на свой токен и chat_id
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

# Акции для отслеживания
# Формат: {'тикер': целевая_цена}
TARGET_STOCKS = {
    "AAPL": 180,
    "MSFT": 450,
    "GOOG": 150
}

# --- Логика программы ---
async def send_telegram_message(message: str):
    """Отправляет сообщение в Telegram."""
    try:
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Сообщение успешно отправлено: {message}")
    except Exception as e:
        print(f"Ошибка при отправке сообщения в Telegram: {e}")

def check_stock_price():
    """Проверяет цены акций и отправляет уведомления."""
    print("Проверка цен акций...")
    for ticker, target_price in TARGET_STOCKS.items():
        try:
            stock = yf.Ticker(ticker)
            current_price = stock.history(period="1d")['Close'].iloc[-1]
            
            print(f"Акция: {ticker}, Текущая цена: {current_price:.2f}, Целевая цена: {target_price}")

            if current_price >= target_price:
                message = f"✅ Акция {ticker} достигла целевой цены {target_price}! Текущая цена: {current_price:.2f}"
                asyncio.run(send_telegram_message(message))
            else:
                message = f"⬇️ Акция {ticker} ниже целевой цены. Текущая: {current_price:.2f}, Целевая: {target_price}"
                # Можно настроить, чтобы отправлялось только при достижении цели
                # или сделать отправку редких отчетов.
                print(message)
        except Exception as e:
            print(f"Ошибка при получении данных для акции {ticker}: {e}")

def main():
    """Запускает планировщик задач."""
    # Запуск проверки каждую минуту
    schedule.every(1).minutes.do(check_stock_price)

    # Бесконечный цикл для выполнения запланированных задач
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

