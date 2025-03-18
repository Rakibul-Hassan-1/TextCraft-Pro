const express = require("express");
const { getTickets, createTicket } = require("../controllers/ticketController");

const router = express.Router();

router.get("/", getTickets);      // Get all tickets
router.post("/", createTicket);   // Create a new ticket

module.exports = router;
