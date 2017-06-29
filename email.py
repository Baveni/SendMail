import smtplib
import getpass


try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    FromAddr = raw_input("login for GMAIL")
    pwd = getpass.getpass("PWD:")
    server.login(FromAddr, pwd)
    ToAddr = [raw_input("enter receiver >> ")]
    subject = raw_input("enter subj >> ")
    content = raw_input("enter content >> ")

    za_poslat = """
    From: %s
    To: %s
    sub: %s
    %s
    """ % (FromAddr, ", ".join(ToAddr), subject, content)

    server.sendmail(FromAddr, ToAddr, za_poslat)
    server.quit()
except smtplib.SMTPException:
    print('Something went wrong...')
