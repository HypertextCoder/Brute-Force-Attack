import string
paswd = input("Insert Password to Crack: \n")
def Brute(paswd):
   print("[+][+] Starting BruteForce...")
   charset = list(string.ascii_letters + string.digits + string.punctuation)
   result = ""
   x = 0
   while x <= len(paswd)-1:
      for char in charset:
         pchar = paswd[x]
         if char == pchar:
           print("[+] Trying...", char)
           print("[+][+] Matched (",char, ")")
           result += char
           print("[+][+] Current:",result)
           x += 1
           break
         else:
           print("[+] Trying...",char)     
   print("[+][+] Matching Done - Password Found:", result)
Brute(paswd) 
#Password MaxLenght is : about 10