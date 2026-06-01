import pandas as pd

# Candidate resume data
resume_data = {
    "Name": ["Rahul", "Anjali", "Kiran", "Sneha", "Vikram"],

    "Profile": [
        "Python developer with experience in machine learning and data analysis",
        "Web developer skilled in HTML CSS JavaScript",
        "Data scientist with Python machine learning and deep learning experience",
        "Software engineer with Java and backend development",
        "Python programmer with data analysis skills"
    ]
}

# Job requirements
job_skills = ["Python", "Machine Learning", "Data Analysis"]

# Create DataFrame
df = pd.DataFrame(resume_data)

match_scores = []

# Calculate matching score
for profile in df["Profile"]:

    score = sum(skill.lower() in profile.lower() for skill in job_skills)

    match_scores.append(score)

# Add score and percentage columns
df["Match Score"] = match_scores
df["Match %"] = (df["Match Score"] / len(job_skills)) * 100

# Sort candidates by score
ranked_df = df.sort_values(by="Match Score", ascending=False)

# Best candidate
top_candidate = ranked_df.iloc[0]

# Output
print("Top Resume Selected\n")

print("Candidate:", top_candidate["Name"])
print("Profile:", top_candidate["Profile"])
print("Match Score:", top_candidate["Match Score"])
print("Match Percentage:", top_candidate["Match %"], "%")