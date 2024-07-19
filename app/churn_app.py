"""FastAPI-приложение для модели оттока."""

from fastapi import FastAPI, Body
from fast_api_handler import FastApiHandler

"""
Пример запуска из директории mle-sprint3/app:
uvicorn churn_app:app --reload --port 8081 --host 0.0.0.0

Для просмотра документации API и совершения тестовых запросов зайти на http://127.0.0.1:8081/docs

Если используется другой порт, то заменить 8081 на этот порт

Запрос:
curl -X 'POST' \
  'http://localhost:8081/api/churn/?user_id=123' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "gender": 1,
  "SeniorCitizen": 0,
  "Partner": 0,
  "Dependents": 0,
  "Type": 0.5501916796819537,
  "PaperlessBilling": 1,
  "PaymentMethod": 0.2192247621752094,
  "MonthlyCharges": 50.8,
  "TotalCharges": 288.05,
  "MultipleLines": 0,
  "InternetService": 0.3437455629703251,
  "OnlineSecurity": 0,
  "OnlineBackup": 0,
  "DeviceProtection": 0,
  "TechSupport": 1,
  "StreamingTV": 0,
  "StreamingMovies": 0,
  "days": 245,
  "services": 2
}'
"""

# создаём FastAPI-приложение 
app = FastAPI()

# создаём обработчик запросов для API
app.handler = FastApiHandler()


@app.post("/api/churn/") 
def get_prediction_for_item(user_id: str, model_params: dict):
    """Функция для получения вероятности оттока пользователя.

    Args:
        user_id (str): Идентификатор пользователя.
        model_params (dict): Параметры пользователя, которые нужно передать в модель.

    Returns:
        dict: Предсказание, уйдёт ли пользователь из сервиса.
    """
    all_params = {
        "user_id": user_id,
        "model_params": model_params
    }
    return app.handler.handle(all_params)
