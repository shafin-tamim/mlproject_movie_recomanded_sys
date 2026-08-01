# 🎬 Movie Recommendation System

A Machine Learning-powered **Movie Recommendation System** that recommends movies similar to the one selected by the user using **Content-Based Filtering** and **Cosine Similarity**.

## 📖 Overview

This project helps users discover movies similar to their favorite ones by analyzing movie metadata such as genres, cast, crew, keywords, and overview. It uses Natural Language Processing (NLP) techniques to convert textual data into feature vectors and recommends the most similar movies.

---

## 🚀 Features

- 🎥 Recommend similar movies instantly
- 🔍 Search movies by title
- 🤖 Content-Based Recommendation
- 📊 Cosine Similarity Algorithm
- 🧹 Data preprocessing and feature engineering
- 🖥️ Simple and interactive Streamlit interface

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Pickle

---

## 📂 Project Structure

```
mlproject_movie_recomanded_sys/
│
├── data/
│   ├── movies.csv
│   └── credits.csv
│
├── app.py
├── recomandation.ipynb
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

1. Load the movie dataset.
2. Clean and preprocess the data.
3. Combine important movie features.
4. Convert text into vectors using CountVectorizer.
5. Compute Cosine Similarity.
6. Recommend the top similar movies based on user input.

---

## 📊 Dataset

The project uses the **TMDB 5000 Movie Dataset**, which includes:

- Movie Title
- Genres
- Cast
- Crew
- Keywords
- Overview
- Popularity
- Ratings

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/shafin-tamim/mlproject_movie_recomanded_sys.git
```

### Navigate to the project folder

```bash
cd mlproject_movie_recomanded_sys
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 💻 Example

**Input**

```
Avatar
```

**Recommended Movies**

- Guardians of the Galaxy
- John Carter
- Star Trek
- Jupiter Ascending
- The Fifth Element

---

## 📈 Future Improvements

- Collaborative Filtering
- Hybrid Recommendation System
- User Login System
- Movie Posters using TMDB API
- Personalized Recommendations
- Cloud Deployment

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Shafin Kader Tamim**

- GitHub: https://github.com/shafin-tamim
- LinkedIn: https://www.linkedin.com/in/sk-tamim

---

⭐ If you like this project, don't forget to give it a **Star** on GitHub!
