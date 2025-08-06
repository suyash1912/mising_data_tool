Data Cleaner Pro 🧼
A user-friendly web application built with Streamlit that allows you to upload a CSV file, perform essential cleaning operations, and explore the data with interactive visualizations.

(A sample screenshot of the application interface)

🚀 Features
📁 CSV Upload: Easily upload your dataset in CSV format.

🗑️ Duplicate Removal: Remove duplicate rows with a single checkbox.

🔧 Missing Value Imputation:

Automatically detects columns with missing values.

Fill missing numeric values using Mean, Median, or Mode.

📊 Data Overview:

Get a quick summary of your dataset's shape (rows, columns) and memory size.

View the first few rows of the data.

See a breakdown of column data types.

📈 Interactive 3D Visualization:

If your data has at least three numeric columns, you can generate an interactive 3D scatter plot.

Select columns for the X, Y, and Z axes.

Optionally color-code the plot by any column in the dataset.

⬇️ Download Cleaned Data: Download the processed, clean dataset as a new CSV file.

🛠️ Tech Stack
Framework: Streamlit

Data Manipulation: Pandas

Visualization: Plotly Express & Matplotlib

⚙️ Installation & Setup
To run this application on your local machine, please follow these steps.

1. Prerequisites
Make sure you have Python 3.9 or higher installed on your system.

2. Clone the Repository
Bash

git clone https://github.com/your-username/data-cleaner-pro.git
cd data-cleaner-pro
3. Create a Virtual Environment (Recommended)
It's a good practice to create a virtual environment to manage project dependencies.

On macOS/Linux:

Bash

python3 -m venv venv
source venv/bin/activate
On Windows:

Bash

python -m venv venv
.\venv\Scripts\activate
4. Install Dependencies
Create a file named requirements.txt with the following content:

Plaintext

streamlit
pandas
matplotlib
plotly
Then, install the required packages using pip:

Bash

pip install -r requirements.txt
5. Run the Application
Now you are ready to run the Streamlit app. Use the following command in your terminal:

Bash

streamlit run app.py
(Assuming you have saved the provided code as app.py)

Your web browser should automatically open a new tab with the "Data Cleaner Pro" application running.

📖 How to Use the App
Upload File: Click the "Browse files" button in the sidebar to upload your CSV file.

Set Cleaning Options:

Choose your preferred method (Mean, Median, or Mode) for filling missing numeric data.

Check or uncheck the "Remove duplicate rows" box as needed.

Toggle the 3D plot visibility with the "Enable 3D Scatter Plot" checkbox.

Review Overview: Once the file is uploaded, the main panel will display:

The shape and size of your data.

A preview of the first 5 rows.

A count of columns by their data type.

Clean Missing Values:

The app will show a list of columns with missing values and their counts.

Click the "🔧 Clean Missing Values" button to apply the imputation method you selected in the sidebar.

A success message and a preview of the transformed data will appear.

Explore in 3D:

Scroll down to the "3D Visualization" section.

Select the desired numeric columns for the X, Y, and Z axes from the dropdown menus.

(Optional) Choose a column to color-code the data points.

Interact with the plot by rotating, zooming, and hovering over points.

Download Your Data:

Once you are satisfied with the cleaning, scroll to the bottom.

Click the "📥 Download Cleaned CSV" button to save the cleaned data to your computer. The downloaded file will be named cleaned_[your_original_filename].csv.

✍️ Author
This project was built with ❤️ by Suyash Mukherjee.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.