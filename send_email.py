import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

load_dotenv()


# -----------------------------
# Gmail account
# -----------------------------

SENDER = os.getenv("SENDER")

# This is NOT your normal Gmail password.
# We'll create an App Password in the next step.
APP_PASSWORD = os.getenv("APP_PASSWORD")


# -----------------------------
# Recipients
# -----------------------------

TO_EMAILS = [
    "students@iiitdwd.ac.in",
    "warden@iiitdwd.ac.in"
]

CC_EMAILS = [
    "anandbarangi@iiitdwd.ac.in"
]

BCC_EMAILS = [
    "24bcs034@iiitdwd.ac.in",
    "24bcs015@iiitdwd.ac.in",
    "24bcs001@iiitdwd.ac.in",
    "24bcs138@iiitdwd.ac.in"
]


# -----------------------------
# Email details
# -----------------------------

SUBJECT = "🙏 Ganpati Bappa Morya! | Ganpati Vargani"


# -----------------------------
# Read HTML
# -----------------------------

with open("email.html", "r", encoding="utf-8") as file:
    html_content = file.read()


# -----------------------------
# Connect to Gmail SMTP
# -----------------------------

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

    server.login(SENDER, APP_PASSWORD)

    message = MIMEMultipart("related")

    message["From"] = SENDER
    message["To"] = ", ".join(TO_EMAILS)
    if CC_EMAILS:
        message["Cc"] = ", ".join(CC_EMAILS)
    
    message["Subject"] = SUBJECT

    # Tell email client this is HTML
    message.attach(
        MIMEText(html_content, "html", "utf-8")
    )

    # Attach the image inline
    with open("image.png", "rb") as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-ID', '<ganpati_img>')
        message.attach(img)

    # Combine all recipients for the SMTP envelope
    all_recipients = TO_EMAILS + CC_EMAILS + BCC_EMAILS

    server.sendmail(
        SENDER,
        all_recipients,
        message.as_string()
    )

    print("✅ Email sent successfully to all recipients!")