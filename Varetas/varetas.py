def extraindo_dados(arquivo):
    with open(arquivo, 'r') as file:
        todas_as_varetas = []
        varestas_separadas = []
        quant_comprimentos = []
        for num, l in enumerate(file):
            if ' ' in l:
                n = (l.strip()).split(' ')
                varestas_separadas.append(int(n[1]))
            else:
                if len(varestas_separadas) != 0:
                    todas_as_varetas.append(varestas_separadas)
                    varestas_separadas = []
            if ' ' not in l:
                quant_comprimentos.append(int(l.strip()))
    return todas_as_varetas, quant_comprimentos


def extraindo_quadrados(quant_por_tamanho):
    if len(quant_por_tamanho) == 1:
        quant_total_quadrados_formados = quant_por_tamanho[0] // 4
        return quant_total_quadrados_formados, None
    else:
        varetas_restantes = quant_por_tamanho.copy()
        quant_total_quadrados_formados = 0
        # Verificando quant de quadrados
        for num, t in enumerate(varetas_restantes):
            if t >= 4:
                quadrado_formado = t // 4
                quant_total_quadrados_formados += quadrado_formado
                varetas_restantes[num] = t - (quadrado_formado * 4)
    return quant_total_quadrados_formados, varetas_restantes


def extraindo_retangulos(varetas_restantes):
    quantidade_de_pares_de_lados_iguais = []
    for num, v in enumerate(varetas_restantes):
        if v >= 2:
            quantidade_de_pares_de_lados_iguais.append(v // 2)
    return len(quantidade_de_pares_de_lados_iguais) // 2


varetas, quant_de_comprimentos = extraindo_dados('entrada.txt')
print(varetas)
print(quant_de_comprimentos)


for caso in varetas:
    quant_quadrados, varetas_restantes = extraindo_quadrados(caso)
    if not varetas_restantes:
        print(quant_quadrados)
    else:
        quant_retangulos = extraindo_retangulos(varetas_restantes)
        print(quant_quadrados + quant_retangulos)

varetas, quant_de_comprimentos = extraindo_dados('entrada.txt')
