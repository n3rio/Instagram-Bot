#!/usr/bin/python
# -*- coding: utf-8 -*-

print '/// ROBOT CARGANDO ARSENAL ///'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import *
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
import selenium.webdriver.support.ui as ui
import os
import random
import time
import dis
import new
import argparse
import pyautogui
global numTab
global cnT
global numero_visitas
global success

def detcTrampa(driver):
	print "[+] Buscando Trampas [+]"
	try:
		trampa = driver.find_element_by_xpath("//div[@class='recaptcha-checkbox-checkmark']")
		d_Trampa = ActionChains(driver)
		d_Trampa.move_to_element(trampa)
		d_Trampa.click(trampa)
		d_Trampa.perform()
		t_dT = random.randrange(40,120)
		time.sleep(t_dT)
	except Exception as e:
		print "[+] No se encontraron trampas - Camino inseguro [+]"

def objFinder(driver):

	print "[+] Buscando Paginas Principales [+]"

	try:
		pags_principales = driver.find_elements_by_class_name("linkspacer")
		for i in pags_principales:
			# l_pp = lista de hrefs de paginas principales
			l_pp = i.get_attribute("href")
		
	except Exception as e:
		print "[+] No se encontraron paginas principales [+]"
		# EL PROGRAMA DEBERIA TERMINAR AQUI

	print "[+] Buscando Cantidad de Paginas [+]"

	try:
		n_pags = driver.find_elements_by_class_name("page-spacer")
		for j in n_pags:
			# l_np = lista de paginacion
			l_np = j.get_attribute("href")

	except Exception as e:
		print "[+] No se encontraro la cantidad de paginas [+]"

	print "[+] Buscando Items [+]"

	try:
		items = driver.find_elements_by_xpath("//a[starts-with(@href, './?page=vote&vote=')]")
	except Exception as e:
		print "[+] No se encontraron items [+]"

def attackControl(driver):

	print "[+] Buscando Paginas Principales [+]"

	try:
		pags_principales = driver.find_elements_by_class_name("linkspacer")
		for i in pags_principales:
			# l_pp = lista de hrefs de paginas principales
			l_pp = i.get_attribute("href")
		
	except Exception as e:
		print "[+] No se encontraron paginas principales [+]"
		# EL PROGRAMA DEBERIA TERMINAR AQUI

	print "[+] Buscando Cantidad de Paginas [+]"

	try:
		n_pags = driver.find_elements_by_class_name("page-spacer")

		for j in n_pags:
			# l_np = lista de paginacion
			l_np = j.get_attribute("href")

	except Exception as e:
		print "[+] No se encontraro la cantidad de paginas [+]"

	print "[+] Buscando Items [+]"

	try:

		items = driver.find_elements_by_xpath("//a[starts-with(@href, './?page=vote&vote=')]")

	except Exception as e:

		print "[+] No se encontraron items [+]"

	for pag in pags_principales:
		go_Pp = ActionChains(driver)
		go_Pp.move_to_element(pag)
		t01 = random.randrange(40,80)
		time.sleep(t01)
		go_Pp.click(pag)
		go_Pp.perform()
		t02 = random.randrange(40,80)
		time.sleep(t02)






	'''
	print "[+] Ataque a SubObjetivo [+]"
	pyautogui.moveTo(308,514,2)
	pyautogui.click()
	t2 = random.randrange(40,120)
	time.sleep(t2)
	date = time.ctime()
	driver.save_screenshot('screenie_'+date+'.png')
	t2 = random.randrange(40,120)
	time.sleep(t2)

	i = 20

	while i > 0:
		print "[+] Ataque a SubObjetivo [+]"
		cuerpo = driver.find_element(By.XPATH,'//body')
		cuerpo.send_keys(Keys.ENTER)
		t2 = random.randrange(80,123)
		time.sleep(t2)

		print "[+] Verificando tipo de SubObjetivo [+]"
		try:
			sObj1 = driver.find_element_by_tag_name('video')
			f_v = open("/home/n3rio/Escritorio/ig-robot/videolinks_nails", "a")
			link_v = sObj1.get_attribute("src\n")
			f_v.write(link_v)
			print "[+] SubObjetivo es un Video - Link almacenado para posterior descarga [+]"
			f_v.close()
		except Exception as e:
			sObj2 = driver.find_elements_by_tag_name("img")
			f_ima = open("/home/n3rio/Escritorio/ig-robot/imagelinks_nails", "a")
			for images in sObj2:
				link_ima = images.get_attribute("src\n")
				f_ima.write(link_ima)
			f_ima.close()
			print "[+] SubObjetivo es una foto - Link almacenado para posterior descarga [+]"

		date = time.ctime()
		driver.save_screenshot('screenie_'+date+'.png')
		t2 = random.randrange(120,140)
		time.sleep(t2)
		i = i - 1
	'''

def initCon(target):
	driver = webdriver.Firefox()
	print "[+] Abriendo navegador - Iniciando ataque a objetivo. [+]"
	driver.get("http://" + target)

	print "[+] Maximizando ventada [+]"

	print "[+] CARGANDO DE OBJETIVO [+]"
	t1 = random.randrange(120,140)
	time.sleep(t1)

	print "[+] OBJETIVO CARGADO - INICIANDO ATAQUE [+]"

	attackControl(driver)

def main(target):
    
    initCon(target)
    

print "[+] Buen dia, Bienvenido a la plataforma de ataque IgBot [+]"
target = raw_input("Indique Objetivo: ")
print "[+] Iniciando ataque [+]"
main(target)