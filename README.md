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

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/regex-matcher-email-validator.git
    cd regex-matcher-email-validator
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python app.py
    ```

5. **Access the application**:
   Open your browser and go to `http://localhost:5000`.

---

## Usage

### 1. **Regex Matcher**:
- **Test String**: Input any string to test (e.g., `Hello123, world!`).
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
├── app.py                  # Main Flask app
├── requirements.txt         # Dependencies
├── templates/               # Folder for HTML templates
│   └── index.html           # Main UI template
└── README.md                # Project documentation
```

---

## Future Enhancements

- **Regex Flags**: Add options for case-insensitive matching and other regex flags.
- **Improved UI**: Use Bootstrap for a more polished and responsive user interface.
- **Cloud Deployment**: Deploy the app to AWS or another cloud provider.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgements

Thanks to [Innomatics Research Labs](https://www.innomatics.in) , Nagaraju Ekkrela Sir(https://github.com/nagarajuekkirala), and Kanav Bansal Sir(https://github.com/bansalkanav) for their guidance and support during this project.
