<h1 align="center" id="title">INFOPHONE</h1>

<p align="center"><img src="https://socialify.git.ci/Bhaskargram/infophone/image?font=Source%20Code%20Pro&amp;language=1&amp;logo=https%3A%2F%2Fi.postimg.cc%2FpLfHKNNG%2FBhaskargram.png&amp;name=1&amp;owner=1&amp;pattern=Brick%20Wall&amp;stargazers=1&amp;theme=Dark" alt="project-image"></p>

<p id="description">A python app which can easily give details of Mobile number and website domain.</p>

<h2>Project Screenshots:</h2>

<img src="https://i.postimg.cc/W1WQGsW7/Screenshot-2024-08-25-160533.png" alt="project-screenshot" width="1080" height="1920/">

# Mobile Number Detector

## Purpose

The Mobile Number Detector is a Python-based application designed to:
- Extract detailed information about mobile numbers, including location and registration details.
- Check website details and extract email addresses.
- Provide a user-friendly interface with interactive features.

## Features

- Phone Number Location Extractor
- Website Details Checker
- Email Address Extractor
- Interactive UI with a skull graphic

<h2>🛠️ Installation Steps:</h2>

### Termux (Android)

1. **Install Termux:**
   - Download and install Termux from the [Google Play Store](https://play.google.com/store/apps/details?id=com.termux) or [F-Droid](https://f-droid.org/packages/com.termux/).

2. **Update Termux Packages:**
   ```bash
   pkg update && pkg upgrade


# Mobile Number Detector

## Purpose
The Mobile Number Detector is a Python-based application designed to:
- Extract detailed information about mobile numbers, including location and registration details.
- Check website details and extract email addresses.
- Provide a user-friendly interface with interactive features.

## Features
- Phone Number Location Extractor
- Website Details Checker
- Email Address Extractor
- Interactive UI with a skull graphic

## Installation Instructions

### Termux (Android)
1. **Install Termux:** Download and install Termux from the [Google Play Store](https://play.google.com/store/apps/details?id=com.termux) or [F-Droid](https://f-droid.org/packages/com.termux/).
2. **Update Termux Packages:**
    ```bash
    pkg update && pkg upgrade
    ```
3. **Install Python:**
    ```bash
    pkg install python
    ```
4. **Install Git:**
    ```bash
    pkg install git
    ```
5. **Clone the Repository:**
    ```bash
    git clone https://github.com/Bhaskargram/infophone/
    cd infophone
    ```
6. **Set Up a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
7. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
8. **Run the Application:**
    ```bash
    python src/app.py
    ```

    ### If you have MAC, Windows, Linux you can use your own Numverify API Key, Instructions are below.

### MacBook (macOS)
1. **Install Homebrew (if not installed):**
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
2. **Install Python:**
    ```bash
    brew install python
    ```
3. **Install Git:**
    ```bash
    brew install git
    ```
4. **Clone the Repository:**
    ```bash
    git clone https://github.com/Bhaskargram/infophone/
    cd infophone
    ```
5. **Set Up a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
6. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
7. **Create and Configure `.env` File:**
    ```bash
    nano .env
    ```
    Add your API keys:
    ```env
    NUMVERIFY_API_KEY=Your_numverify_api_key
    GOOGLE_MAPS_API_KEY=your_google_maps_api_key
    ```
8. **Run the Application:**
    ```bash
    python src/app.py
    ```

### Linux (Ubuntu, Kali Linux)
1. **Update Packages:**
    ```bash
    sudo apt update && sudo apt upgrade
    ```
2. **Install Python and Git:**
    ```bash
    sudo apt install python3 python3-venv git
    ```
3. **Clone the Repository:**
    ```bash
    git clone https://github.com/Bhaskargram/infophone/
    cd infophone
    ```
4. **Set Up a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
5. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
6. **Create and Configure `.env` File:**
    ```bash
    nano .env
    ```
    Add your API keys:
    ```env
    NUMVERIFY_API_KEY=Your_numverify_api_key
    GOOGLE_MAPS_API_KEY=your_google_maps_api_key
    ```
7. **Run the Application:**
    ```bash
    python src/app.py
    ```

### Windows
1. **Install Python (if not installed):**
    Download and install Python from [python.org](https://www.python.org/downloads/). Make sure to check the option to add Python to your PATH during installation.
2. **Install Git (if not installed):**
    Download and install Git from [git-scm.com](https://git-scm.com/download/win).
3. **Open Command Prompt or PowerShell:**
4. **Clone the Repository:**
    ```bash
    git clone https://github.com/Bhaskargram/infophone/
    cd infophone
    ```
5. **Set Up a Virtual Environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
6. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
7. **Create and Configure `.env` File:**
    ```bash
    notepad .env
    ```
    Add your API keys:
    ```env
    NUMVERIFY_API_KEY=Your_numverify_api_key
    GOOGLE_MAPS_API_KEY=your_google_maps_api_key
    ```
8. **Run the Application:**
    ```bash
    python src/app.py
    ```

## Application Overview

### Main Menu
When the application starts, it will draw a skull using the `turtle` graphics module and then present the main menu with the following options:
- **Phone Number Location Extractor:** Input a phone number to get detailed information, including location.
- **Website Details Checker:** Input a domain to get details about the website.
- **Support:** Opens your default email client with a pre-filled email address for support.
- **Exit:** Close the application.

### Sub-Menu
After selecting an option, you can return to the main menu or exit the application via the sub-menu.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For support, please email: [bhaskarjs.md@finixia.in](mailto:bhaskarjs.md@finixia.in)

Visit the [GitHub Repository](https://github.com/Bhaskargram/infophone/) for more information and updates.

