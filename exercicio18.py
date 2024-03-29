'''Question 18
Level 3

Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1'''

senhas = input("Digite as senhas para ver se são validas: Formato comma separated values (csv): ")
senhas = senhas.split(',')

senhasValidas = []


for item in senhas:
    criterio1 = False
    criterio2 = False
    criterio3 = False
    criterio4 = False
    criterio5 = False

    for i in item:
        if i.isalpha() and i.islower(): # 1 critério satisfeito
            criterio1 = True

        if i.isalpha() and i.isupper():
            criterio3 = True

        if i.isdigit():
            criterio2 = True

        if i in '$#@':
            criterio4 = True

    if 6 <= len(item) <= 12:
        criterio5 = True

    if(criterio1 and criterio2 and criterio3 and criterio4 and criterio5):
        senhasValidas.append(item)



print(','.join(senhasValidas))






