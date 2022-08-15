from flask import request, jsonify
from config import app, db
from models import Contact
from typing import List, Dict, Tuple


@app.route("/contacts", methods=["GET"])
def get_contacts() -> jsonify:
    """
    Endpoint to retrieve all contacts from the database.

    This endpoint handles GET requests to the "/contacts" URL, querying the database for all contacts,
    serializing them into JSON format using the `to_json` method of the `Contact` model, and returning
    the list of contacts as a JSON response.

    Returns:
        A Flask JSON response containing a list of all contacts in the database, each represented as a JSON object.
    """
    contacts: List[Contact] = Contact.query.all()
    json_contacts: List[Dict[str, str | int]] = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})


@app.route("/create_contact", methods=["POST"])
def create_contact() -> Tuple[jsonify, int]:
	"""
	Endpoint to create a new contact in the database.

	This endpoint handles POST requests to the "/create_contact" URL. It expects a JSON payload with
	"firstName", "lastName", and "email" fields. If any of these fields are missing, it returns a 400
	Bad Request response.

	If all fields are present, it attempts to create a new Contact object and save it to the database.
	If the operation is successful, it returns a 201 Created response with a success message. If there
	is an exception (e.g., due to a duplicate email), it returns a 400 Bad Request response with the
	error message.

	Returns:
		A Flask JSON response. On success, it returns a message indicating the user was created and
		a 201 status code. On failure, due to missing fields or exceptions, it returns an error message
		and a 400 status code.
	"""
	first_name: str = request.json.get("firstName")
	last_name: str = request.json.get("lastName")
	email: str = request.json.get("email")

	if not first_name or not last_name or not email:
		return jsonify({"message": "You must include a first name, last name and email"}), 400

	new_contact: Contact = Contact(first_name=first_name, last_name=last_name, email=email)
	try:
		db.session.add(new_contact)
		db.session.commit()
	except Exception as e:
		return jsonify({"message": str(e)}), 400

	return jsonify({"message": "User created!"}), 201


@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id: int) -> Tuple[jsonify, int]:
    """
    Endpoint to update an existing contact in the database.

    This endpoint handles PATCH requests to the "/update_contact/<int:user_id>" URL, where `user_id` is the
    unique identifier of the contact to be updated. It looks up the contact by `user_id`. If the contact is
    not found, it returns a 404 Not Found response.

    The request should include a JSON payload with any of the following optional fields: "firstName",
    "lastName", and "email". The endpoint updates the contact with any provided fields, leaving other fields
    unchanged if they are not specified in the request.

    After updating the contact in the database, it commits the changes and returns a 200 OK response with a
    success message.

    Parameters:
        user_id (int): The unique identifier of the contact to be updated.

    Returns:
        A Flask JSON response. On success, it returns a message indicating the user was updated and a 200
        status code. If the user is not found, it returns a 404 Not Found response.
    """
    contact: Contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404

    data: dict = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "User updated."}), 200


@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id: int) -> Tuple[jsonify, int]:
    """
    Endpoint to delete an existing contact from the database.

    This endpoint handles DELETE requests to the "/delete_contact/<int:user_id>" URL, where `user_id` is the
    unique identifier of the contact to be deleted. It attempts to find the contact by `user_id` in the database.
    If the contact is found, it is deleted from the database, and the changes are committed.

    Parameters:
        user_id (int): The unique identifier of the contact to be deleted.

    Returns:
        A Flask JSON response. If the contact is successfully deleted, it returns a message indicating the
        user was deleted and a 200 status code. If the contact is not found, it returns a 404 Not Found response
        with an appropriate message.
    """
    contact: Contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)