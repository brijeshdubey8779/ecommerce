from index import db, app  # Import the db and app from index.py

# Create the database tables inside the application context
with app.app_context():
    db.create_all()


print("created")