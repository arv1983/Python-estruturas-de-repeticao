
def corresponding_parenthesis(parens):
    abre = 0
    fecha = 0
    retorna = ""
    for item in parens:
        if item == "(":
            abre += 1
        else:
            fecha += 1
    
    res = abre - fecha
    if res == 0:
        return ''
    
    if(res > 0):
        i = 0
        while i < res:
            i += 1
            retorna = retorna + '('
    else:
        res = res * -1
        i = 0
        while i < res:
            i += 1
            retorna = retorna + ')'
    return retorna

# EXEMPLO 1:
result = corresponding_parenthesis("()()")
print(result)

# > ""
# EXEMPLO 2:
result = corresponding_parenthesis("()))")
print(result)

# > ))
# EXEMPLO 3:
result = corresponding_parenthesis(")))(((((")
print(result)

# > ((
# EXEMPLO 4:
result = corresponding_parenthesis(")(")
print(result)








def remove_more_than_two_repetitions(text):
    res = []
    res[:] = text
    
    resu = [i for i, j in zip_longest(res, res[1:])
                                                if i != j]
    return resu

text2 = "Ollloco meuuuu, taaa peegaando fogoo biiiiichooo"
text = remove_more_than_two_repetitions(text2)
# > Olloco meuu, taa peegaando fogoo biichoo
print(text)