# 929. Unique Email Addresses

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid_emails = set()

        for i in range(len(emails)):
            local, domain = emails[i].split('@')
            local = local.split('+')[0]
            local = ''.join(local.split('.'))
            valid_emails.add(local+'@'+domain)

        return len(valid_emails)
