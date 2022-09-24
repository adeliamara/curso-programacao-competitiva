def verifica_status_aprovacao(media):
    if(media >= 7): 
        return "Aluno aprovado."
    elif (media < 5):
        return "Aluno reprovado."
    return "Aluno em exame."


def verifica_status_aprovacao_final(media):
    if(media >= 5):
        return "Aluno aprovado."
    return "Aluno reprovado."
    
if __name__ == "__main__":
    notas = input()
    [nota1, nota2, nota3, nota4] = map(float, notas.split(' '))        
    
    media  = (nota1 * 2 + nota2 * 3 + nota3 * 4 + nota4)/10
    print("Media: %.1f" % media)
    
    status = verifica_status_aprovacao(media)
    print(status)
    
    if(status == "Aluno em exame."):
        nota_exame = float(input())
        print("Nota do exame: %.1f" % nota_exame)
        media = (media + nota_exame)/2
        status = verifica_status_aprovacao_final(media)
        print(status)
        print("Media final: %.1f" % media)
