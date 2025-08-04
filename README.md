🇬🇷 COVID-19 Analytics – Greece  
Beginner-level data-science project using Python

---

### 📊 Dataset Overview  
**Dataset:** owid-covid-data.csv  
(Our World in Data – daily updated, filtered for Greece) [^99^]

| Column                              | Description                                |
|-----------------------------------|--------------------------------------------|
| date                              | Date of record (YYYY-MM-DD)                |
| new_cases                        | Daily new confirmed cases                   |
| new_deaths                       | Daily new deaths                            |
| icu_patients                    | Patients intubated in ICU                   |
| hosp_patients                | Total hospitalised                           |
| new_tests_smoothed          | 7-day average daily tests                   |
| positive_rate                   | % of tests that were positive               |
| people_fully_vaccinated_per_hundred | % population fully vaccinated             |

---

### 🛠️ Tools Used  
- Python 3  
- Pandas for cleaning & aggregation  
- Seaborn / Matplotlib for plots  
- Jupyter Lab  

---

### 📈 Key Insights  
- Peak ICU occupancy: 847 patients (2021-12-07)  
- Highest 7-day positivity: 33 % (2020-11-20)  
- Vaccination plateau: 75 % of population fully vaccinated by July 2022  

---

### 📚 What I learned  
- Loading & filtering time-series CSVs  
- Handling missing values (NaN)  
- Calculating rolling averages (7-day)  
- Creating publication-ready plots in Greek & English  

---

### 💡 Next steps  
- Seasonal decomposition (winter vs summer waves)  
- Compare Greece vs EU average  
- Add boxplots or moving averages  
- Interactive dashboard with Plotly  

---

### 🚀 Run it yourself  
```bash
git clone https://github.com/YOUR_USERNAME/covid-greece-analytics.git
cd covid-greece-analytics
pip install -r requirements.txt
jupyter lab
