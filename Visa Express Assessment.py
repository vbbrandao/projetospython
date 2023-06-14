#!/usr/bin/env python
# coding: utf-8


import openpyxl as opl
import requests as rq
import json
import sys
import os

req_exemplo = rq.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')
vlr_ex = req_exemplo.json()
print(vlr_ex['USDBRL']['bid'])

#coletando cotação CAD/BRL
requisição = rq.get('http://economia.awesomeapi.com.br/json/last/CAD-BRL')
cotacaocadbrl = requisição.json()
finalcotacaocadbrl = (float(cotacaocadbrl['CADBRL']['bid']))

#Iniciando cálculo para chegar em CAD/COP, já que o API não suporta essa cotação

#Coletando cotação CAD/USD
requisicao1 = rq.get('http://economia.awesomeapi.com.br/json/last/CAD-USD')
cadusd = requisicao1.json()
valorcadusd = float(cadusd['CADUSD']['bid'])
print(valorcadusd)

#Coletando cotação USD/COP
requisicao2 = rq.get('http://economia.awesomeapi.com.br/json/last/USD-COP')
usdcop = requisicao2.json()
valorusdcop = float(usdcop['USDCOP']['bid'])
print(valorusdcop)
type(valorusdcop)

#Obtendo cotação CAD/COP
copfinal = (float(valorcadusd))*(float(valorusdcop))
print(copfinal)

#Área de preparação das variáveis para o programa
func_finsupport = lambda x,y: (833 * x) + y
func_cotacaobr = lambda x,y: (x*y)
requisição = rq.get('http://economia.awesomeapi.com.br/json/last/CAD-BRL')
cotacao = requisição.json()
var_canada = ['Canada','CAN','can','canada','CANADA']
var_brasil = ['Brasil','brasil','BRASIL','Brazil','brazil','BRAZIL','br','BR']
var_colombia = ['Colombia','COLOMBIA','colombia','COL','col']
var_australia = ['Australia','australia','aus','AUS']
var_usa = ['EE.UU','EEUU','USA','UNITED STATES','United States','united states','USA','usa','EUA','eua']
#iniciando o programa
print('Hello! Welcome to visa express assesment')
nationality = input('What country are you from? ')
country = input('Where are you going? ')
#abrindo a condição para escolha Canada
if country in var_canada:
    course_lenght = eval(input('For how long (in months)? '))
    tuition_value = eval(input('How much is your tuition in dollars? '))
    print('Ok! Here is what you need:')
    finsuppCAD = func_finsupport(course_lenght, tuition_value)
    print(f'You will need at least {finsuppCAD:,}', 'dollars in your account')
#definindo cotação em real    
    if nationality in var_brasil:
      brlfinal = (func_cotacaobr(finalcotacaocadbrl,finsuppCAD))
      print(f'The current exchange rate is: R$ {finalcotacaocadbrl} and minimum amount in your currency is R$ {brlfinal:,.2f}')
#definindo cotação em COP
    elif nationality == 'Colombia' or 'colombia' or 'Col' or 'COL':
      copfinalformat = func_cotacaobr(copfinal,finsuppCAD)
      print(f'The current exchange rate is: COP {copfinal:,.4f} and the minimum amount in your currency is COP {copfinalformat:,.2f}')
#mensagem extra      
    print('- ColYou will also need to present academic and labour ties')
#analisando presença de sponsor    
    sponsor_support = input('Do you have a sponsor? ')
#sponsor positivo
    if sponsor_support == 'Yes' or sponsor_support =='yes'or sponsor_support =='y':
      print('Provide the following: \n- sponsor letter \n- sponsor bank statement from the last three months \n- IRS declaration \n- labor certificate with the 3 last payslips')
#sponsor negativo      
    else:
      print('Provide your bank statement from the last three months with the above mentioned amount and IRS declaration')
#analisando suporte academico      
    academic_support = input('Do you have any second degree? ')
#suporte academido de nível superior positivo    
    if academic_support == 'Yes' or academic_support =='yes'or academic_support =='y':
        print('You will need to provide a diploma of your highest degree')
#suporte de nível academico superior negativo        
    else:
        print('Please present any certificate of studies')
#analisando suporte laboral        
    labor_support = input('Do you currently work? '  )
#suporte laboral positivo    
    if labor_support == 'Yes' or labor_support =='yes'or labor_support =='y':
      print('Please also provide your labor certificate and three last payslips')
#abrindo condição para Australia      
elif country in var_australia:
#Brasil e Colombia passam pelas mesmas condições  
  if nationality in var_brasil or nationality in var_colombia:
        print('You only need: \n - COE\n - Health insurance \n - GTE letter')
#abrindo condição para Estados Unidos
elif country in var_usa:
        print('Ask for your online form')       
#retorno, caso o aluno seja de um país diferente        
else: 
    print('Please check with one of our staff what are the requirements for your country')
print('After sending your documents to our staff please make sure to ask which will need to have a certified translation')




