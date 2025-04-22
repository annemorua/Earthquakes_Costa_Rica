# 📡 RSN-UCR Earthquake Scraper

This Python script scrapes earthquake data from the official website of the **Red Sismológica Nacional de Costa Rica (RSN-UCR)**.

---

## 📋 What does the script do?

- Automatically navigates through pages listing recent earthquakes.
- Extracts each earthquake’s **date and time** and **magnitude (Mw)**.
- Saves the data into a `.csv` file for further analysis.

---

## 📦 Requirements

Make sure you have Python 3 installed. Then, install the required packages using:

```bash
pip install requests beautifulsoup4
```

---

## 📁 CSV Output Structure

The generated CSV file contains two columns:

- `fecha_hora`: Earthquake date and time.
- `magnitud`: Magnitude on the Mw scale.

Example:

```
fecha_hora,magnitud
2024-01-20 10:43:15,4.5
2024-01-20 02:11:30,3.8
```

---

## 🚀 How to Use

1. Open the `.py` script and adjust these variables to define the data range you want to scrape:

```python
archivo_csv = "f_m_ENERO.csv"
start = 5475  # Starting index for pagination
decremento = 15  # Number of records per page
```

2. Run the script:

```bash
python your_script_name.py
```

3. The script will append data to the specified CSV file.

---

## ⏳ Notes

- The script includes a 1-second delay between requests to avoid overloading the RSN server.
- Please scrape responsibly and do not abuse the service.

---

## 🧠 Credits

- **Data Source**: [RSN-UCR](https://rsn.ucr.ac.cr/)
- **Author**: [Your Name or Username]

---
