email_id = input("please Eter your email id").strip()
username = email[:email_id.index('@')]
domain = email[:email_id.index('@')+1]
print(f"Your Username:{username}and your domain name is{domain}")
