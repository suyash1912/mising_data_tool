# Data Cleaner Pro

A powerful, user-friendly web application for data cleaning and exploration. Built with Streamlit, it enables you to upload CSV files, perform essential cleaning operations, and visualize your data with interactive 3D plots.

## Features

### Data Processing
- **CSV Upload**: Seamlessly upload datasets in CSV format
- **Duplicate Removal**: Remove duplicate rows with one click
- **Missing Value Imputation**: Automatically detect and fill missing values using Mean, Median, or Mode
- **Data Overview**: Get comprehensive dataset statistics including shape, memory usage, and data types

### Visualization
- **Interactive 3D Scatter Plots**: Generate dynamic visualizations for datasets with numeric columns
- **Customizable Axes**: Select any numeric columns for X, Y, and Z axes
- **Color Coding**: Optionally color-code data points by any column

### Export
- **Clean Data Download**: Export processed datasets as CSV files with automatic naming

## Tech Stack

- **Framework**: Streamlit
- **Data Processing**: Pandas
- **Visualization**: Plotly Express, Matplotlib
- **Python**: 3.9+

## Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/suyash1912/mising_data_tool.git
   cd data-cleaner-pro
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

The application will automatically open in your default web browser.

## Usage Guide

### Getting Started
1. **Upload Your Data**: Use the sidebar file uploader to select your CSV file
2. **Configure Settings**: Choose your preferred cleaning options in the sidebar

### Data Cleaning
1. **Review Data Overview**: Examine dataset statistics and preview in the main panel
2. **Handle Missing Values**: 
   - View columns with missing data and their counts
   - Select imputation method (Mean, Median, or Mode)
   - Click "Clean Missing Values" to apply changes
3. **Remove Duplicates**: Toggle the duplicate removal option as needed

### Visualization
1. **Enable 3D Plotting**: Check the "Enable 3D Scatter Plot" option
2. **Configure Plot**: 
   - Select numeric columns for X, Y, and Z axes
   - Choose an optional color-coding column
3. **Interact**: Rotate, zoom, and hover over data points in the 3D plot

### Export Results
1. **Download Cleaned Data**: Click "Download Cleaned CSV" to save your processed dataset
2. **File Naming**: Downloaded files are automatically named `cleaned_[original_filename].csv`

## Requirements

Create a `requirements.txt` file with the following dependencies:

```
streamlit
pandas
matplotlib
plotly
```

## Project Structure

```
data-cleaner-pro/
│
├── script.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
├── README.md          # Project documentation
└── LICENSE            # License file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Suyash Mukherjee**

---

*Built with ❤️ using Streamlit and Python*
