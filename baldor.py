def fraccion_mixta_a_decimal(parte_entera, numerador, denominador, exp=None):
    """
    Convierte una fracción mixta a decimal

    Args:
        parte_entera (_type_): Parte entera de la fracción
        numerador (_type_): Numerador de la fracción
        denominador (_type_): Denominador de la fracción
        exp (_type_): 
        
    Returns: 
        float: Fracción mixta convertida a decimal
    
    Raises: 
        ValueError: si el denominador es 0
    """
    if denominador == 0:
        raise ValueError('El denominador no puede ser 0')
    if numerador < 0 or          denominador <0:
        # Se asume una parte fraccionario simpre positiva porque el signo
        # lo da la el valor entero
        raise ValueError('Numerador y denominador de la parte fraccionaria \
                         deben ser positivos (el signo va en el valor entero)')
    
    # Calcula el valor decimal de la fracción (sin el entero)
    valor_decimal_fraccion = numerador/denominador
        
    valor_absoluto_total = abs(parte_entera) + valor_decimal_fraccion    
        
    if exp is None:
        if parte_entera < 0:
            return -valor_absoluto_total
        else:
            return valor_absoluto_total
    else:
        if parte_entera < 0:
            return -valor_absoluto_total * exp
        else:
            return valor_absoluto_total * exp