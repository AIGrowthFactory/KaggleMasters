# Kaggle Master Achievements Analysis

## Introduction
This repository contains a Python script for analyzing Kaggle Master Achievements. The script processes data from Kaggle's Meta dataset, focusing on users with 'grandmaster' tiers. It further filters and analyzes profiles based on specific criteria such as country and location, specifically targeting users associated with Turkey.

## Prerequisites
Before running this script, ensure you have the following installed:
- Python 3.x
- Pandas library

## Usage
The script performs the following operations:
1. **Data Loading**: Reads user, achievements, and profiles data from Kaggle's Meta dataset.
2. **Data Processing**: Identifies users with 'grandmaster' achievements.
3. **Data Merging**: Combines user profiles with their respective achievements.
4. **Data Filtering**: Filters the merged data for users in or associated with Turkey.
5. **Alternative Data Processing**: An alternative approach to filtering the data to include users with master level achievements, excluding grandmasters.

## Script Overview
- **Library Import**: The script uses Pandas for data manipulation.
- **Data Loading**: Data is loaded from CSV files into Pandas dataframes.
- **Grandmaster Achievements Processing**: Counts the number of 'grandmaster' tiers for each user.
- **Profiles Merging**: Merges user profiles with their achievement data.
- **Country and Location-based Filtering**: Filters users based on their association with Turkey.
- **Alternative Filtering Process**: A separate section for creating a dataframe of users with master level achievements excluding grandmasters.

## Contact
For any queries or contributions, feel free to contact [atakan.ozkaya@trakyayatirim.com.tr].

---

