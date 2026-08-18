# CarValue Predictor: Machine Learning Car Price Prediction App

A full-stack machine learning web application designed to predict used car market values based on specifications like mileage, year, make, model, and condition.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Database Design](#database-design)
- [API Endpoints](#api-endpoints)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Deployment](#deployment)
- [Future Improvements](#future-improvements)
- [Credits](#credits)
- [License](#license)

---

## Overview

### Motivation
Built to solve the uncertainty of pricing used vehicles, this project empowers buyers and sellers with data-driven price estimates derived from real market trends and regression modeling.

### Objective
To provide an interactive tool where users input car attributes (mileage, year, fuel type, transmission) and receive an instant, accurate machine-learning-powered price prediction alongside historical comparison metrics.

### Learning Outcomes
- Trained and evaluated a regression machine learning model using Python (Scikit-Learn/Pandas)
- Developed a RESTful API wrapper around a trained ML model using Flask/FastAPI
- Implemented complete CRUD operations for saving user prediction searches
- Connected a responsive frontend interface to a Python backend service
- Deployed a full-stack ML application

---

## Features

- **Instant Price Prediction:** Input vehicle specs and get immediate ML-driven valuation estimates.
- **User Authentication:** Secure registration and login to save past predictions and search history.
- **Prediction History & Dashboard:** Track previously searched cars and view market depreciation insights.
- **Data Visualization:** Interactive charts comparing car mileage vs. predicted resale price.
- **Fully Responsive Design:** Optimized for mobile devices, tablets, and desktop browsers.

---

## Tech Stack

### Core Language 

python 3

### Machine Learning & Data Science Libraries 

scikit-learn 1.4.2
pandas
numpy
matplotlib
joblib

### Specific ML Components (from scikit-learn)

gradient boosting regressor
ordinal encoder
column transformer
selectpercentile

### Web Framework

stream lit

### Development Environment

jupyter notebook
venv (virtual environment)

### Storage & Infrastructure

azurite
queue storage

### Data 

csv files
kaggle / marketcheck dataset 

---

 
### Folder Structure

```text
client/
server/
  ├── ml_models/
  │         └── price_model.pkl
  ├── routes/
  │         └── predictionRoutes.py
  ├── controllers/
  │         └── predictionController.py
  ├── utils/
  │         └── preprocessing.py
  └── app.py
