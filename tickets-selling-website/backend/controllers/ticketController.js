const Ticket = require("../models/Ticket");

// Get All Tickets
const getTickets = async (req, res) => {
  try {
    const tickets = await Ticket.find();
    res.json(tickets);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Create a New Ticket
const createTicket = async (req, res) => {
  try {
    const { eventName, price, availableSeats, date } = req.body;
    const newTicket = new Ticket({ eventName, price, availableSeats, date });
    await newTicket.save();
    res.status(201).json(newTicket);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

module.exports = { getTickets, createTicket };
