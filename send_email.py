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

RECIPIENTS = [
    "arnav.angarkar20@gmail.com",
    "24bcs034@iiitdwd.ac.in"
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

    for recipient in RECIPIENTS:

        message = MIMEMultipart("related")

        message["From"] = SENDER
        message["To"] = recipient
        message["Subject"] = SUBJECT

        # Tell email client this is HTML
        message.attach(
            MIMEText(html_content, "html", "utf-8")
        )

        # Attach the image inline
        with open("ganpati.jpg", "rb") as img_file:
            img = MIMEImage(img_file.read())
            img.add_header('Content-ID', '<ganpati_img>')
            message.attach(img)



        server.sendmail(
            SENDER,
            recipient,
            message.as_string()
        )

        print(f"✅ Sent to {recipient}")