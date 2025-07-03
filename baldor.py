def fraccion_mixta_a_decimal(parte_entera, numerador, denominador):
    """
    Convierte una fracción mixta a decimal

    Args:
        parte_entera (_type_): Parte entera de la fracción
        numerador (_type_): Numerador de la fracción
        denominador (_type_): Denominador de la fracción
        
    Returns: 
        float: Fracción mixta convertida a decimal
    
    Raises: 
        ValueError: si el denominador es 0
    """
    if denominador == 0:
        raise ValueError('El denominador no puede ser 0')
    if numerador < 0 or denominador <0:
        # Se asume una parte fraccionario simpre positiva porque el signo
        # lo da la el valor entero
        raise ValueError('Numerador y denominador de la parte fraccionaria \
                         deben ser positivos')
    
    # Calcula el valor decimal de la fracción (sin el entero)
    valor_decimal_fraccion = numerador/denominador
        
    valor_absoluto_total = abs(parte_entera) + valor_decimal_fraccion    
        
    if parte_entera < 0:
        return -valor_absoluto_total
    else:
        return valor_absoluto_total

def fraccion_a_decimal(numerador, denominador):
    """
    Convierte una fraccion (positiva o negativa) a decimal

    Args:
        numerador (_type_): numerador de la fracción
        denominador (_type_): denominador de la fracción
    Returns:
        float: Fraccion convertida a decimal
    Raises:
        ValueError: Si numerador es 0
    """
    if denominador == 0:
        raise ValueError('Numerador es 0')
    
    valor_decimal = numerador / denominador
    return valor_decimal