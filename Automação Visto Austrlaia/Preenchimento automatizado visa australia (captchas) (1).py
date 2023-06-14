#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pyautogui as pyauto
import time
import pyperclip


# In[3]:


#Campos de preenchimento para automação
senha = '@2022Australia'
country = 'brazil'
apptype = 'offshore' #onshore, offshore
TRN = '' #se é onshore
hapid = ''
coes = '1'#1,2,3
course = 'indep' #voc, indep, high
family_unit = 'n'
previous_travel = 'n'#n,y
student = 'Karine Cordeiro'


# In[ ]:


#Solicitando a realização dos ajustes necessários para o início do programa
pyauto.alert('Please set your screen size to 1920x1080', title = 'Warning!') #ajuste de tamanho da tela
pressed = pyauto.confirm('Did you set your screen size?', buttons=['Yes','No'])
while pressed == 'No':
    time.sleep(20)
    pressed = pyauto.confirm('Did you set your screen size?', buttons=['Yes','No']) 
time.sleep(2) #tempo para a próxima pergunta
initial_page = pyauto.confirm('Are you ready to begin?') #confirmando se o usuário está pronto para começar
while initial_page == 'No':
    initial_page = pyauto.confirm('Are you readu to begin?')
time.sleep(3)


# In[ ]:


#Abrindo o navegador
time.sleep(1)
pyauto.press('win')
pyauto.write('edge')
pyauto.press('enter')
time.sleep(3)


# In[ ]:


#acessando o site da imigração
link = 'https://online.immi.gov.au/lusc/login'
pyperclip.copy(link)
pyauto.hotkey('ctrl','v')
pyauto.press('enter')
time.sleep(3)
break 


# In[4]:


#acessando a área para criar a immi account
time.sleep(3)
if apptype == 'offshore':
    time.sleep(3)
    pyauto.hotkey('ctrl','f')
    pyauto.write('Create Immi')
    pyauto.press('esc')
    pyauto.press('enter')
    time.sleep(3)
#Entrando na página 1 de criação da conta
    pyauto.alert('Please fill the personal information')
    time.sleep(15)
    blanks = pyauto.confirm('Have you filled all the blanks?', buttons = ['Yes','No'])
    while blanks == 'No':
        time.sleep(15)
        blanks = pyauto.confirm('Have you filled all the blanks?', buttons = ['Yes','No'])
        break
else:
    pass


# In[5]:


#Criando immi account página 2
pyauto.alert('Remember to hide the bookmarks bar and set the zoom to 67%')
time.sleep(3)
pyauto.press('tab')
pyauto.press('tab')
pyauto.press('tab')
pyperclip.copy(senha) 
pyauto.hotkey('ctrl','v')#escrevendo a senha
pyauto.press('tab')
pyperclip.copy(senha) 
pyauto.hotkey('ctrl','v')#confirmando a senha
#preenchendo as perguntas de segurança
pyauto.press('tab')
pyauto.write('where')
pyauto.press('tab')
pyauto.press('tab')
pyauto.write(country)
pyauto.press('tab')
pyauto.write('name')
pyauto.press('tab')
pyauto.write('australia')
pyauto.press('tab')
pyauto.write('what was your favourite')
time.sleep(1)
pyauto.press('tab')
pyauto.write('english')
#solicitando que o usuário clique nas caixas de texto
pyauto.press('end')
pyauto.alert('Please click ok after check the boxes')
pyauto.hotkey('ctrl','f')
pyauto.write('submit')
pyauto.press('esc')
pyauto.press('enter')
time.sleep(4) #Página de confirmação do login
pyauto.hotkey('ctrl','f')
pyauto.write('continue')
pyauto.press('esc')
pyauto.press('enter')
break


# In[7]:


#Página inicial da aplicação zoom 67%
#Criando a nova aplicação
time.sleep(3)
pyauto.click(x=55, y=251) #clicando em nova aplicação
time.sleep(3) #aguardando carregar a página
pyauto.click(x=179, y=449) #selecionando aplicação de estudante
pyauto.click(x=200, y=482) #selecionando aplicação student visa 500
break


# In[8]:


#Página 1
time.sleep(3)
pyauto.click(x=564, y=340) #Aceitando os termos e condições
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
pyauto.press('enter')
break


# In[9]:


#Página 2/25 Zoom 67%
#Abrindo condicional para onshore
#Necessário clicar duas vezes na janela da immi
time.sleep(3)
pyauto.press('tab')
pyauto.press('tab')
if apptype == 'onshore':
    pyauto.write('Australia')
    pyauto.click(x=523, y=428)
    pyauto.click(x=521, y=465)
    pyauto.click(x=478, y=530) 
#Abrindo condicional para offshore
else:
    pyauto.write(country)
    time.sleep(1)
    pyauto.press('tab')
    pyauto.write('citizen')
    pyauto.press('enter')
    time.sleep(2)
    pyauto.click(x=522, y=452) #CHECAR 
    pyauto.click(x=483, y=518)
    time.sleep(2)
    pyauto.press('tab')
    pyauto.press('tab')
    pyauto.press('tab')
    pyauto.press('enter')
    time.sleep(10)
pyauto.alert('Please fill the COE information')
#Abrindo condição para 1 COE REVISADO EM 25/04 em 67% zoom
if coes == '1':
    pyauto.click(x=521, y=650)
    pyauto.press('tab')
    pyauto.write(course)
    time.sleep(1)
    pyauto.click(x=521, y=835)
    pyauto.click(x=523, y=901)
#Abrindo condição para 2 COE REVISADO EM 10/05 em 67% zoom
elif coes =='2':
    pyauto.click(x=511, y=684)
    pyauto.press('tab')
    pyauto.write(course)
    time.sleep(1)
    pyauto.click(x=514, y=881)
    pyauto.click(x=521, y=951)
#Abrindo condição para 3 COE
elif coes =='3':
    pyauto.click(x=516, y=709)
    pyauto.press('tab')
    pyauto.write(course)
    pyauto.click(x=514, y=905)
    pyauto.click(x=514, y=972)
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
#pyauto.press('enter')
break


# In[6]:


#Zoom 67%
#Página 3/25
#rodar depois do preenchimento
hapiddetails = 'Visa regular exams'
pyauto.alert('Please complete all personal information')
time.sleep(70) #65
pyauto.alert('Personal information filled?') #ACRESECNTAR LOOP WHILE
if apptype == 'offshore': #revisado em 25/04 com 67%
    time.sleep(3)
    pyauto.click(x=513, y=723) #identity
    pyauto.press('end')
    time.sleep(1)
    pyauto.click(x=514, y=609) #name/spelling
    pyauto.click(x=513, y=607)
    pyauto.click(x=479, y=672)
    pyauto.click(x=515, y=711)
    pyauto.click(x=516, y=775)
    pyauto.click(x=514, y=839)
    pyauto.click(x=516, y=904)
else:#Laço para onshore
    time.sleep(3)
    pyauto.click(x=515, y=727)#identity
    pyauto.press('end')
    time.sleep(1)
    pyauto.click(x=515, y=608)#name/spelling
    pyauto.click(x=468, y=676)#passport nationality
    time.sleep(1)
    pyauto.click(x=515, y=708)
    pyauto.click(x=515, y=775)
    pyauto.click(x=515, y=839)
    pyauto.click(x=482, y=908)
    pyauto.hotkey('tab')
    pyauto.hotkey('tab')
    pyauto.write(hapiddetails)
    pyauto.hotkey('tab')
    pyauto.write(hapid)
    time.sleep(1)
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
#pyauto.press('enter')
break


# In[12]:


#Página 4
#Zoom 67%
time.sleep(3)
pyauto.click(x=475, y=587)
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
#pyauto.press('enter')


# In[3]:


#página 5 (em aplicação offshore) Any visit to Australia?
time.sleep(2)
if apptype == 'offshore':
    time.sleep(2)
    pyauto.click(x=537, y=386)
    pyauto.hotkey('ctrl','f')
    pyauto.write('next')
    pyauto.press('esc')
    #pyauto.press('enter')
else:
    pass
break


# In[4]:


#Página 6 Family unit
#zoom 67%
time.sleep(2)
if family_unit == 'y':
    pyauto.click(x=484, y=320)
    time.sleep(40)
    pyauto.alert('Press OK when family unit form is finished')
else:
    time.sleep(3)
    pyauto.click(x=519, y=318)
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
#pyauto.press('enter')
break


# In[7]:


#Página 8 COMPLETAR COM LAÇO ONSHORE
#zoom 67%
time.sleep(3)
pyauto.click(x=1122, y=217)
pyauto.press('tab')
pyauto.write(country)
pyauto.hotkey('tab')
pyauto.hotkey('tab')
if apptype == 'offshore': 
    if country == 'brazil':
        pyauto.write('brasilia')
        time.sleep(1)
        pyauto.press('tab')
        pyauto.press('enter')
    elif country != 'brazil':
        pyauto.write('santiago')
        time.sleep(4)
        pyauto.press('tab')
        pyauto.press('enter')
elif apptype == 'onshore':
    pyauto.press('tab')
    pyauto.write('melbourne')
    time.sleep(3)
    pyauto.press('tab')
    time.sleep(1)
    pyauto.press('enter')
time.sleep(3)
pyauto.click(x=566, y=539)
pyauto.write(country)
pyauto.press('enter')
pyauto.press('tab')
'''pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
#pyauto.press('enter')
break'''


# In[9]:


#Página 9
time.sleep(3)
pyauto.click(x=478, y=369)
time.sleep(2)
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
#pyauto.press('enter')
break


# In[23]:


#página 10 non accompanying members of the family unit
#Criar laço para family unit
#zoom 67%
time.sleep(3)
pyauto.click(x=521, y=369)
time.sleep(5)
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
#pyauto.press('enter')
break


# In[8]:


#página 11 Other family members
#zoom 67%
time.sleep(2)
pyauto.click(x=476, y=320)
time.sleep(3)
pyauto.press('tab')
pyauto.press('tab')
pyauto.press('tab')
pyauto.press('enter')
time.sleep(90)
pyauto.alert('Has the family informations been filled?')
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
'''pyauto.press('enter')'''
break


# In[10]:


#Página 14/25
#zoom 67%
sop = "Please refer to my sop attached"
time.sleep(3)
pyauto.click(831,466)
pyauto.write(sop)
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
pyauto.press('enter')
#Página 15/25 #VERIFICAR ZOOM
time.sleep(3)
pyauto.click(x=487, y=325)
time.sleep(1)
pyauto.click(x=487, y=432)
pyauto.hotkey('tab')
pyauto.write(sop)
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
pyauto.press('enter')
#Página 16 Preenchendo OSHC
time.sleep(3)
pyauto.click(x=481, y=355)
pyauto.click(x=527, y=389)
time.sleep(25)
pyauto.alert('OSHC infomration filled?')
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
pyauto.press('enter')
break


# In[11]:


#Página 17
#zoom 67%
time.sleep(35)
pyauto.alert('Page is filled?')
pyauto.click(x=538, y=517)
pyauto.click(x=530, y=555)
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
#pyauto.press('enter')
break


# In[ ]:


#Página 18


# In[4]:


#Página 19
#67% zoom
time.sleep(3)
pyauto.click(x=520, y=388)
pyauto.press('tab')
if country == 'brazil':
    pyauto.write('port')
else:
    pyauto.write('spani')
pyauto.click(x=518, y=512)
pyauto.click(x=519, y=547)
pyauto.click(x=518, y=598)
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
#pyauto.press('enter')
break


# In[5]:


#Página 20
#zoom 67%
time.sleep(3)
if previous_travel == 'n':
    pyauto.click(x=517, y=424)
    pyauto.hotkey('ctrl','f')
    pyauto.write('next')
    pyauto.press('esc')
    pyauto.press('enter')
else:
    pyauto.click(x=477, y=424)
    pyauto.hotkey('ctrl','f')
    pyauto.write('next')
    pyauto.press('esc')
    pyauto.press('enter')
    pyauto.alert('Previous travel info filled?')
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
#pyauto.press('enter')


# In[10]:


#Zoom 67%
#Página 21
'''time.sleep(3)
if apptype == 'onshore':
    pyauto.click(x=479, y=357)
    pyauto.press('tab')
    pyauto.write(f'Australia Student Visa (500) TRN {TRN}')
    pyauto.click(x=523, y=582)
    pyauto.click(x=528, y=623)
    pyauto.hotkey('ctrl','f')
    pyauto.write('next')
    pyauto.press('esc')
    pyauto.press('enter')
else:                 
    time.sleep(3)
    pyauto.alert('Adjust zoom to 75%')
    pyauto.click(520,353)
    pyauto.click(520,394)
    pyauto.click(520,435)
    pyauto.hotkey('ctrl','f')
    pyauto.write('next')
    pyauto.press('esc')
    pyauto.press('enter')
pyauto.alert('Adjust zoom to 75%')
#Página 22/25
time.sleep(3)
pyauto.click(520,353)
pyauto.click(520,394)
pyauto.click(520,435)
pyauto.click(520,477)
pyauto.click(520,516)
pyauto.click(520,630)
pyauto.click(520,866)
pyauto.click(520,907)
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
pyauto.press('enter')'''
#página 23
time.sleep(3)
pyauto.hotkey('end')
time.sleep(1)
pyauto.click(520,186)
pyauto.click(520,228)
pyauto.click(520,265)
pyauto.click(520,309)
pyauto.click(520,350)
pyauto.click(520,388)
pyauto.click(520,434)
pyauto.click(520,474)
pyauto.click(520,515)
pyauto.click(520,555)
pyauto.click(520,595)
pyauto.click(520,635)
pyauto.click(520,675)
pyauto.click(520,726)
pyauto.click(520,766)
pyauto.click(520,806)
pyauto.click(520,846)
pyauto.click(520,886)
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
pyauto.press('enter')
#Página 24/25
time.sleep(3)
pyauto.hotkey('end')
time.sleep(1)
pyauto.click(472,378)
pyauto.click(472,418)
pyauto.click(472,460)
pyauto.click(472,501)
pyauto.click(472,542)
pyauto.click(472,669)
pyauto.click(472,723)
pyauto.click(472,829)
pyauto.click(472,887)
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
pyauto.press('enter')
#Página 25/25
time.sleep(4)
pyauto.hotkey('end')
time.sleep(2)
pyauto.click(472,146)
pyauto.click(472,186)
pyauto.click(472,243)
pyauto.click(472,288)
pyauto.click(472,327)
pyauto.click(472,383)
pyauto.click(472,427)
pyauto.click(472,470)
pyauto.click(472,510)
pyauto.click(472,567)
pyauto.click(472,628)
pyauto.click(472,672)
pyauto.click(472,763)
pyauto.click(472,839)
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
pyauto.press('enter')
#Página de revisão
time.sleep(15)
pyauto.hotkey('end')
time.sleep(1)
pyauto.click(221,935)
time.sleep(11)
pyauto.click(916,110) #clicando em salvar
time.sleep(3)
pyauto.write(f'Application Form {student}')
time.sleep(2)
pyauto.alert('Is the name correct?')
pyauto.press('enter')
time.sleep(3)
pyauto.click(1327,399)
pyauto.hotkey('ctrl','f')
pyauto.write('next')
pyauto.press('esc')
pyauto.press('enter')
break


# In[32]:


pyauto.position()


# In[ ]:




