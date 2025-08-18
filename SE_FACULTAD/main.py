#Mario Isaac Molina Rodriguez
# Moises Enrique Escobar Bonilla

from motor import inferir
# Aptitudes y actitudes posibles = APAC
from base import APAC_POSIBLES

def obtener_apacs():
    print("***** SISTEMA EXPERTO DE EVALUACION DE FACULTAD *****")
    print("Ingrese las Aptitudes y Actitudes que destaquen en usted:")
    
    entrada = input("Aptitudes y Actitudes: separado por coma (,):").lower()
    
    partes = entrada.split(",")
    
    apacs_procesados = []
    
    for parte in partes:
        apacs_procesados.append(parte.strip())
    
    apacs_base =[]
    
    for s_procesado in apacs_procesados:
        apac_valido_sw = False
        for s_posible in APAC_POSIBLES:
            if s_procesado == s_posible:
                apac_valido_sw = True
                break
        if apac_valido_sw:
            apacs_base.append(s_procesado)

        if not apac_valido_sw:
            print("No se reconicieron aptitues y actitudes validas")
            
    return apacs_base
    

    
def mostrar(evaluaciones)          :
    evaluacion_final = []
    
    for d in evaluaciones:
        apac_posible = False
        for s_posible in APAC_POSIBLES:
            if d == s_posible:
                apac_posible = True
                break
        if not apac_posible:
            evaluacion_final.append(d)

    # Evaluacion final
    if evaluacion_final:
        print("***** RESULTADOS *****")
        print("En base a sus aptitudes y actitudes:")
        
        for d in evaluacion_final:
            print(f"{d.capitalize()}")
            
    else:
        print("No se encontraron resultados")
    
def main():
    apacs = obtener_apacs()
    resultados = inferir(apacs)
    mostrar(resultados) 
    
if __name__ == "__main__":
    main()