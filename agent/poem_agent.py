# This is the "orchestrator"
from connectors.gemini_connector import get_poem_from_gemini
from connectors.db_connector import save_poem_to_db

def generate_and_save_poem(name: str, topic: str) -> str:
    """
    The main business logic.
    1. Get poem from AI.
    2. Save poem to DB.
    3. Return poem to user.
    """
    print(f"Agent: Generating poem for {name} on {topic}...")
    
    # 1. Call Gemini Connector
    poem_text = get_poem_from_gemini(name, topic)
    
    # 2. Call DB Connector
    save_poem_to_db(name=name, topic=topic, poem_text=poem_text)
    
    # 3. Return the result
    return poem_text