from db.models import SessionLocal, Poem, Base, engine

def create_db_and_tables():
    # This creates the .db file and the 'poems' table
    Base.metadata.create_all(bind=engine)

def save_poem_to_db(name: str, topic: str, poem_text: str):
    # Get a new database session
    db = SessionLocal()
    try:
        # Create a new Poem object
        db_poem = Poem(name=name, topic=topic, poem_text=poem_text)
        
        # Add it to the session and commit
        db.add(db_poem)
        db.commit()
        db.refresh(db_poem)
        print(f"Successfully saved poem for {name} to DB.")
    except Exception as e:
        print(f"Error saving to DB: {e}")
        db.rollback()
    finally:
        # Always close the session
        db.close()