from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AdPrediction(Base):

    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)

    ad_network = Column(String)
    game_genre = Column(String)
    campaign_type = Column(String)

    install_probability = Column(Float)
    bid = Column(Float)
    expected_revenue = Column(Float)