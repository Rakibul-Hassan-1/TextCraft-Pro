tickets-selling-website/  
│── backend/                # Node.js + Express backend  
│   ├── server.js           # Main server file  
│   ├── routes/             # API routes (ticket, user, payment)  
│   ├── controllers/        # Business logic for routes  
│   ├── models/             # Data models (if using a database)  
│   ├── config/             # Config files (DB, Firebase, Stripe)  
│   ├── middleware/         # Authentication & other middleware  
│   └── package.json        # Backend dependencies  
│  
│── frontend/               # React frontend  
│   ├── public/             # Static assets  
│   ├── src/                # Source files  
│   │   ├── components/     # Reusable UI components  
│   │   ├── pages/          # Different pages (Home, Events, Checkout)  
│   │   ├── context/        # Global state management  
│   │   ├── api/            # API calls to backend  
│   │   ├── App.js          # Main React component  
│   │   ├── index.js        # Entry point  
│   └── package.json        # Frontend dependencies  
│  
└── README.md               # Project documentation  
