import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.alza.cz/dell-inspiron-14-5482?dq=6166325" # Change the link if you want to. - but alza.cz is necessary.
headers = {"User-Agent": "Put here your user-agent"} 

def check_price():
    page = requests.get(url, headers=headers)
    #print(page.content) 
    soup = BeautifulSoup(page.content,"html.parser") 

    title = soup.find(itemprop = "name").get_text()

    for span in soup.find_all("span", attrs={"class":"bigPrice price_withVat"}):
        price = (span.text)

	# Removal of unnecessary things that prevent string to float conversion 
    first = price.replace(u'\xa0',' ') # In the input was special character in unicode.
    second = first.replace(" ","") 
    third = second.replace(",-","") 
    converted_price = float(third)

    if converted_price < 20000: # Checking the price
        send_mail()
    print(title.strip()) 
    print(converted_price)

def send_mail(): # Function for sending an email alert
    server = smtplib.SMTP("smtp.gmail.com", 587) #SMTP - Simple Mail Transfer protocol
    server.ehlo()  # Establish connection
    server.starttls()
    server.ehlo()

    server.login("email@com","password") # Your Gmail account
    subject = "Price fell down - check it"
    body = "Check this link for alza: https://www.alza.cz/dell-inspiron-14-5482?dq=6166325"
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail("sender","reciver",msg) # Sender - email of sender # Reciever - email of reciever
    print("Email was sent!")
    server.quit()

def main():
    check_price()
main()
