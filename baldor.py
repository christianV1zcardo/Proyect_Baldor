import sympy

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
        
def _iterador_r(dic, ej):
    for k, v in dic.items():
        print(f"EJ {ej}| {k}: {v}")

def _salida_iteradores(k, v, ej):
    print(f"""EJ {ej}| {k}:\n\n{v}\n\n-----------------------------------------------------------""")

def _iterador_r_pretty(dic, ej):
    for k, v in dic.items():
        v = sympy.pretty(v)
        _salida_iteradores(k, v, ej)
        
def _iterador_r_pretty_pow(dic, ej):
    for k, v in dic.items():
        v = sympy.powsimp(v)
        v = sympy.pretty(v)
        _salida_iteradores(k, v, ej)

def _iterador_r_pretty_pow_exp(dic, ej):
    for k, v in dic.items():
        v = sympy.expand(v)
        v = sympy.powsimp(v)
        v = sympy.pretty(v)
        _salida_iteradores(k, v, ej)

def it_respuesta(dic, ej, pretty=False, powsimp=False, exp=False):
    """
    Itera entre los ejercicios y muestra su respuesta

    Args:
        dic (dict): Diccionario con los ejercicios
        ej (int): Ejercicio del libro
        pretty (bool, optional): Si True usa formato sympy.pretty. Por defecto
                                    es False
        powsimp (bool, optional): Si True aplica sympy.powsimp. Requiere 
                                    pretty=True Por defecto es False
        exp (bool, optional): Si True aplica sympy.expand. Requiere 
                            pretty=True y powsim=True. Por defecto es False
    
    Returns:
        Nada, imprime las respuestas en consola
    """
    if not isinstance(dic, dict):
        raise TypeError("El argumento 'dic' debe ser un diccionario.")
    
    if pretty is False:
        _iterador_r(dic, ej)
    elif pretty is True and powsimp is False: 
        _iterador_r_pretty(dic, ej)
    
    elif pretty is True and powsimp is True:
        if exp is True:
            _iterador_r_pretty_pow_exp(dic, ej)
        else:
            _iterador_r_pretty_pow(dic, ej)
