
---

# 🚀 Product Listing API

![Banner](https://capsule-render.vercel.app/api?type=waving\&color=0:0ea5e9,100:6366f1\&height=200\&section=header\&text=Product%20Listing%20API\&fontSize=40\&fontColor=ffffff)

---

## 👨‍💻 Built by **Amit Kumar Tiwari**

---

## 🧠 Project Overview

A **high-performance backend system** built to browse and search through **220,000+ products** with:

* ⚡ Fast cursor-based pagination
* 🔍 Search + filtering support
* 🕒 Snapshot consistency (no duplicate/missing items)
* ☁️ Production deployment on Render
* 🐘 PostgreSQL (Neon cloud DB)

---

## 🛠️ Tech Stack

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge\&logo=postgresql\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Render](https://img.shields.io/badge/Render-000000?style=for-the-badge\&logo=render\&logoColor=white)

---

## 🌐 Live API

👉 **[https://two00000-plus-products-listing-backend.onrender.com](https://two00000-plus-products-listing-backend.onrender.com)**

---

## 📦 Dataset

* 📊 220,000+ generated products
* 🔀 Combined from JSON, JSONL, CSV datasets
* 🧹 Normalized into unified schema

---

## 🧾 Database Schema

| Field      | Type        |
| ---------- | ----------- |
| id         | bigint (PK) |
| public_id  | uuid        |
| name       | text        |
| brand      | text        |
| category   | text        |
| price      | numeric     |
| created_at | timestamp   |
| updated_at | timestamp   |

---

## ⚡ Features

### 🚀 Cursor Pagination (Production Grade)

Prevents duplicates & scales efficiently:

```sql
(updated_at, id)
```

---

### 🕒 Snapshot Consistency

Ensures stable browsing even when data changes during pagination.

---

### 🔍 Smart Search

Search across:

* Product Name
* Brand
* Category

---

### 🧰 Filtering

* Category filtering
* Cursor pagination
* Search query support

---

## 📸 API Preview

### 🔹 Get Products

```http
GET /products?limit=20
```

### 🔹 Response Example

```json
{
  "products": [
    {
      "public_id": "uuid",
      "name": "Nike Running Shoes",
      "brand": "Nike",
      "category": "Shoes",
      "price": 2999,
      "updated_at": "2026-06-23T10:10:00"
    }
  ],
  "next_cursor": "eyJ1cGRhdGVkX2F0Ijog..."
}
```

---

## 🖥️ Frontend Preview

> Add your deployed frontend screenshot here 👇

```
📌 Screenshot Placeholder:
(Add your GitHub Pages UI screenshot)
```

---

## 🧠 Key Engineering Decisions

### ⚡ Cursor Pagination

* Replaces slow OFFSET queries
* Handles large datasets efficiently

### 🧩 Stable Sorting

```sql
ORDER BY updated_at DESC, id DESC
```

### 🕒 Snapshot System

* Prevents shifting results during scrolling

---

## 🧪 Local Setup

```bash
git clone <repo-url>
cd product_listing
```

```bash
python -m venv venv
venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
uvicorn app.main:app --reload
```

---

## ☁️ Deployment

### Render Config

* Build:

```bash
pip install -r requirements.txt
```

* Start:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

---

## 🔮 Future Improvements

* ⚡ Redis caching layer
* 🔍 Elasticsearch / pg_trgm search
* 📊 Analytics dashboard
* 🔐 Auth system
* 📈 Product ranking algorithm

---

## 💬 What this project demonstrates

* Large-scale data handling (200k+ rows)
* Backend architecture design
* Pagination at production level
* Real-world API design patterns
* Deployment to cloud infrastructure

---

## 🏁 Author

### 👨‍💻 Amit Kumar Tiwari

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork it!

---

