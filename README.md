# Emailwarning
Tool for pentesters warn e-mail account users post exploitation.
This script was made for pentesters warn users that have their passwords stolen from vulnerables websites. 

**********I am not responsable if someone uses for malicious purposes.**********

# How to use

> python Emailwarning.py

The e-mail list must contain e-mail and password separated by commas in each line.
You will be prompted to type the file name of the e-mail list that must be in the same path of the script:

> What''s the filename? mylist.txt

Further you chose the e-mail provider:

> Warn users from: Gmail(1) Outlook(2) Yahoo(3): (type number) 

An e-mail will be send to the account owners by theirself without showing what account is vulnerable:

*"Dear account owner,
Your password account has been compromissed.
We recommend you to change your password immediately.
Has a proof, your password is:
password"*

And a confirmation message will be displayed:

*"Vulnerable! :(
Account owner warned!
4 accounts warned successfully."*






