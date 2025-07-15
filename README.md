FinDoV2 – Personal Finance Manager 🚧 In Progress 🚧
FinDoV2 is a modern, full-stack personal finance management app that helps users track expenses, manage budgets, and gain insights into their spending. Inspired by tools like Mint and YNAB, FinDoV2 offers a customizable, open-source alternative with a clean UI and smart features.

Built with Next.js, FastAPI, and PostgreSQL, it includes:

💰 Expense tracking & budgeting

📊 Interactive dashboards

🔐 Secure JWT authentication

🧠 ML-powered expense categorization

🐳 Dockerized for easy deployment

Tech Stack

- Frontend: Next.js 13, TypeScript, Tailwind CSS, React Query
- Backend: FastAPI, Python 3.9+
- Database: PostgreSQL
- ML Service: scikit-learn for expense categorization
- Containerization: Docker, Docker Compose
- Authentication: JWT
- Caching: Redis
 Prerequisites

- Docker and Docker Compose
- Node.js 18+ (for local frontend development)
- Python 3.9+ (for local backend development)

 Getting Started

 With Docker 

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FinDoV2.git
   cd FinDoV2
   ```

2. Create a `.env` file in the `backend` directory with the following content:
   ```env
   DATABASE_URL=postgresql://findo:findo123@db:5432/findo
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   REDIS_URL=redis://redis:6379/0
   ```

3. Start the application with Docker Compose:
   ```bash
   docker-compose up --build
   ```

4. The application will be available at:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - ML Service: http://localhost:8001

### Local Development

#### Backend

1. Navigate to the backend directory and create a virtual environment:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run database migrations:
   ```bash
   alembic upgrade head
   ```

4. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

#### Frontend

1. Navigate to the frontend directory and install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Create a `.env.local` file with:
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

## Project Structure

```
FinDoV2/
├── backend/               # FastAPI backend
│   ├── alembic/           # Database migrations
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── core/          # Core functionality
│   │   ├── models/        # Database models
│   │   ├── schemas/       # Pydantic models
│   │   └── services/      # Business logic
│   ├── tests/             # Backend tests
│   ├── main.py            # FastAPI application
│   └── requirements.txt   # Python dependencies
│
├── frontend/             # Next.js frontend
│   ├── public/            # Static files
│   ├── src/
│   │   ├── app/         # App router
│   │   ├── components/    # Reusable components
│   │   ├── lib/           # Utility functions
│   │   └── styles/        # Global styles
│   └── package.json       # Frontend dependencies
│
├── ml-service/           # ML service for expense categorization
│   ├── models/            # Trained ML models
│   ├── app/
│   │   ├── api/          # API endpoints
│   │   └── services/      # ML services
│   └── main.py            # FastAPI application
│
├── docker-compose.yml    # Docker Compose configuration
└── README.md             # This file
```

## API Documentation

Once the backend is running, you can access the interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Environment Variables

 Backend

- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Secret key for JWT token generation
- `ALGORITHM`: Algorithm used for JWT (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time in minutes
- `REDIS_URL`: Redis connection URL
- `ML_SERVICE_URL`: URL of the ML service (default: http://ml-service:8001)

Frontend

- `NEXT_PUBLIC_API_URL`: URL of the backend API

 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Next.js](https://nextjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [React Query](https://tanstack.com/query)
- [scikit-learn](https://scikit-learn.org/)

