from fastapi import FastAPI, Request
from datetime import datetime, timezone
from middleware import LoggingMiddleware
from models import SummaryReq

app = FastAPI()

# Add middleware
app.add_middleware(LoggingMiddleware)

@app.post("/summaries")
async def create_summary(request: SummaryReq):
    text = request.text

    # Split to words & take frist 10 of them
    words = text.split()
    first_10_words = words[:10]
    
    # Join words back
    summary = " ".join(first_10_words)
    
    # Get time
    now = datetime.now(timezone.utc).isoformat()
    
    return {
        "summary": summary,
        "timestamp": now
    }

