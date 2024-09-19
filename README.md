# GitHub-User-Analytics-and-Recommendation-System

## Overview

This project aims to collect data from GitHub users, store it in MongoDB, and create an analytics dashboard to understand users' technical strengths and weaknesses. Additionally, a recommendation system is built to suggest users with similar technological interests.

## Features

### Data Collection

- Utilizes the GitHub API to fetch user data, handle API rate limits, and incorporate error-handling strategies.
- Stores collected data in MongoDB in a structured format.
- Implements batch collection to fetch at least 1000 users' data efficiently.

### Analytics Dashboard

- Retrieves user data from MongoDB for analysis.
- Displays user statistics such as the number of repositories, commits, and languages used.
- Visualizes data with graphs showing popular languages, average commits, etc.
- Provides individual profile analytics to visualize strengths and weaknesses in terms of technologies used.
- Offers interactivity allowing users to search for specific GitHub profiles and view analytics.
- Hosts and deploys the dashboard onto a web app server (e.g., Heroku, Render.com).

### Recommendation System

- Processes user data to derive features such as languages used and frequency of commits.
- Builds a recommendation system using techniques such as collaborative filtering or cosine similarity to suggest users with similar interests.
- Integrates the recommendation system into the dashboard, allowing users to view and explore recommendations.

## Setup

1. Clone the repository:

    ```
    git clone https://github.com/your-username/github-analytics-recommendation.git
    ```

2. Install dependencies:

    ```
    cd github-analytics-recommendation
    pip install -r requirements.txt
    ```

3. Run the application:

    ```
    python app.py
    ```

## Usage

1. Access the dashboard by visiting [http://localhost:8050](http://localhost:8050) in your web browser.
2. Enter a GitHub username in the input field and click the "Search" button to view analytics for the user.
3. Explore different visualizations and features provided by the dashboard.
