# Importing necessary libraries
import pandas as pd

# Loading data from CSV files
users_df = pd.read_csv("../input/meta-kaggle/Users.csv")
achievements_df = pd.read_csv("../input/meta-kagglemaster-achievements-snapshot/MasterAchievements.csv")
profiles_df = pd.read_csv("../input/meta-kagglemaster-achievements-snapshot/MasterProfiles.csv")

# Processing achievements data to count 'grandmaster' tiers
achievements_df['GM_tier_count'] = achievements_df[achievements_df.astype(str) == 'grandmaster'].count(axis=1)
gm_achievements_df = achievements_df[achievements_df['GM_tier_count'] > 0]

# Merging profiles with users who have grandmaster achievements
gm_profiles_df = gm_achievements_df.merge(profiles_df)

# Filtering data for specific countries and locations
turkey_gm_profiles_df = gm_profiles_df[(gm_profiles_df['Country'].isin(['Turkey', 'Türkiye'])) |
                                       (gm_profiles_df['Location'].str.contains('Turkey', na=False))]

# Extracting and resetting index of the first column
user_ids = turkey_gm_profiles_df.iloc[:, 0].astype(str)
user_ids = user_ids.reset_index(drop=True)

# Additional filtering process (if needed)
# This section seems to be a continuation or alternative of the above filtering process
# Ensure that this part is needed or integrate appropriately with the above steps
gm_profiles_alternative_df = achievements_df.merge(profiles_df)
alternative_filtered_df = gm_profiles_alternative_df[(gm_profiles_alternative_df['Country'].isin(['Turkey', 'Türkiye'])) |
                                                     (gm_profiles_alternative_df['Location'].str.contains('Turkey', na=False))]
mask = alternative_filtered_df.set_index(['UserName']).index.isin(turkey_gm_profiles_df.set_index(['UserName']).index)
distinct_profiles_df = alternative_filtered_df[~mask] # This line filters the dataset to create a dataframe of users who have master level achievements but are not grandmasters

