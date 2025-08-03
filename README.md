# 🇬🇷 COVID-19 Analytics – Greece  
*Beginner-level data-science project using Python*

---

## 📊 Dataset Overview  
**Dataset**: [owid-covid-data.csv](https://covid.ourworldindata.org/data/owid-covid-data.csv)  
(Our World in Data – daily updated, filtered for Greece) [^99^]


| Column | Description |
|--------|-------------|
| `date` | Date of record (YYYY-MM-DD) |
| `new_cases` | Daily new confirmed cases |
| `new_deaths` | Daily new deaths |
| `icu_patients` | Patients intubated in ICU |
| `hosp_patients` | Total hospitalised |
| `new_tests_smoothed` | 7-day average daily tests |
| `positive_rate` | % of tests that were positive |
| `people_fully_vaccinated_per_hundred` | % population fully vaccinated |

---

## 🛠️ Tools Used  
- Python 3  
- Pandas for cleaning & aggregation  
- Seaborn / Matplotlib for plots  
- Jupyter Lab  

---

## 📈 Key Insights  
- **Peak ICU occupancy**: 847 patients (2021-12-07)  
- **Highest 7-day positivity**: 33 % (2020-11-20)  
- **Vaccination plateau**: 75 % of population fully vaccinated by July 2022  

---

## 📚 What I learned  
- Loading & filtering time-series CSVs  
- Handling missing values (`NaN`)  
- Calculating rolling averages (7-day)  
- Creating publication-ready plots in Greek & English  

---

## 💡 Next steps  
- Seasonal decomposition (winter vs summer waves)  
- Compare Greece vs EU average  
- Add boxplots or moving averages  
- Interactive dashboard with Plotly  

---

## 🚀 Run it yourself
git clone https://github.com/YOUR_USERNAME/covid-greece-analytics.git
cd covid-greece-analytics
pip install -r requirements.txt
jupyter lab

## 📸 Visualizations 

<p align="center">
  <img src="plots/cases_deaths_7d.png" alt="Daily cases & deaths (7-day avg)" width="400"/>
  <img src="plots/vaccination_rate.png" alt="Fully vaccinated %" width="400"/>
  <br/>
  <img src="plots/unvaccinated.png" alt="Unvaccinated %" width="400"/>
  <img src="plots/icu_patients.png" alt="ICU patients" width="400"/>
  <br/>
  <img src="plots/weekly_tests.png" alt="Weekly tests" width="400"/>
  <img src="plots/weekly_positives.png" alt="Weekly positives" width="400"/>
</p>
