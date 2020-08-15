"""
Unique mail
from a list of given mails we have to determine which of those will recieve the mail.
questions are from leetcode
If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address. (Note that this rule does not apply for domain names.)
If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com. (Again, this rule does not apply for domain names.)
It is possible to use both of these rules at the same time.
Given a list of emails, we send one email to each address in the list. How many different addresses actually receive mails?
"""

list_input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
def numEmails(emails):
        ans = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            ans.add(local.replace('.','') + '@' + domain)
        return len(ans)
    
numEmails(list_input)
