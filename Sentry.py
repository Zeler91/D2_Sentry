import sentry_sdk
import os
from bottle import Bottle, request, route, run
from sentry_sdk.integrations.bottle import BottleIntegration

# Интеграция Sentry
sentry_sdk.init(
    dsn="https://ff8960d16b174f7295c75f3d4b67bd8a@sentry.io/1815278",
    integrations=[BottleIntegration()]
)

# app = Bottle()

@route("/")
def index():  
    return "Добавьте к адресу /success - для успешного запроса\n Добавьте к адресу /fail - для ошибочного запроса"

@route('/success')  
def success():  
    return "Запрос прошел успешно!!!"

@route('/fail')  
def fail():  
    raise RuntimeError("There is an error!")  
    return  
  
  
if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)