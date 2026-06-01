"""
Created on Foxy Kronfeld
Install Packages for QPython3L, Python3 and Python for Windows
PIP and Packages Updater included
@author: @Foxy_kr
"""

import os
import sys
import subprocess
import logging
import platform
import warnings

try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
    import requests

os.system('cls' if os.name == 'nt' else 'clear')

# Suppress DeprecationWarnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Configuration of the Logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Conditional import based on Python version
if sys.version_info < (3, 8):
    try:
        import importlib_metadata as metadata  # For Python 3.5, 3.6, and 3.7
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'importlib_metadata'])
        import importlib_metadata as metadata  # For Python 3.5, 3.6, and 3.7
else:
    try:
        from importlib import metadata  # For Python 3.8 and later
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'importlib'])
        from importlib import metadata  # For Python 3.8 and later

# List of required modules (cleaned of duplicates)
required_packages = {
    "requests", "wheel", "beautifulsoup4", "certifi", "cfscrape", "charset-normalizer", "cloudscraper",
    "colorama", "emoji-country-flag", "et-xmlfile", "fake-useragent", "Faker", "Flag", "geographiclib",
    "geopy", "getmac", "idna", "iso8601", "m3u8", "names", "nodejs", "openpyxl", "optional-django",
    "ping3", "pyaes", "pyasn1", "pycountry", "pyfiglet", "Pygments", "pyparsing", "pyshorteners",
    "PySocks", "pystyle", "python-dateutil", "pytz", "random-user-agent", "requests-toolbelt",
    "rich", "rsa", "setuptools", "six", "sock", "soupsieve", "Telethon", "tenacity", "termcolor",
    "tqdm", "urllib3", "user-agent", "websocket-client", "wget", "zipp", "playsound"
}

def install_package(package):
    """Install a single package using pip."""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print(f"Successfully installed: {package}")
    except subprocess.CalledProcessError:
        print(f"Error installing {package}")

def check_os():
    """Check the operating system."""
    os_type = platform.system()
    print('\n')
    if os_type == "Windows":
        print("\33[1;92mOperating System:\t\33[0m Windows")
    elif os_type == "Linux":
        print("\33[1;92mOperating System:\t\33[0m Android")
    elif os_type == "Darwin":
        print("\33[1;92mOperating System:\t\33[0m macOS")
    else:
        print("\33[1;92mOperating System:\t\33[0m Unknown")

def check_python_version():
    """Check the Python version."""
    python_version = sys.version_info
    pythonversion = f"{python_version.major}.{python_version.minor}.{python_version.micro}"
    print(f"\33[1;92mPython Version:\t\t\33[0m {pythonversion}")

def print_pip_version():
    """Print the current pip version."""
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pip', '--version'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        pip_version = result.stdout.strip()
        return pip_version
    except Exception as e:
        print(f"Error retrieving pip version: {e}")
        return None

def check_pip_update():
    """Check and update pip, and print the current version."""
    try:
        print("\nChecking pip update...")
        current_version = print_pip_version().split()[1]
        print(f"\33[1;92mCurrent pip version:\33[0m {current_version}")

        # Update pip with quiet mode to suppress output
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip', '--quiet'])
        print("\33[32mpip has been updated to the latest version.\33[0m")
    except subprocess.CalledProcessError as e:
        print(f"Error updating pip: {e}")

def is_version_compatible(version, package):
    """Check if the given version is compatible with the current Python version."""
    python_version = sys.version_info
    version_parts = list(map(int, version.split('.')))

    # Define compatibility requirements for each package Python 3.6.6
    compatibility_requirements = {
        "ping3": [4, 0, 8],
        "Pygments": [2, 14, 0],
        "names": [0, 3, 0],
        "beautifulsoup4": [4, 10, 0],
        "requests": [2, 26, 0],
        "openpyxl": [3, 0, 0],
        "rich": [10, 0, 0],
        "Telethon": [1, 24, 0],
        "Faker": [9, 0, 0],
        "geopy": [2, 2, 0],
        "colorama": [0, 4, 4],
        "tqdm": [4, 62, 0],
        "python-dateutil": [2, 8, 2],
        "pytz": [2021, 3, 29],
        "pycountry": [22, 1, 10],
        "requests-toolbelt": [0, 9, 1],
        "websocket-client": [0, 57, 0],
        "playsound": [1, 3, 0],
        "fake-useragent": [0, 1, 11],
        "cloudscraper": [1, 2, 58],
        "cfscrape": [2, 1, 0],
        "pyshorteners": [1, 0, 1],
        "random-user-agent": [1, 0, 0],
        "getmac": [0, 9, 4],
        "pyfiglet": [0, 8, 0],
        "zipp": [3, 6, 0],
        "et-xmlfile": [1, 1, 0],
        "charset-normalizer": [2, 0, 0],
        "six": [1, 16, 0],
        "pyparsing": [3, 0, 0],
        "pyasn1": [0, 4, 8],
        "rsa": [4, 7, 2],
        "m3u8": [0, 6, 0],
        "nodejs": [0, 0, 0],
        "optional-django": [0, 1, 0],
        "termcolor": [1, 1, 0],
        "soupsieve": [2, 3, 2],
        "pyaes": [1, 6, 1],
        "geographiclib": [1, 50, 0],
        "emoji-country-flag": [0, 1, 0],
        "sock": [0, 1, 0],
        "tenacity": [8, 0, 0],
        "urllib3": [1, 21, 1],
        "wget": [3, 2, 0]
    }

    if package in compatibility_requirements:
        required_version = compatibility_requirements[package]
        return version_parts >= required_version
    return True  # If no specific requirement, assume compatible

def get_latest_version(package_name):
    """Fetch the latest version of a package from PyPI."""
    try:
        # Send a GET request to the PyPI JSON API for the specified package
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=15)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Check if 'info' and 'version' keys exist in the response
        if 'info' in data and 'version' in data['info']:
            return data['info']['version']
        else:
            print(f"Version information not found for package: {package_name}")
    except requests.exceptions.SSLError as ssl_error:
        print(f"SSL error fetching version for {package_name}: {ssl_error}")
    except requests.RequestException as e:
        print(f"Error fetching version for {package_name}: {e}")
    return None

def check_and_install_packages():
    """Check for required packages and install them if necessary."""
    python_version = sys.version_info
    for package in required_packages:
        try:
            installed_version = metadata.version(package)
            print(f"\n{package} is installed with version: {installed_version}")

            if sys.version_info < (3, 7, 0):
                # Check against compatibility requirements
                if not is_version_compatible(installed_version, package):
                    print(f"\33[1;91mInstalled version {installed_version} of {package} is lower than the required version. Installing compatible version...\33[0m")
                    install_package(package)  # Install the latest compatible version
                else:
                    print(f"\33[32m{package} is compatible with your Python version.\33[0m")
            else:
                # For Python versions higher than 3.6.6, check for the latest version
                latest_version = get_latest_version(package)
                print(f"Latest version of {package} is: {latest_version}")
                if latest_version:
                    if installed_version != latest_version:
                        if is_version_compatible(latest_version, package):
                            print(f"\33[1;92mA newer version of {package} is available: {latest_version}. Updating...\33[0m")
                            install_package(f"{package}=={latest_version}")
                        else:
                            print(f"\33[1;91mThe latest version {latest_version} of {package} is not compatible with your Python version.\33[0m")
                    else:
                        print(f"\33[32m{package} is up to date.\33[0m")
                else:
                    print(f"Could not retrieve the latest version for {package}.")
        except Exception:
            print(f"{package} is not installed. Installing...")
            install_package(package)

def print_installed_versions():
    """Print the installed versions of the required packages."""
    installed_packages = {pkg.metadata['Name']: pkg.version for pkg in metadata.distributions()}
    print("\n\33[1;92mInstalled versions of required packages:\33[0m")
    for package in required_packages:
        version = installed_packages.get(package.split('==')[0], "Not installed")
        print(f"{package}: {version}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\33[1;92m\n Python Packages Installer\n PIP Auto Updater\n and Packages Updater\n for all systems\n\33[0m by Foxy Kronfeld")
    check_os()
    check_python_version()
    if sys.version_info > (3, 7, 0):
        check_pip_update()  # Always check for pip update
    check_and_install_packages()
    print_installed_versions()  # Print installed versions of packages
    input('\n\33[1;92mPress Enter to Exit\33[0m')