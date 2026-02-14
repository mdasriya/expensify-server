from fastapi import FastAPI
from app.core.database import Base, engine

# Import models so tables are created
from app.modules.auth.auth_model import User

# Import routers
from app.modules.auth.auth_routes import router as auth_router

# Create FastAPI app
app = FastAPI(
    title="Expensify API",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_router)


# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Expensify API is running 🚀"
    }
