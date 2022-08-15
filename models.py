from config import db


class Contact(db.Model):
    """
    Contact model for storing contact information in the database.

    Attributes:
        id (int): Unique identifier for the contact.
        first_name (str): First name of the contact. Maximum length is 80 characters.
        last_name (str): Last name of the contact. Maximum length is 80 characters.
        email (str): Email address of the contact. Must be unique and maximum length is 120 characters.

    Methods:
        to_json(self): Serializes the contact information into a JSON-compatible dictionary.
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_json(self):
        """
        Serializes the contact information into a JSON-compatible dictionary.

        Returns:
            dict: A dictionary containing the contact's id, first name, last name, and email.
        """
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }