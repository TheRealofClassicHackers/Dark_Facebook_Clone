# Dark Facebook Cloner (DFC) v2.5

<div align="center">
  <img src="https://via.placeholder.com/150x150.png?text=DFC+Logo" alt="DFC Logo" width="150"/>
  <h1>Dark Facebook Cloner</h1>
  <p>Automate Facebook account creation with temporary emails and proxies – for ethical testing only!</p>
  <a href="https://www.facebook.com/profile.php?id=61555424416864">
    <button style="background-color: #1877F2; color: white; padding: 12px 24px; border: none; border-radius: 6px; cursor: pointer; font-size: 16px;">
      Contact Us / Report Issues
    </button>
  </a>
</div>

---

## 📋 Table of Contents
- [About DFC](#about-dfc)
- [Features](#features)
- [How It Works](#how-it-works)
- [Pros & Cons](#pros--cons)
- [Limitations](#limitations)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)
- [Disclaimer](#disclaimer)

---

## 🌟 About DFC

**Dark Facebook Cloner (DFC)** is a Python-based tool crafted by **The Realm of Classic Hackers (T.R.C.H)** to automate the creation of Facebook accounts using temporary email addresses and proxies. Designed for ethical research and testing, DFC simplifies generating accounts for API testing or platform analysis in controlled environments.

⚠️ **Important**: Use DFC responsibly and in compliance with Facebook’s Terms of Service and local laws. Unauthorized account creation is prohibited.

---

## ✨ Features

- **Automated Account Creation**: Generates Facebook accounts with random usernames, passwords, and profile details.
- **Temporary Emails**: Uses the Mail.tm API to create disposable email addresses.
- **Proxy Support**: Routes requests through proxies listed in `proxies.txt` for anonymity.
- **Randomized Data**: Employs the Faker library to create realistic names, birthdays, and genders.
- **Output Logging**: Saves account details (email, ID, password, token) to `username.txt`.
- **User-Friendly Interface**: Features a colorful CLI with ASCII art and clear prompts.

---

## 🔍 How It Works

DFC streamlines account creation through these steps:

1. **Proxy Validation**:
   - Loads proxies from `proxies.txt`.
   - Tests each proxy by connecting to the Mail.tm API using multithreading.
   - Selects valid proxies for subsequent requests.

2. **Email Generation**:
   - Fetches available domains from Mail.tm.
   - Creates temporary email accounts with random usernamesEstranged usernames and passwords.

3. **Facebook Registration**:
   - Generates user details (name, birthday, gender) using Faker.
   - Sends a signed POST request to the Facebook API (`https://b-api.facebook.com/method/user.register`) with a hardcoded API key and secret.
   - Captures the user ID and access token upon successful registration.

4. **Data Storage**:
   - Saves account details to `username.txt` for easy access.
   - Displays results in the console with error handling for failed attempts.

The tool uses Python’s `requests`, `colorama`, and `faker` libraries, with robust error handling to manage network or API issues.

---

## ✅ Pros & Cons

### Pros
- **Time-Saving**: Automates repetitive account creation tasks.
- **Anonymity**: Supports proxies to mask IP addresses.
- **Flexible**: Generates varied user data for realistic accounts.
- **Open-Source**: Free to use, modify, and contribute to.
- **Error Handling**: Gracefully handles API failures and network issues.

### Cons
- **Ethical Concerns**: Potential misuse could violate platform policies.
- **API Reliability**: Depends on Mail.tm and Facebook APIs, which may change.
- **Proxy Dependency**: Requires high-quality proxies for consistent performance.
- **Hardcoded Credentials**: API key and secret may become outdated.

---

## 🚫 Limitations

- **API Key Issues**: The hardcoded Facebook API credentials may no longer be valid due to API updates.
- **Rate Limiting**: APIs may throttle requests, limiting bulk account creation.
- **Proxy Quality**: Poor or slow proxies can cause failures.
- **No Email Verification**: Lacks support for checking verification emails, which may be required.
- **Legal Risks**: Unauthorized use may lead to account bans or legal consequences.
- **Detection Risk**: Facebook may flag automated account creation attempts.

---

## 🛠️ Installation

Get DFC up and running in a few steps:

### Prerequisites
- **Python 3.6+**: Install from [python.org](https://www.python.org/downloads/).
- **pip**: Included with Python for package management.
- **Git**: Optional, for cloning the repo. Get it from [git-scm.com](https://git-scm.com/downloads).

### Steps
1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/TheRealofClassicHackers/Dark_Facebook_Clone.git
   cd DFC
   python Dark_Cone.py
