# Email Automation — Gmail SMTP

A Python-based email automation tool that sends emails through Gmail's SMTP server.

## Features

- Send emails through Gmail SMTP
- Add CC recipients
- Add BCC recipients
- Send multiple attachments
- Validate attachment file paths
- Securely load Gmail credentials using `.env`
- Interactive terminal-based interface

## Technologies Used

- Python
- `smtplib`
- `email.message`
- `python-dotenv`
- Gmail SMTP

## Project Structure

```text
EMAIL_AUTOMATION/
│
├── main.py
├── .env
├── .env.example
├── .gitignore
└── README.md
