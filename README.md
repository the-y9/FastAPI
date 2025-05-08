# 🔐 FastAPI Authentication Starter Pack

A minimal yet powerful FastAPI starter for handling user **signup** and **login** using Pydantic models and clean service-based architecture.

---

## 📦 Features

- 🚀 Easy-to-use user signup and login endpoints  
- 🧱 Separation of concerns via `services` and `models`  
- 🔄 Async route handling  
- ⚙️ Ready for JWT/token integration (extendable)  

---

## 📁 Project Structure

```
project-root/
├── backend/
│   ├── services/
│   │   └── auth_service.py     # Authentication logic lives here
│   ├── models.py               # Pydantic models for request validation
│   ├── routes/
│   │   └── auth_routes.py      # API routes for login and signup
│   └── main.py                 # FastAPI app instance
```

---

## 📥 Installation

1. **Clone this starter pack:**
```bash
git clone https://github.com/your-username/fastapi-auth-starter.git
cd fastapi-auth-starter
```

2. **Install dependencies:**
```bash
pip install fastapi uvicorn
```

---

## 🛠️ Usage

### 🚀 Run the app

```bash
uvicorn backend.main:app --reload
```

---

## 🧩 API Endpoints

### 🔑 `POST /user-login`

Authenticate an existing user.

**Request Example:**
```json
{
  "username": "johndoe",
  "password": "mypassword"
}
```

**Success Response:**
```json
{
  "message": "Login successful"
}
```

---

### ✍️ `POST /user-signup`

Register a new user.

**Request Example:**
```json
{
  "username": "janedoe",
  "email": "jane@example.com",
  "password": "secure123"
}
```

**Success Response:**
```json
{
  "response": "User registered successfully"
}
```

---

## 🧱 How It Works

### 1. **Routes**
Defined in `auth_routes.py` using FastAPI's `APIRouter`.

### 2. **Services**
`auth_service.py` handles core authentication logic (e.g. DB checks, hashing).

### 3. **Models**
`UserLogin` and `UserSignup` Pydantic models validate incoming requests.

---

## ⚙️ Ready to Extend

- Add JWT authentication with `python-jose`
- Use SQLAlchemy or Tortoise ORM for persistent storage
- Integrate password hashing with `passlib`

---

## 📫 Contributing

Feel free to fork, improve, and make PRs. This is meant to be a clean, extendable base.

---

## 📝 License

MI
