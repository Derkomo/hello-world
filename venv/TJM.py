def calcul_tjm(salaire_annuel_brut=None):
    tjm_net = ((salaire_annuel_brut / 12) / 22) * 0.7
    tjm_brut = (salaire_annuel_brut / 12 / 22)
    salaire_net_par_mois = tjm_net * 22
    salaire_brut_par_mois = tjm_brut * 22
    n = print(f"TJM Net = {tjm_net} \n"
              f"salaire Net par mois = {salaire_net_par_mois} \n"
              f"TJM Brut = {tjm_brut} \n"
              f"salaire brut par mois ={salaire_brut_par_mois} \n")

    return n


def calcul_salaire(tjm_brut):
    # Avec une marge de 40% pour Findit
    salaire_monsuel_brut = tjm_brut * 20 * 0.6
    salaire_annuel_brut = salaire_monsuel_brut * 12

    salaire_monsuel_net = salaire_monsuel_brut * 0.7
    salaire_annuel_net = salaire_monsuel_net * 12

    n = print(f"salaire monsuel brut = {salaire_monsuel_brut} \n"
              f"salaire annuel brut = {salaire_annuel_brut} \n"
              f"salaire monsuel net = {salaire_monsuel_net} \n"
              f"salaire annuel net ={salaire_annuel_net} \n")
    return n

def calcul_marge (tjm_brut,salaire_a_brut):
   # salaire_a_brut = tjm_brut * 22 * (1-marge) * 12

    marge = 1-(salaire_a_brut)/(12*22*tjm_brut)

    j_Findit = tjm_brut*marge
    m_Findit = tjm_brut*marge*22
    a_Findit = m_Findit*12


    j_mehdi = tjm_brut * (1-marge)
    m_mehdi = tjm_brut * (1-marge)*22
    a_mehdi = m_mehdi * 12

    return print(f"La marge de Findit est de {marge} \n"
                 f"Sur un TJM de {tjm_brut} FindIT a {j_Findit} par jour, {m_Findit} par mois ce qui fait {a_Findit} par an \n"
                 f"Sur un TJM de {tjm_brut} mehdi a {j_mehdi} par jour,{m_mehdi} par mois ce qui fait {a_mehdi} par an")

calcul_marge(350,39000)

calcul_tjm(43200)
calcul_salaire(300)