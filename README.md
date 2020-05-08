# A basic banking system that stores data using the Python File System. 
1. On run, the program should present the following options:
- Staff Login
- Close App
2. Selecting staff login should return:
- enter username
- enter password
3. username can be found in staff.txt, entering the correct username and password should give a 'Login successful' message
4. after successful login, program should present:
- Create new account
- Check account details
- log out
![pic1](https://github.com/dyn4casie/snbank/blob/master/images/Screenshot%20(374).png)
5. typing 1 for creating new account, program should request for
- account name
- account email
- account type
- opening balance
6. After entering the information above, program should: 
- generate a ten digit account number for the customer, 
- Save the created account details in customer.txt file, 
- display the newly created account number
- prompt a 'Account created successfully message'
![pic2](https://github.com/dyn4casie/snbank/blob/master/images/Screenshot%20(370).png)
- present the options in number 4 above
1. If staff selects check account details in number 4, program should request for account number
2. The program should fetch the details of the account from the customer.txt file and display it to the staff, then present back the options in number 4.
3. If staff selects logout in number 4, delete the user session file and return the user back to the staff login page.
![pic3](https://github.com/dyn4casie/snbank/blob/master/images/Screenshot%20(371).png)
