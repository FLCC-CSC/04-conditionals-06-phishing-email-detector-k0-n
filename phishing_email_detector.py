# FILE NAME - phishing_email_detector.py

# NAME: Josh Fielding
# DATE: 10/4/25
# BRIEF DESCRIPTION: Write a program that analyzes an email subject line to detect phishing attempts based on common red flags



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

# prompt user to enter an email subject line
subject = input("Enter the email subject line: ")

# check phishing indicators and output a warning message
print("\nSECURITY ASSESSMENT:")
if "urgent" in subject.lower() or "immediate action required" in subject.lower():
    print("HIGH RISK: Possible phishing attempt.")
elif "win" in subject.lower() or "free" in subject.lower():
    print("MEDIUM RISK: Suspicious offer detected.")
elif "password reset" in subject.lower():
    print("LOW RISK: Verify legitimacy with sender.")
else:
    print("No phishing indicators detected.")

# print subject thats been analyzed
print("------------------------")
print(f'Analyzed subject: "{subject}"')

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
Enter the email subject line: Meeting on Friday

SECURITY ASSESSMENT:
No phishing indicators detected.
------------------------
Analyzed subject: "Meeting on Friday"
'''

'''
Enter the email subject line: URGENT REQUEST FOR BANK TRANSFER

SECURITY ASSESSMENT:
HIGH RISK: Possible phishing attempt.
------------------------
Analyzed subject: "URGENT REQUEST FOR BANK TRANSFER"
'''

'''
Enter the email subject line: All I do is win win win no matter what

SECURITY ASSESSMENT:
MEDIUM RISK: Suspicious offer detected.
------------------------
Analyzed subject: "All I do is win win win no matter what"
'''

'''
Enter the email subject line: Did you request a password reset?

SECURITY ASSESSMENT:
LOW RISK: Verify legitimacy with sender.
------------------------
Analyzed subject: "Did you request a password reset?"
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Was using `in` difficult or was it natural?

It was natural





'''



########################################
#            ATTESTATION
########################################

'''

Please gauge your utilization of AI on the following spectrum. Place an "X" in front
of the appropriate response. Only choose one of the following:

[ ] I did not use AI at all for this lab.
[X] I wrote the initial draft of the software but had AI help me make it better.
[ ] I fed the lab description to AI and had it generate a response but I modified it.
[ ] AI created the entire program for me.



It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[X] I pretty much get it.
[ ] I'm solid. Totally got it.

'''
