from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import models so SQLAlchemy can detect them
from models.organization import Organization
