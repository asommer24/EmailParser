###
### Email parser for Outlook files
### Andrew Sommer
### Created on 12/11/17
### Version 1.2
### Last edited on 12/14



class EmailParser:
    s = " " #any copied emails list from outlook 

    names = open("names.txt", "w+")
    emails = open("emails.txt", "w")
    for str in s.split(","):
        name, email = str.split("<")
        names.write(name +"\n")
        email = email.strip(">")
        emails.write(email + "\n")


    names.close()
    emails.close()
