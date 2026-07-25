from app.extensions import db

# Create a new database model
class Submission(db.Model):
    # Tells SQLAlchemy what the database table should be called
    __tablename__ = "submissions"

    # ID
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    #Name
    name = db.Column(
        db.String(100),
        nullabel=False
    )

    #Email
    email = db.Column(
        db.String(255),
        nullable=False
    )

    #Message
    message = db.Column(
        db.Text(1000),
        nullable=False
    )