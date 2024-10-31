
# Passenger Comfort Data Collection Application - PyQt

This repository contains a PyQt application used to collect data from users during dynamic driving scenarios. Users could indicate their comfort levels at specific moments in time, selecting options like "comfortable," "acceptable," "so and so," or "uncomfortable." The application was utilized to gather data for the Bachelor Thesis of **Torok Armin** at **Babes-Bolyai University**, July 2024. The thesis, titled **"Passenger Comfort Assessment in Dynamic Driving Environments,"** aimed to assess passenger comfort across different driving conditions.

## Table of Contents
- Overview
- Features
- Folder Structure
- Technologies Used
- Setup
- Usage
- Contributing
- License
- README File

---

## Overview

This application is designed to log users' comfort levels in response to driving scenarios. The app allows users to click buttons or press keys to log the exact time when a specific comfort level was felt. The application records and saves these data points into CSV format, making them easy to analyze.

## Features

- **Real-Time Comfort Level Logging**: Users can log comfort levels in real time with button presses.
- **Dynamic Button Styling**: The selected comfort level button changes color, providing clear feedback.
- **CSV Data Saving**: The recorded data is saved in a structured CSV format for easy access and analysis.

## Folder Structure

- `src`: Contains the main PyQt script.
- `Labeled_Data`: Contains the saved CSV data files.

## Technologies Used

- **Python (3.11)**: The programming language used.
- **PyQt5**: The Python GUI framework used to create the interface.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ArminT28/Bachelor_Thesis_Comfortability_Labeling.git
   cd Bachelor_Thesis_Comfortability_Labeling
   ```

2. **Install dependencies**:
   ```bash
   pip install PyQt5
   ```

3. **Run the Application**:
   ```bash
   python src/MainWindow.py
   ```

## Usage

1. **Start/Stop Recording**: Use the "Start Recording" and "Stop Recording" buttons to manage the data collection process.
2. **Select Comfort Level**: Click any comfort level button to log that state along with the timestamp. The options include "Excellent," "Acceptable," "So and So," "Uncomfortable," and "Not paying attention."
3. **Save Data**: When data collection is finished, click "Save Data" to export the data to a CSV file.

## Contributing

Contributions are welcome! To contribute, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## README File

This README File was generated using OpenAI's ChatGPT version 3.5.
