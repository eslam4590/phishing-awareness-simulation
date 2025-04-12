# This script creates a phishing email template with a customizable message

def generate_email_template(company_name, action_link):
    template = f"""
    Subject: Immediate Action Required - {company_name} Password Reset

    Dear Employee,

    We have detected unusual activity in your account and require you to reset your password immediately.

    Please click the link below to proceed:
    {action_link}

    If you do not take action within 24 hours, your account will be locked as a precautionary measure.

    Best regards,
    {company_name} IT Security Team
    """
    with open("phishing_email.txt", "w") as f:
        f.write(template.strip())
    print("Phishing email template generated as 'phishing_email.txt'.")

# Example usage
generate_email_template("AcmeCorp", "http://fake-login.acmecorp.com")
