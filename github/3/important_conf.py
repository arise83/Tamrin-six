n=int(input())
emails =[]
for i in range(n):
    email=input()
    ats=email.find('@')
    if '@' and '.' in email:
        damane=email[ats+1:]

        emails.append(damane)
        
emails=set(emails)
emails=list(emails)
emails=sorted(emails)
for email in emails:
        print(email)
