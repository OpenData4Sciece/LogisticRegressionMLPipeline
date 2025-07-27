
# Logistic Regression ML Pipeline with FastAPI 🚀

A clean and modern ML microservice for logistic regression using FastAPI. Built with scalability, explainability, and deployability in mind.

## 🔧 Project Structure

```
logistic-regression-fastapi/
│
├── app/
│   ├── main.py           # FastAPI app entrypoint
│   ├── model.py          # Model loading and prediction logic
│   └── schemas.py        # Pydantic request/response models
│
├── models/
│   └── logistic_model.joblib   # Pretrained logistic regression model
│
├── notebooks/
│   └── train_model.ipynb       # Jupyter notebook for training and evaluation
│
├── Dockerfile           # Containerisation setup
└── requirements.txt     # Python dependencies
```

## 🧪 Training

The `notebooks/train_model.ipynb` trains a simple logistic regression classifier and exports the model.

## ▶️ Run API

```bash
uvicorn app.main:app --reload
```

## 🐳 Docker

```bash
docker build -t logistic-api .
docker run -d -p 8000:8000 logistic-api
```

## ✨ Author

[![Pierre-Henry Soria](https://avatars0.githubusercontent.com/u/1325411?s=200)](https://ph7.me)

Made with ❤️ by **[Pierre-Henry Soria](https://pierrehenry.be)** — an AI Data Scientist & Senior Software Engineer. Incredibly passionate about AI, machine learning, data science, and emerging technologies. I could happily talk all night about programming and IT with anyone who’s keen. Roquefort 🧀, ristretto ☕️, and dark chocolate lover! 😋

[![@phenrysay](https://img.shields.io/badge/x-000000?style=for-the-badge&logo=x)](https://x.com/phenrysay)  [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pH-7)  [![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/cWBuZ4DXGK4)  [![Bluesky](https://img.shields.io/badge/bluesky-1e90ff?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDAwMDAwIiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAzMiAzMiIgd2lkdGg9IjI0cHgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTMwIDZsLTIuOTk5LTEuNjY2TDMyIDMuMzQgMjMuMTg5IDAgMTYuMDA2IDUuMzQgOC44MTMgMCAwIDMuMzQgNC45OTkgNC4zMzQgMCA2bDUuMDAxIDQuODAzTDQgMjAuODFWMjRsNS4wMDEtMS42NjZMMTYgMjhMMjIuOTk5IDIyLjM0IDMyIDI0di0zLjE4OUwyNy4wMDIgMTIgMzAgNiIgLz48L3N2Zz4=)](https://bsky.app/profile/ph7s.bsky.social "Bluesky Profile")
