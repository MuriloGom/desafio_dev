import random, string, re
minusculas = string.ascii_lowercase
maiusculas = string.ascii_uppercase
digitos = string.digits
simbolos = string.punctuation

t = int(input("Quantos caracteres quer que a sua senha tenha? "))
mai = input("Quer que sua senha tenha letras maísculas?[y/n] ")
num = input("Quer que sua senha tenha números?[y/n] ")
sim = input("Quer que sua senha tenha simbolos?[y/n] ")

caracteres_permitidos = minusculas

if mai == 'y':
	caracteres_permitidos += maiusculas
if num == 'y':
	caracteres_permitidos += digitos
if sim == "y":
	caracteres_permitidos += simbolos

senha = "".join(random.choices(caracteres_permitidos, k=t))

search_num = re.findall(r"\d", senha)
search_pun = re.findall(r"\W", senha)
search_mai = re.findall("[A-Z]",senha)
valorSenha = 0
if len(senha) >= 8:
	valorSenha = valorSenha + 1
if search_num:
	valorSenha = valorSenha + 1
if search_pun:
	valorSenha = valorSenha + 1
if search_mai:
	valorSenha = valorSenha + 1

if valorSenha <= 1:
	valorSenha = "Fraca"
if valorSenha == 2:
	valorSenha = "Média"
if valorSenha == 3:
	valorSenha = "Boa"
if valorSenha == 4:
	valorSenha = "Muito Boa"

print(f"\nSua nova senha é: {senha}")
print(f"Sua senha é: {valorSenha}")

