from flask_mail import Message

def send_welcome_email(email, username):
    from app import mail  # Import inside the function to avoid circular import
    
    msg = Message(
        subject="Welcome to Personal Expense Tracker",
        recipients=[email],
    )
    
    # Plain text version for email clients that don't support HTML
    msg.body = f"""Hi {username},

Welcome to ExpenseTracker!

This platform was built with care by DevPK to help you track your expenses easily and efficiently.

We're excited to have you on board and support your journey to better financial control.

If you have any questions or need assistance, feel free to reach out.

Happy tracking!

Best regards,
DevPK
"""
    
    # HTML version with styling
    msg.html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to ExpenseTracker</title>
    </head>
    <body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f4f4;">
        <table role="presentation" style="width: 100%; border-collapse: collapse;">
            <tr>
                <td style="padding: 40px 0;">
                    <table role="presentation" style="width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); overflow: hidden;">
                        <!-- Header -->
                        <tr>
                            <td style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px 30px; text-align: center;">
                                <h1 style="margin: 0; color: #ffffff; font-size: 28px; font-weight: 600;">
                                    💰 ExpenseTracker
                                </h1>
                            </td>
                        </tr>
                        
                        <!-- Content -->
                        <tr>
                            <td style="padding: 40px 30px;">
                                <h2 style="margin: 0 0 20px 0; color: #333333; font-size: 24px; font-weight: 600;">
                                    Hi {username}! 👋
                                </h2>
                                
                                <p style="margin: 0 0 20px 0; color: #555555; font-size: 16px; line-height: 1.6;">
                                    Welcome to <strong>ExpenseTracker</strong>!
                                </p>
                                
                                <p style="margin: 0 0 20px 0; color: #555555; font-size: 16px; line-height: 1.6;">
                                    This platform was built with care by <strong style="color: #667eea;">DevPK</strong> to help you track your expenses easily and efficiently.
                                </p>
                                
                                <p style="margin: 0 0 30px 0; color: #555555; font-size: 16px; line-height: 1.6;">
                                    We're excited to have you on board and support your journey to better financial control. 🚀
                                </p>
                                
                                <!-- Call to Action Button -->
                                <table role="presentation" style="margin: 30px 0;">
                                    <tr>
                                        <td style="text-align: center;">
                                            <a href="#" style="display: inline-block; padding: 14px 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #ffffff; text-decoration: none; border-radius: 5px; font-weight: 600; font-size: 16px;">
                                                Get Started
                                            </a>
                                        </td>
                                    </tr>
                                </table>
                                
                                <p style="margin: 30px 0 0 0; color: #555555; font-size: 16px; line-height: 1.6;">
                                    If you have any questions or need assistance, feel free to reach out.
                                </p>
                                
                                <p style="margin: 20px 0 0 0; color: #555555; font-size: 16px; line-height: 1.6;">
                                    Happy tracking! 📊
                                </p>
                            </td>
                        </tr>
                        
                        <!-- Footer -->
                        <tr>
                            <td style="background-color: #f8f9fa; padding: 30px; text-align: center; border-top: 1px solid #e9ecef;">
                                <p style="margin: 0 0 10px 0; color: #666666; font-size: 14px;">
                                    Best regards,<br>
                                    <strong style="color: #667eea;">DevPK</strong>
                                </p>
                                
                                <p style="margin: 20px 0 0 0; color: #999999; font-size: 12px; line-height: 1.5;">
                                    © 2024 ExpenseTracker. All rights reserved.<br>
                                    You're receiving this email because you signed up for an account.
                                </p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """
    
    mail.send(msg)