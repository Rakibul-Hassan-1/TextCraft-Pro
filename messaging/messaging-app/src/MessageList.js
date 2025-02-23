import axios from "axios";
import React, { useEffect, useState } from "react";
import "./MessageList.css"; // Create and import the CSS for styling

const MessageList = () => {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState({
    sender: "",
    recipient: "",
    message_text: "",
  });

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/messages/")
      .then((response) => {
        setMessages(response.data);
      })
      .catch((error) => {
        console.error("Error fetching messages:", error);
      });
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post("http://localhost:8000/api/messages/", newMessage)
      .then((response) => {
        setMessages([...messages, response.data]);
        setNewMessage({ sender: "", recipient: "", message_text: "" });
      })
      .catch((error) => {
        console.error("Error sending message:", error);
      });
  };

  return (
    <div className="message-container">
      <h1 className="header">Messages</h1>
      <ul className="message-list">
        {messages.map((msg, index) => (
          <li key={index} className="message-item">
            <div className="message-header">
              <strong>
                {msg.sender} to {msg.recipient}
              </strong>
            </div>
            <p>{msg.message_text}</p>
          </li>
        ))}
      </ul>

      <h2 className="header">Send a Message</h2>
      <form onSubmit={handleSubmit} className="message-form">
        <input
          type="text"
          placeholder="Sender"
          value={newMessage.sender}
          onChange={(e) =>
            setNewMessage({ ...newMessage, sender: e.target.value })
          }
          required
          className="input-field"
        />
        <input
          type="text"
          placeholder="Recipient"
          value={newMessage.recipient}
          onChange={(e) =>
            setNewMessage({ ...newMessage, recipient: e.target.value })
          }
          required
          className="input-field"
        />
        <textarea
          placeholder="Your message"
          value={newMessage.message_text}
          onChange={(e) =>
            setNewMessage({ ...newMessage, message_text: e.target.value })
          }
          required
          className="textarea-field"
        />
        <button type="submit" className="submit-button">
          Send
        </button>
      </form>
    </div>
  );
};

export default MessageList;
