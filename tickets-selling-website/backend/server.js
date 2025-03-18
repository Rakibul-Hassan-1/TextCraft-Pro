const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json()); // Allows JSON body parsing

const PORT = 5000;

// ✅ Add this test route
app.get("/api/data", (req, res) => {
  res.json({ message: "Hello from Backend!" });
});

// Start Server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
