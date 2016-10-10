# -*- coding: utf-8 -*-
from lettuce import step, world
from calculadora import Calculadora

@step(u'dado que tengo el número "([^"]*)" y "([^"]*)" - Arrange')
def dado_que_tengo_el_numero_group1_y_group1_arrange(step, num1, num2):
    cal = Calculadora()
    world.resultado = cal.suma(int(num1),int(num2))

@step(u'cuando realizo la suma - Act')
def cuando_realizo_la_suma_act(step):
    pass
    
@step(u'entonces el resultado que obtengo es "([^"]*)" - Assert')
def entonces_el_resultado_que_obtengo_es_group1_assert(step, esperado):
    assert int(esperado)==world.resultado, 'El resultado '+esperado+' no es el esperado.'
