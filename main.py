#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    if not s:
        return []

    c = [s[0]]
    o = [1]      
    k = 1        

    n = len(s)
    while k < n:
        if s[k] == s[k - 1]:
            o[-1] += 1
        else:
            c.append(s[k])
            o.append(1)
        k += 1
    return list(zip(c, o))



def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:  
        return []


    i = 1
    while i < len(s) and s[i] == s[0]:
        i += 1

    return [(s[0], i)] + artcode_r(s[i:])
    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
