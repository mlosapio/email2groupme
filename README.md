# email2groupme

Quick and dirty code to tie email into group.me room annoucements from a bot. 

### Setup

This script works best when declared in /etc/aliases on a mail server like so...

```
announcements: |/usr/local/sbin/email2GroupMe.py -c /etc/email2GroupMe.ini
```

This will cause sendmail|postfix to provide the email message as stdin to the scirpt. 

