from flask import Flask, jsonify, request

app = Flask(__name__)

# Data sementara untuk tiket bioskop
tickets = [
    {"id": 1, "movie_name": "Avengers: Endgame", "quantity": 100, "price": 100000},
    {"id": 2, "movie_name": "Spider-Man: Far From Home", "quantity": 150, "price": 90000}
]

# Mendapatkan semua tiket
@app.route('/tickets', methods=['GET'])
def get_tickets():
    return jsonify(tickets)

# Mendapatkan tiket berdasarkan ID
@app.route('/tickets/<int:id>', methods=['GET'])
def get_ticket(id):
    ticket = next((ticket for ticket in tickets if ticket['id'] == id), None)
    if ticket:
        return jsonify(ticket)
    else:
        return jsonify({"message": "Ticket not found"}), 404

# Menambahkan tiket baru
@app.route('/tickets', methods=['POST'])
def add_ticket():
    new_ticket = request.get_json()
    tickets.append(new_ticket)
    return jsonify(new_ticket), 201

# Mengupdate tiket berdasarkan ID
@app.route('/tickets/<int:id>', methods=['PUT'])
def update_ticket(id):
    ticket = next((ticket for ticket in tickets if ticket['id'] == id), None)
    if ticket:
        ticket.update(request.get_json())
        return jsonify(ticket)
    else:
        return jsonify({"message": "Ticket not found"}), 404

# Menghapus tiket berdasarkan ID
@app.route('/tickets/<int:id>', methods=['DELETE'])
def delete_ticket(id):
    global tickets
    tickets = [ticket for ticket in tickets if ticket['id'] != id]
    return jsonify({"message": "Ticket deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
