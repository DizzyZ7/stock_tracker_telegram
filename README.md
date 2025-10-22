# stock_tracker_telegram

Бот на Python, который отслеживает цены на акции и отправляет уведомления в Telegram, когда цена достигает заданного уровня.

## Требования
* Python 3.x
* Библиотеки `yfinance`, `python-telegram-bot` и `schedule`.

## Настройка
1.  Создайте бота: Обратитесь к @BotFather в Telegram, создайте нового бота и получите его токен.
2.  Получите Chat ID: Создайте группу или канал и получите его `chat_id`.
3.  Измените настройки В файле `stock_tracker.py` замените `YOUR_BOT_TOKEN` и `YOUR_CHAT_ID` на ваши значения. Также настройте акции и целевые цены в словаре `TARGET_STOCKS`.
4.  **Установите зависимости:**
    ```sh
    pip install -r requirements.txt
    ```

## Запуск
```sh
python stock_tracker.py
