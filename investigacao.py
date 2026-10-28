import pandas as pd

crimes = pd.read_csv("crime_scene.csv")
person = pd.read_csv("person.csv")
interviews = pd.read_csv("interviews.csv")
confessions = pd.read_csv("cofessions.csv")
hotel_checkins = pd.read_csv("hotel_checkins.csv")
surveillance = pd.read_csv("surveillance.csv")

cena = crimes[
    (crimes["date"].astype(str) == "19860814") &
    (crimes["location"].str.contains("Coral Bay Marina", case=False, na=False))
]
print(cena.to_string(index=False))

