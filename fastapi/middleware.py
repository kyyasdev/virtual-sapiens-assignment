import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware): 
    async def dispatch(self, request: Request, call_next):
        # Start time
        start_time = time.time()
        
        # Path
        path = request.url.path
        
        # Processing
        response = await call_next(request)
        
        # Oxecution time
        execution_time = time.time() - start_time
        
        # Get status code
        status_code = response.status_code
        
        # Log info
        print(f"What our middleware sees 😀 -> Path: {path} | Execution Time: {execution_time:.4f}s | Status Code: {status_code}")
        
        return response

