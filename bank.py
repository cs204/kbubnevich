answer = input ("Приветствие: ")
if answer[:1] == 'з' and answer[:12] != 'здравствуйте':
    print ("$20")
if answer[:1] != 'з':
    print ("$100")
if answer [:12] == 'здравствуйте':
    print ('$0')

