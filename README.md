
# 🚀 Artera Technical Test REST API

Welcome to the official repository for the Artera technical test! Follow this guide to set up and run the app.

---

## 🛠️ Requirements

Before you start, make sure you have the following:

- [Docker](https://docs.docker.com/install/)

## 📥 Clone the Repository

To clone the repository, run:

```bash
git clone https://github.com/Artera-LTD/technical-test-rest-api
```

---

## 🚀 Getting Started

Here's how to set up and run the application.

### 1️⃣ Start PostgreSQL

Start the local PostgreSQL instance using Docker:

```bash
make run_postgres_local
```

### 2️⃣ Configure Environment Variables

Copy the example environment file and adjust the configuration as needed:

```bash
cp .env.example .env
```

### 3️⃣ Install Python Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up the Django Backend

Navigate to the Django backend directory:

```bash
cd src/artera-rest-api
```

#### 4.1 Apply Database Migrations

Set up the database schema with migrations:

```bash
python manage.py migrate
```

#### 4.2 Populate Demo Data (Optional)

Load demo data for frontend testing:

```bash
python manage.py seed_artworks
```

#### 4.3 Run the Django Development Server

Start the Django backend server:

```bash
python manage.py runserver
```

>**Backend API Endpoint:** [http://localhost:8000](http://localhost:8000)

### 5️⃣ Start the Frontend

Navigate to the frontend directory:

```bash
cd src/artera-next-frontend
```

#### 5.1 Install Node.js Dependencies

Install the required frontend packages:

```bash
npm install
```

#### 5.2 Run the Next.js Development Server

Start the frontend server:

```bash
npm run dev
```

> **Frontend Endpoint:** [http://localhost:3000](http://localhost:3000)

---

## 🌐 Quick Links

- **Backend (API)**: [http://localhost:8000](http://localhost:8000)
- **Frontend (UI)**: [http://localhost:3000](http://localhost:3000)

---

Now you're all set to explore and develop with the Artera technical test app! 🚀
