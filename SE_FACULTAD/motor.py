
from base import REGLAS

def inferir(entrada):
    coincidencias = []
    reglas_aplicadas = []
    
    for c in entrada:
        coincidencias.append(c)
        
    sw = True
    
    while sw:
        sw = False
        for i in range(len(REGLAS)):
            regla = REGLAS[i]
            
            regla_sw = False
            
            for j in reglas_aplicadas:
                if i == j:
                    regla_sw = True
                    break
            
            if regla_sw:
                continue
            
            condicion_sw = True
            for condiciones in regla['if']:                
                condicion_encontrada_sw = False                
                for c in coincidencias:
                    if condiciones == c:
                        condicion_encontrada_sw = True
                        break
                
                if condiciones not in coincidencias:
                    condicion_sw = False
                    break
            
            if condicion_encontrada_sw:
                for c in regla['then']:
                    
                    conclusiones = False
                    
                    for s in coincidencias:
                        if c == s:
                            conclusiones = True
                            break
                    
                    if not conclusiones:
                        coincidencias.append(c)
                        sw = True
                        
                    reglas_aplicadas.append(i)
                    
    return coincidencias