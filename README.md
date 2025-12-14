# Birthday Wisher

An automated birthday email sender that helps you never forget to send birthday wishes to your friends and family. This project uses Python to check for birthdays daily and sends personalized birthday emails using pre-written templates via Gmail SMTP.

## Features

- Automated birthday detection based on current date
- Personalized email messages using customizable templates
- Multiple letter templates for variety (randomly selected)
- CSV-based birthday database for easy management
- Environment variable configuration for secure credential management
- Gmail SMTP integration for reliable email delivery
- Easy to automate with task schedulers

## Requirements

- Python 3.x
- Gmail account with App Password enabled
- Required Python packages (see `requirements.txt`):
  - `pandas` - For reading and processing the birthday CSV file
  - `python-dotenv` - For loading environment variables from `.env` file
  - `numpy` - Dependency for pandas
  - `python-dateutil` - For date parsing and manipulation
  - `pytz` - For timezone handling
  - `smtplib` - Built into Python standard library for email sending

## Installation

1. Clone this repository:

```bash
git clone https://github.com/<username>/birthday_wisher.git
cd birthday_wisher
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with the following variables:

```env
MY_EMAIL=your_email@gmail.com
MY_PASSWORD=your_gmail_app_password
```

**Important:**

- Replace all placeholder values with your actual credentials
- Never commit the `.env` file to version control
- For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password

## Usage

To run the script:

```bash
python main.py
```

### How It Works

1. The script loads environment variables from `.env` file
2. Validates that `MY_EMAIL` and `MY_PASSWORD` are set
3. Reads the `birthdays.csv` file to get all birthday entries
4. Checks if today's date (month and day) matches any birthday in the database
5. If a match is found:
   - Randomly selects one of the available letter templates (letter_1.txt, letter_2.txt, or letter_3.txt)
   - Replaces the `[NAME]` placeholder with the birthday person's name
   - Connects to Gmail SMTP server
   - Sends a personalized birthday email with subject "Happy Birthday!"

### Birthday Database Format

Add birthdays to the `birthdays.csv` file in the following format:

```csv
name,email,year,month,day
John Doe,john@example.com,1990,1,1
Jane Smith,jane@example.com,1995,5,15
```

**Note:** The `year` column is included in the CSV but only `month` and `day` are used for birthday matching.

### Customizing Letter Templates

The application comes with three default letter templates in the `letter_templates` directory. You can:

- Edit existing templates (`letter_1.txt`, `letter_2.txt`, `letter_3.txt`)
- Add new templates following the naming pattern `letter_X.txt` where X is a number
- Use `[NAME]` as a placeholder for the recipient's name (will be automatically replaced)

Example template:

```
Dear [NAME],

Happy birthday!

All the best for the year!

Your Name
```

## Error Handling

The script includes basic error handling for:

- Missing environment variables (raises `ValueError` if `MY_EMAIL` or `MY_PASSWORD` are not set)
- CSV file reading (pandas will raise errors if the file is missing or malformed)
- Template file reading (will raise `FileNotFoundError` if template files are missing)
- SMTP connection and authentication errors

**Note:** For production use, consider adding more comprehensive error handling, logging, and retry mechanisms.

## Setting Up Automated Execution

To run this script automatically on a schedule, you can:

1. **Windows Task Scheduler**: Create a scheduled task to run the script daily
2. **Linux/Mac Cron Jobs**: Add a cron job to execute the script at specified intervals
3. **Cloud Services**: Deploy to AWS Lambda, Google Cloud Functions, or similar services
4. **GitHub Actions**: Set up a scheduled workflow to run the script

Example cron job (runs daily at 9 AM):

```bash
0 9 * * * /usr/bin/python3 /path/to/birthday_wisher/main.py
```

## Security Notes

- **Never commit your `.env` file** to version control - it contains sensitive credentials
- Use Gmail's App Passwords instead of your main account password
- Keep your birthday database (`birthdays.csv`) private as it contains personal information
- Consider using a secrets management service for production deployments
- The `.env` file should be included in `.gitignore` to prevent accidental commits

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
