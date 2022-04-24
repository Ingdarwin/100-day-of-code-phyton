

def forma_name(f_name,l_name):
  f_name_ok=""
  l_name_ok=""
  for letter in range(0,len(f_name)):
    if letter==0:
      f_name_ok += f_name[letter].upper()
    else:
       f_name_ok += f_name[letter].lower()
  for letter_l in range(0,len(l_name)):
    if letter_l==0:
      l_name_ok += l_name[letter_l].upper()
    else:
       l_name_ok += l_name[letter_l].lower()
  print(f_name_ok+" "+l_name_ok)
forma_name("darWin","aveLlA")