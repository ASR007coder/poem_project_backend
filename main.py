import sys
import os
import uvicorn

# --- THIS IS THE FIX ---
# Add the project's root folder (simple_backend) to the Python path
# This must be at the very top of main.py
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(FILE_DIR)
# --- END OF FIX ---


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# These imports will NOW work
from db.models import PoemRequest, PoemResponse
from agent.poem_agent import generate_and_save_poem
from connectors.db_connector import create_db_and_tables

# Create the FastAPI app
app = FastAPI()

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    print("Server starting up... Creating database tables.")
    create_db_and_tables()

# --- API Endpoint ---
@app.post("/generate-poem", response_model=PoemResponse)
async def handle_generate_poem(request: PoemRequest):
    print(f"API: Received request from {request.name}")
    
    # 1. Call the agent
    poem = generate_and_save_poem(request.name, request.topic)
    
    # 2. Return the response
    return PoemResponse(poem=poem)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)