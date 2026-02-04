# Environmental Analytics for Pasture Biomass Optimization

**Author:** Abdullah Mahmoud Aldous  
**Degree Program:** Data Science and Artificial Intelligence – Al Hussein Technical University  
**Project Context:** Environmental Consultancy for Sustainable Pasture Management  

---

## 🌱 Project Overview

This project addresses the optimization of **pasture management practices** for sustainable agriculture. The government agency overseeing sustainable farming tasked us to analyze biomass production in pasture paddocks, understand environmental influences, and provide prescriptive recommendations to improve livestock feed availability while maintaining ecological balance.

The project uses **data analytics techniques** spanning **descriptive, predictive, and prescriptive analytics**:

1. **Descriptive Analytics:** Identify trends, patterns, and relationships in pasture biomass data using statistical measures and visualizations.  
2. **Predictive Analytics:** Forecast biomass production using regression models, time series methods, and deep learning (LSTM).  
3. **Prescriptive Analytics:** Optimize the Environmental Suitability Index (ESI) using metaheuristic algorithms to find optimal weights for rainfall, temperature, and vegetation indices.

---

## 📂 Repository Structure
```text
Pasture-Biomass-Analytics/
│
├─ FinalAnalytics.docx             # Research document & summary of findings
├─ FinalAnalytics.ipynb           # Main Jupyter notebook with all analyses
├─ Complete_Dataset_updated.csv   # Dataset used for analysis
├─ EvoloPy-master/                # Metaheuristic framework
│   ├─ optimizers/                # Metaheuristic algorithms
│   │   ├─ GA.py                  # Genetic Algorithm
│   │   ├─ DE.py                  # Differential Evolution
│   │   ├─ MVO.py                 # Multi-Verse Optimizer
│   │   ├─ BAT.py                 # Bat Algorithm
│   │   ├─ CS.py                  # Cuckoo Search
│   │   └─ ...                    # Other algorithms
│   ├─ benchmarks.py              # Objective functions (e.g., MSE_ESI)
│   ├─ plot_boxplot.py            # Boxplot visualizations
│   ├─ plot_convergence.py        # Convergence visualizations
│   ├─ solution.py                # Example solution runner
│   ├─ example.py                 # Demonstration scripts
│   ├─ __init__.py
│   ├─ LICENSE.txt
│   ├─ requirements.txt
│   ├─ optimizer.py               # Runs metaheuristic algorithms
│   ├─ README.md                  # EvoloPy framework README
│   └─ 2025-01-24-04-32-09/      # Each run generates a folder like this
│       ├─ boxplot-MSE_SI.png
│       ├─ convergence-MSE_ESI.png
│       ├─ experiment.csv
│       └─ experiment_details.csv
└─ .gitignore                     # Ignore temporary files & __pycache__
```

---

## 📊 Dataset

- **Name:** Biomass and Pasture Dataset  
- **Source:** [Mendeley Data](https://data.mendeley.com/datasets/8tjgtkktky/5/files/c4064af6-8c84-4ad7-b3c1-fe573358cbf8)  
- **Research Paper:** [ScienceDirect Article](https://www.sciencedirect.com/science/article/pii/S235234092400177X)  
- **Features:** Biomass, weather data, satellite-derived vegetation indices, forage quality metrics.

---

## 🧮 Descriptive Analytics

- **Central Tendency:** Mean and median show paddocks without animals have higher biomass; animals reduce biomass due to consumption.  
- **Dispersion:** Variance and coefficient of variation (CV) indicate high biomass variation.  
- **Frequency & Position:** Quartiles classify biomass as low, medium, or high.  
- **Outlier Detection:** Only columns B3 and B4 contained true outliers, detected via IQR and z-score.  
- **Visualizations:** Histograms, KDE, doughnut, violin, box, line, scatter plots, and heatmaps reveal patterns, correlations, and feature relationships.  

**Key Insights:**

- NDVI → Vegetation health: higher NDVI = higher biomass  
- NDWI → Moisture: higher NDWI = higher biomass  
- GCI → Chlorophyll content: higher = higher biomass  
- HUM_REL → Humidity: higher humidity supports biomass growth  
- Presence of animals reduces biomass but maintains balance  

---

## 📈 Predictive Analytics

- **Feature Selection:** Sequential Feature Selector + Decision Tree performed best.  
- **Forecasting Models:**
  - **Time Series:** Exponential smoothing predicts biomass trends.  
  - **Machine Learning:** Decision Tree regression provides accurate predictions.  
  - **Deep Learning:** LSTM with dense layers was tested, but Decision Tree outperformed it.  
- **Evaluation Metrics:** MAE and R² used to compare model performance.  
- **Visualization:** Line and scatter plots show predicted vs. actual biomass values.

---

## ⚙️ Prescriptive Analytics – Optimizing ESI

- **Objective:** Find optimal weights (W1, W2, W3) for rainfall, max temperature, and NDVI to minimize **Mean Squared Error (MSE)** for Environmental Suitability Index (ESI).  
- **Algorithms Applied:** GA, DE, MVO (others available: PSO, BAT, CS, etc.)  
- **Experiment Settings:**  
  - Population Size: 30  
  - Iterations: 50  
  - Runs: ≥10 per optimizer  

**Example Benchmark Function (from `benchmarks.py`):**
```python
def MSE_ESI(num):
    w1, w2, w3 = num
    actual_ESI = data['Environmental Suitability Index']
    predicted_ESI = w1 * data['Rainfall'] + w2 * data['TEMP_MAX'] + w3 * data['NDVI']
    mse = np.mean((actual_ESI - predicted_ESI)**2)
    return mse

## License

- Parts of this project use the **EvoloPy framework**, which is licensed under the [Apache License 2.0](EvoloPy/LICENSE.txt).  
- My own code (e.g., `FinalAnalytics.ipynb`, `benchmarks.py` setups, and analysis scripts) is authored by **Abdullah Mahmoud Aldous**.  
- You are free to use, modify, and distribute this project following the Apache 2.0 terms for EvoloPy and standard attribution for my code.