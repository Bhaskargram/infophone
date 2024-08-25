<h1 align="center" id="title">INFOPHONE</h1>

<p align="center"><img src="https://socialify.git.ci/Bhaskargram/infophone/image?font=Source%20Code%20Pro&amp;language=1&amp;logo=https%3A%2F%2Fi.postimg.cc%2FpLfHKNNG%2FBhaskargram.png&amp;name=1&amp;owner=1&amp;pattern=Brick%20Wall&amp;stargazers=1&amp;theme=Dark" alt="project-image"></p>

<p id="description">A python app which can easily give details of Mobile number and website domain.</p>

<h2>Project Screenshots:</h2>

<img src="https://i.postimg.cc/kGRr4zFy/image.png" alt="project-screenshot" width="400" height="400/">

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


<h1>Mobile Number Detector</h1>

        <h2>Purpose</h2>
        <p>The Mobile Number Detector is a Python-based application designed to:</p>
        <ul>
            <li>Extract detailed information about mobile numbers, including location and registration details.</li>
            <li>Check website details and extract email addresses.</li>
            <li>Provide a user-friendly interface with interactive features.</li>
        </ul>

        <h2>Features</h2>
        <ul>
            <li>Phone Number Location Extractor</li>
            <li>Website Details Checker</li>
            <li>Email Address Extractor</li>
            <li>Interactive UI with a skull graphic</li>
        </ul>

        <h2>Installation Instructions</h2>

        <h3>Termux (Android)</h3>
        <ol>
            <li><strong>Install Termux:</strong> Download and install Termux from the <a href="https://play.google.com/store/apps/details?id=com.termux">Google Play Store</a> or <a href="https://f-droid.org/packages/com.termux/">F-Droid</a>.</li>
            <li><strong>Update Termux Packages:</strong>
                <pre><code>pkg update && pkg upgrade</code></pre>
            </li>
            <li><strong>Install Python:</strong>
                <pre><code>pkg install python</code></pre>
            </li>
            <li><strong>Install Git:</strong>
                <pre><code>pkg install git</code></pre>
            </li>
            <li><strong>Clone the Repository:</strong>
                <pre><code>git clone https://github.com/Bhaskargram/infophone/</code></pre>
                <pre><code>cd infophone</code></pre>
            </li>
            <li><strong>Set Up a Virtual Environment:</strong>
                <pre><code>python -m venv venv</code></pre>
                <pre><code>source venv/bin/activate</code></pre>
            </li>
            <li><strong>Install Dependencies:</strong>
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li><strong>Create and Configure <code>.env</code> File:</strong>
                <pre><code>nano .env</code></pre>
                <p>Add the following lines:</p>
                <pre><code>NUMVERIFY_API_KEY=eeaa381b2e5b7ebec2645b13d7e88562
GOOGLE_MAPS_API_KEY=your_google_maps_api_key</code></pre>
            </li>
            <li><strong>Run the Application:</strong>
                <pre><code>python src/app.py</code></pre>
            </li>
        </ol>

        <h3>MacBook (macOS)</h3>
        <ol>
            <li><strong>Install Homebrew (if not installed):</strong>
                <pre><code>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</code></pre>
            </li>
            <li><strong>Install Python:</strong>
                <pre><code>brew install python</code></pre>
            </li>
            <li><strong>Install Git:</strong>
                <pre><code>brew install git</code></pre>
            </li>
            <li><strong>Clone the Repository:</strong>
                <pre><code>git clone https://github.com/Bhaskargram/infophone/</code></pre>
                <pre><code>cd infophone</code></pre>
            </li>
            <li><strong>Set Up a Virtual Environment:</strong>
                <pre><code>python -m venv venv</code></pre>
                <pre><code>source venv/bin/activate</code></pre>
            </li>
            <li><strong>Install Dependencies:</strong>
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li><strong>Create and Configure <code>.env</code> File:</strong>
                <pre><code>nano .env</code></pre>
                <p>Add your API keys:</p>
                <pre><code>NUMVERIFY_API_KEY=eeaa381b2e5b7ebec2645b13d7e88562
GOOGLE_MAPS_API_KEY=your_google_maps_api_key</code></pre>
            </li>
            <li><strong>Run the Application:</strong>
                <pre><code>python src/app.py</code></pre>
            </li>
        </ol>

        <h3>Linux (Ubuntu, Kali Linux)</h3>
        <ol>
            <li><strong>Update Packages:</strong>
                <pre><code>sudo apt update && sudo apt upgrade</code></pre>
            </li>
            <li><strong>Install Python and Git:</strong>
                <pre><code>sudo apt install python3 python3-venv git</code></pre>
            </li>
            <li><strong>Clone the Repository:</strong>
                <pre><code>git clone https://github.com/Bhaskargram/infophone/</code></pre>
                <pre><code>cd infophone</code></pre>
            </li>
            <li><strong>Set Up a Virtual Environment:</strong>
                <pre><code>python3 -m venv venv</code></pre>
                <pre><code>source venv/bin/activate</code></pre>
            </li>
            <li><strong>Install Dependencies:</strong>
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li><strong>Create and Configure <code>.env</code> File:</strong>
                <pre><code>nano .env</code></pre>
                <p>Add your API keys:</p>
                <pre><code>NUMVERIFY_API_KEY=eeaa381b2e5b7ebec2645b13d7e88562
GOOGLE_MAPS_API_KEY=your_google_maps_api_key</code></pre>
            </li>
            <li><strong>Run the Application:</strong>
                <pre><code>python src/app.py</code></pre>
            </li>
        </ol>

        <h3>Windows</h3>
        <ol>
            <li><strong>Install Python (if not installed):</strong>
                <p>Download and install Python from <a href="https://www.python.org/downloads/">python.org</a>. Make sure to check the option to add Python to your PATH during installation.</p>
            </li>
            <li><strong>Install Git (if not installed):</strong>
                <p>Download and install Git from <a href="https://git-scm.com/download/win">git-scm.com</a>.</p>
            </li>
            <li><strong>Open Command Prompt or PowerShell:</strong></li>
            <li><strong>Clone the Repository:</strong>
                <pre><code>git clone https://github.com/Bhaskargram/infophone/</code></pre>
                <pre><code>cd infophone</code></pre>
            </li>
            <li><strong>Set Up a Virtual Environment:</strong>
                <pre><code>python -m venv venv</code></pre>
                <pre><code>.\venv\Scripts\activate</code></pre>
            </li>
            <li><strong>Install Dependencies:</strong>
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li><strong>Create and Configure <code>.env</code> File:</strong>
                <pre><code>notepad .env</code></pre>
                <p>Add your API keys:</p>
                <pre><code>NUMVERIFY_API_KEY=eeaa381b2e5b7ebec2645b13d7e88562
GOOGLE_MAPS_API_KEY=your_google_maps_api_key</code></pre>
            </li>
            <li><strong>Run the Application:</strong>
                <pre><code>python src/app.py</code></pre>
            </li>
        </ol>

        <h2>Application Overview</h2>

        <h3>Main Menu</h3>
        <p>When the application starts, it will draw a skull using the <code>turtle</code> graphics module and then present the main menu with the following options:</p>
        <ul>
            <li><strong>Phone Number Location Extractor:</strong> Input a phone number to get detailed information, including location.</li>
            <li><strong>Website Details Checker:</strong> Input a domain to get details about the website.</li>
            <li><strong>Support:</strong> Opens your default email client with a pre-filled email address for support.</li>
            <li><strong>Exit:</strong> Close the application.</li>
        </ul>

        <h3>Sub-Menu</h3>
        <p>After selecting an option, you can return to the main menu or exit the application via the sub-menu.</p>

        <h2>License</h2>
        <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

        <h2>Contact</h2>
        <p>For support, please email: <a href="mailto:bhaskarjs.md@finixia.in">bhaskarjs.md@finixia.in</a></p>

        <p>Visit the <a href="https://github.com/Bhaskargram/infophone/">GitHub Repository</a> for more information and updates.</p>
    </div>
