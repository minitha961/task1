import requests
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)
data = response.json()

sorted_data = sorted(data, key=lambda x: x['cases'], reverse=True)
top_10 = sorted_data[:10]

countries = [country['country'] for country in top_10]
cases = [country['cases'] for country in top_10]
deaths = [country['deaths'] for country in top_10]
recovered = [country['recovered'] for country in top_10]

sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(x=countries, y=cases, palette="Blues_d")
plt.xlabel("Country")
plt.ylabel("Total COVID-19 Cases")
plt.title("Top 10 Countries by Total COVID-19 Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nCOVID-19 Data (Top 10 Countries):")
for country in top_10:
    print(f"{country['country']}: Cases - {country['cases']}, Deaths - {country['deaths']}, Recovered - {country['recovered']}")