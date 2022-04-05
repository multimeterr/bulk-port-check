# bulk-port-check
Basic bulk port check for full networks.

This code allows you to check suspicious/vulnerable (or what you want to do port) ports on large networks. 
It is working like nmap, you can use ip addresses with CIDR notation (/10 to /32) it will check all network from network id to broadcast.

You can add your networks to 'nets' list. Also if you have to check much more amount address you can write devices.txt file with , seperated addresses.(uncomment lines 22,23,24,25 and comment line 28)

And if you have smtp gateway you can send mail with results.(or you can use commented try block for sending from gmail, just delete try block and uncommnet other one, give you address and password and its done)
