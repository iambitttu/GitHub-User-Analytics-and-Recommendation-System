import streamlit as st
import pymongo
import pandas as pd
import plotly.express as px

# MongoDB connection details
MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "github_users"
MONGO_COLLECTION = "user_data"

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]


# Streamlit app
def app():
    st.title("GitHub User Analytics")

    # User search functionality
    username = st.text_input("Enter GitHub username:")
    if username:
        user_data = collection.find_one({"login": username})
        if user_data:
            # Display user statistics
            st.subheader("User Statistics")
            user_stats = {
                "Name": user_data['name'],
                "Username": user_data['login'],
                "Bio": user_data['bio'],
                "Public Repositories": user_data['public_repos'],
                "Followers": user_data['followers'],
                "Following": user_data['following']
            }
            st.dataframe(pd.DataFrame(user_stats.items(), columns=["Attribute", "Value"]))

            # Data processing and visualization
            languages = user_data.get("languages", {})
            if languages:
                languages_df = pd.DataFrame.from_dict(languages, orient="index", columns=["bytes"])
                languages_df = languages_df.reset_index().rename(columns={"index": "language"})
                st.subheader("Programming Languages Used")
                fig = px.bar(languages_df, x="language", y="bytes", title="Language Breakdown")
                st.plotly_chart(fig, use_container_width=True)  # Adjust chart size
        else:
            st.write(f"No data found for user: {username}")


if __name__ == "__main__":
    app()
