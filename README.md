# Regex Matcher and Email Validator

This project is a simple **Flask web application** that allows users to:
- Input a **test string** and a **regular expression (regex)** to find matches.
- Validate an **email address** to check if it follows a valid format using regex.

It’s designed to be a straightforward tool for testing regex patterns and performing email validation, similar to [regex101.com](https://regex101.com).

---

## Features

- **Regex Matcher**: Input a string and a regex pattern to find all matches within the string.
- **Email Validator**: Enter an email address to verify if it’s in a valid format.
- Built using **Flask** and **Python's re module** for regular expressions.

---

## Installation and Setup

1. **Create a virtual environment** (optional but recommended, so that local system cannot face any issue):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    nohup python3 app.py &
    ```

4. **Access the application**:
   Open your browser and go to `(http://13.61.33.243:5000/validate_email)`.

---

## Usage

### 1. **Regex Matcher**:
- **Test String**: Input any string to test (e.g., `amit113920,Hi!`).
- **Regex Pattern**: Enter a valid regex (e.g., `\d+` to match digits).
- Click "Match" to see all matches in the string.

### 2. **Email Validator**:
- **Enter Email**: Input an email address (e.g., `example@example.com`).
- Click "Validate" to check if the email is in a valid format.

---

## Project Structure

```
regex-matcher-email-validator/
│
├── app.py                   # Main Flask app
├── requirements.txt         # Dependencies
├── templates/               # Folder for HTML templates
  └── index.html             # Main UI template
```

---

## Future Enhancements

- **Regex Flags**: Add options for case-insensitive matching and other regex flags.
- **Improved UI**: Use Bootstrap for a more polished and responsive user interface.
- **Cloud Deployment**: Deploy the app to AWS or another cloud provider.

---

## Acknowledgements

Thanks to [Innomatics Research Labs](https://www.innomatics.in) , Nagaraju Ekkrela Sir(https://github.com/nagarajuekkirala), and Kanav Bansal Sir(https://github.com/bansalkanav) for their guidance and support during this project.
