import smtplib
import time

print('***********************************************************************************\n')
print('This script was made for pentesters warning users that have their passwords stolen')
print('from vulnerables websites. Don''t use for malicious purposes.')
print('The e-mail list must contain e-mail and password separated by commas(,)')
print('Example: test@testmail.com,mypassword\n')
print('***********************************************************************************\n')

warning = 'Dear account owner,\nYour password account has been compromissed.\nWe recommend you to change your password immediately.\nHas a proof, your password is:'
sub = 'Change Your Password Immediately!'


class Vader():
    def __init__(self):
        try:
            self.lista = input('What''s the filename? ')
            self.chose = int(input('Warn users from: Gmail(1) Outlook(2) Yahoo(3): (type number) '))
        except KeyboardInterrupt:
            print('User interruption...')
        self.accounts = 0

    def luke(self):
        smtpcon = smtplib.SMTP('smtp.gmail.com', 587)
        smtpcon.starttls()
        try:
            file = open(self.lista, 'r').readlines()
            for line in file:
                line = line.strip()
                user, password = line.split(',')
                try:
                    smtpcon.login(user, password)
                    try:
                        email = '{}'.format(user)
                        message = 'Subject:{}\n\n{}\n{}'.format(sub,warning,password)
                        smtpcon.sendmail(email,email,message)
                        self.accounts += 1
                        acc = str(self.accounts)
                        print('Vulnerable! :(\nAccount owner warned!')
                        smtpcon.quit()
                    except:
                        print('Not possible to send email')
                except smtplib.SMTPAuthenticationError:
                    print('Not vulnerable :)')
                except UnicodeEncodeError:
                    pass
                except ValueError:
                    pass
        except KeyboardInterrupt:
            print('User interruption...')
            print('{} accounts warned successfully.'.format(acc))
            time.sleep(1)
        print('{} accounts warned successfully.'.format(acc))

    def leia(self):
        smtpcon = smtplib.SMTP('smtp-mail.outlook.com', 587)
        smtpcon.starttls()
        smtpcon.ehlo()
        try:
            file = open(self.lista, 'r').readlines()
            for line in file:
                line = line.strip()
                user, password = line.split(',')
                try:
                    smtpcon.login(user, password)
                    try:
                        email = '{}'.format(user)
                        message = 'Subject:{}\n\n{}\n{}'.format(sub,warning,password)
                        #('From: ' + email, 'To: '+ email, 'Subject: '+ sub, warning, password)
                        #msg = '\r\n'.join(message)
                        smtpcon.sendmail(email, email, message)
                        self.accounts += 1
                        acc = str(self.accounts)
                        print('Vulnerable! :(\nAccount owner warned!')
                        smtpcon.quit()
                    except:
                        print('Not possible to send email')
                except smtplib.SMTPAuthenticationError:
                    print('Not vulnerable :)')
                except UnicodeEncodeError:
                    pass
                except ValueError:
                    pass
        except KeyboardInterrupt:
            print('{} accounts warned successfully.'.format(acc))
            print('User interruption...')
            time.sleep(1)
        print('{} accounts warned successfully.'.format(acc))

    def hanSolo(self):
        smtpcon = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
        smtpcon.starttls()
        try:
            file = open(self.lista, 'r').readlines()
            for line in file:
                line = line.strip()
                user, password = line.split(',')
                try:
                    smtpcon.login(user, password)
                    try:
                        email = '{}'.format(user)
                        message = 'Subject:{}\n\n{}\n{}'.format(sub, warning, password)
                        smtpcon.sendmail(email, email, message)
                        self.accounts += 1
                        acc = str(self.accounts)
                        print('Vulnerable! :(\nAccount owner warned!')
                        smtpcon.quit()
                    except:
                        print('Not possible to send email')
                except smtplib.SMTPAuthenticationError:
                    print('Not vulnerable :)')
                except UnicodeEncodeError:
                    pass
                except ValueError:
                    pass
        except KeyboardInterrupt:
            print('{} accounts warned successfully.'.format(acc))
            print('User interruption...')
            time.sleep(1)
        print('{} accounts warned successfully.'.format(acc))

if __name__ == '__main__':
    I = Vader()
    if I.chose == 1:
        I.luke()
    elif I.chose == 2:
        I.leia()
    elif I.chose == 3:
        I.hanSolo()
    else:
        print('Incorrect option!')
