ans = ['Mango', 'mango', 'aam', 'Aam']
yourans = ''
while yourans not in ans:

  yourans = input('King of Fruits is called?: ')
  if yourans == ['Mango', 'mango', 'aam', 'Aam']:

      print('Correct')
  else:
    print(f'{yourans} is wrong answer')