const mongoose = require("mongoose");

const ticketSchema = new mongoose.Schema({
  eventName: { type: String, required: true },
  price: { type: Number, required: true },
  availableSeats: { type: Number, required: true },
  date: { type: Date, required: true },
});

const Ticket = mongoose.model("Ticket", ticketSchema);
module.exports = Ticket;
