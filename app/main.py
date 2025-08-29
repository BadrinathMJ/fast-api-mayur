from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth, routes_predict
from app.middleware.logging_middleware import LoggingMiddleWare
from app.core.exceptions import register_exception_handlers

app = FastAPI(title='Car Price Prediction API')

#Linke Middleware
app.add_middleware(LoggingMiddleWare)

#Link endo points
app.include_router(routes_auth.router, tags = ['Auth'])
app.include_router(routes_predict.router, tags=['Prediction'])

#Monitoring usinh Prometheus
Instrumentator().instrument(app).expose(app)

#Add exception handler
register_exception_handlers(app)