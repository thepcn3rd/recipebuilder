#!/usr/bin/python3

import base64
import zlib
import bz2

def applyb64(i):
 print("base64 Encoding the Information")
 headerInfo = '#!/usr/bin/python3\n'
 headerInfo += 'import base64;exec(base64.b64decode("'
 encodedInfo = base64.b64encode(i.encode("utf-8"))
 footerInfo = '"))'
 outputInfo = headerInfo + str(encodedInfo, "utf-8") + footerInfo
 return outputInfo

def applyZLIB(i):
 print("zlib Compress the Information")
 compressionLevel = input("Select compression level (1-9): ")
 headerInfo = '#!/usr/bin/python3\n'
 headerInfo += 'import zlib, base64;z=base64.b64decode("'
 encodedInfo = base64.b64encode(zlib.compress(i.encode("utf-8"), int(compressionLevel)))
 footerInfo = '");y=zlib.decompress(z);exec(y)'
 outputInfo = headerInfo + str(encodedInfo, "utf-8") + footerInfo
 return outputInfo

def applyBZ2(i):
 print("bz2 Compress the Information")
 compressionLevel = input("Select compression level (1-9): ")
 headerInfo = '#!/usr/bin/python3\n'
 headerInfo += 'import bz2, base64;w=base64.b64decode("'
 encodedInfo = base64.b64encode(bz2.compress(i.encode("utf-8"), int(compressionLevel)))
 footerInfo = '");r=bz2.decompress(w);exec(r)'
 outputInfo = headerInfo + str(encodedInfo, "utf-8") + footerInfo
 return outputInfo

def applyXOR(i):
 print("XOR Information")
 hexValue = input("XOR INT Value: ")
 headerInfo = '#!/usr/bin/python3\n'
 headerInfo += 'import base64;j=bytearray(base64.b64decode("'
 bArray = bytearray(i.encode("utf-8"))
 for b in range(len(bArray)):
  bArray[b] ^= int(hexValue)
 encodedInfo = base64.b64encode(bArray)
 footerInfo = '"));\n'
 footerInfo += 'for c in range(len(j)): j[c] ^= ' + hexValue + '\n'
 footerInfo += 'exec(str(j, "utf-8"))'
 outputInfo = headerInfo + str(encodedInfo, "utf-8") + footerInfo
 return outputInfo


def executeRecipe(r):
 outputPython = "outFile.py"
 print 
 filename = input("Filename to apply recipe: ")
 print
 info = ''
 f = open(filename, "r")
 for line in f:
  if '#!/usr/bin/python3' not in line:
   info += line
 f.close()
 for recipe in r:
  if recipe == "b64":
   outputRecipe = applyb64(info)
   info = outputRecipe
  elif recipe == "XOR":
   outputRecipe = applyXOR(info)
   info = outputRecipe
  elif recipe == "zlib":
   outputRecipe = applyZLIB(info)
   info = outputRecipe
  elif recipe == "bz2":
   outputRecipe = applyBZ2(info)
   info = outputRecipe
 f = open(outputPython, "w")
 f.write(outputRecipe)
 f.close()
 



def main():
 recipes = []
 selection = 'a'
 print
 print("Build a Encoded/Compressed File from a Recipe you Build")
 while selection != 'q' and selection != 'Q':
  print("Select which task to fulfill:")
  print("1. Base64 Encode")
  print("2. XOR")
  print("3. zlib Compress")
  print("4. bz2 Compress")
  print
  print("D. Display Recipe")
  print("E. Execute Recipe")
  print("Q. Quit")
  selection = input("> ")
  if selection == '1':
   print
   print("base64")
   recipes.append("b64")
   print
  elif selection == '2':
   print
   print("XOR")
   recipes.append("XOR")
   print
  elif selection == '3':
   print
   print("zlib")
   recipes.append("zlib")
   print
  elif selection == '4':
   print
   print("bz2")
   recipes.append("bz2")
   print
  elif selection == "D" or selection == "d":
   print
   print("Recipe:")
   for recipe in recipes:
    print(recipe)
   print
  elif selection == "E" or selection == "e":
   print
   print("Execute the Recipe")
   executeRecipe(recipes)
   print
   recipes = []


if __name__ == "__main__":
    main()
  
