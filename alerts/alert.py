import smtplib
from email.message import EmailMessage

def send_alert(anomaly):
    """
    Send an alert about an anomaly.

    Args:
        anomaly (dict): The anomaly to alert about.
    """
    # Create the email message
    msg = EmailMessage()
    msg.set_content(str(anomaly))

    msg['Subject'] = 'IDS Alert'
    msg['From'] = 'ids@example.com'
    msg['To'] = 'admin@example.com'

    # Send the email
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
