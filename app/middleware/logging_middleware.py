import logging
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logging.info(f"Rquest:{request.method} {request.url}")
        response = await call_next(request)
        logging.info(f'Request:{response.status_code}')
        return response
