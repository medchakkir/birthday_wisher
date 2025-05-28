# Birthday Wisher

An automated birthday email sender that helps you never forget to send birthday wishes to your friends and family. This application automatically checks for birthdays each day and sends personalized birthday emails using pre-written templates.

## Features

- Automated birthday detection
- Personalized email messages using templates
- Multiple letter templates for variety
- Secure email sending using SMTP
- CSV-based birthday database
- Easy to maintain and update birthday list

## Requirements

- Python 3.x
- Required Python packages (install via requirements.txt):
  - pandas
  - numpy
  - python-dateutil
  - pytz
  - six
  - tzdata

## Installation

1. Clone this repository:

```bash
git clone https://github.com/momed-ali01/birthday_wisher.git
cd birthday_wisher
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Configure your email settings:
   - Update the `MY_EMAIL` and `MY_PASSWORD` variables in `main.py` with your Gmail credentials
   - Note: For Gmail, you'll need to use an App Password. See [Gmail App Passwords](https://support.google.com/accounts/answer/185833) for more information.

## Usage

1. Add birthdays to the `birthdays.csv` file in the following format:

```csv
name,email,month,day
John Doe,john@example.com,1,1
```

2. Customize letter templates:

   - Edit or add new templates in the `letter_templates` directory
   - Templates should use `[NAME]` as a placeholder for the recipient's name

3. Run the application:

```bash
python main.py
```

The application will:

- Check if any birthdays match today's date
- Select a random letter template
- Personalize the template with the birthday person's name
- Send the email automatically

## Project Structure

```
birthday_wisher/
├── main.py              # Main application script
├── birthdays.csv        # Birthday database
├── letter_templates/    # Email templates directory
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
├── requirements.txt     # Python dependencies
└── README.md           # This documentation
```

## Email Templates

The application comes with three default letter templates, but you can add or modify them as needed. Each template should:

- Be placed in the `letter_templates` directory
- Use `[NAME]` as a placeholder for the recipient's name
- Be named in the format `letter_X.txt` where X is a number

## Security Notes

- Never commit your email credentials to version control
- Consider using environment variables for sensitive information
- Use App Passwords instead of your main email password
- Keep your birthday database private

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
