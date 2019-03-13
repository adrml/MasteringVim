#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telebot
from telebot import types

TOKEN = '520096113:AAF4EmQQ9Lo2lf3YEEuZJu7MXkDv6Il-1mg' 
bot = telebot.TeleBot(TOKEN) 
xatAdmin= 0 # <- El chatID del vuestro bot
permetreComanda=False
comandes={}
primers=[]
segons=[]
platActual=""

@bot.message_handler(commands=['reset'])
def reset(missatge):
	if (missatge.chat.id==xatAdmin):
		primers=[]
		segons=[]
		global permetreComanda
		permetreComanda=False
	else:
		bot.send_message(missatge.chat.id,"No ets l'administrador")

@bot.message_handler(commands=['anular'])
def anular(missatge):
	if (missatge.chat.id!=xatAdmin):
		comandes.pop(missatge.from_user.username)
		bot.send_message(missatge.chat.id,"Comanda anulada")

@bot.message_handler(commands=['demanar'])
def demanar(missatge):
	if (missatge.chat.id!=xatAdmin):		
		if 	(missatge.from_user.username not in comandes.keys()):
			comandes[missatge.from_user.username]=["",""]
			if (permetreComanda):
				markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
				for plat in primers:
					markup.add(types.KeyboardButton(plat))
				resposta=bot.send_message(missatge.chat.id,"Tria quin primer vols",reply_markup=markup)
				bot.register_next_step_handler(resposta, afegirPrimers)
			else:
				bot.send_message(missatge.chat.id,"No es permeten comandes")
		else:
			bot.send_message(missatge.chat.id,"Ja has demanat, pots anular amb /anular")

def afegirPrimers(resposta):
	comandes[resposta.from_user.username][0]=resposta.text
	markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
	for plat in segons:
		markup.add(types.KeyboardButton(plat))
	answer=bot.send_message(resposta.chat.id,"Tria quin segon vols",reply_markup=markup)	
	bot.register_next_step_handler(answer, afegirSegons)

def afegirSegons(resposta):
	comandes[resposta.from_user.username][1]=resposta.text
	bot.send_message(resposta.chat.id,"Petició feta, en breu a menjar")
	

@bot.message_handler(commands=['activar'])
def activar(missatge):
	if (missatge.chat.id==xatAdmin):
		global permetreComanda
		permetreComanda=True
		bot.send_message(missatge.chat.id,"Menú activat")
	else:
		bot.send_message(missatge.chat.id,"No ets l'administrador")

@bot.message_handler(commands=['carta'])
def carta(missatge):
	if (missatge.chat.id==xatAdmin):
		bot.send_message(missatge.chat.id,"Primers "+str(primers)+" segons: "+str(segons))
	else:
		bot.send_message(missatge.chat.id,"No ets l'administrador")

@bot.message_handler(commands=['veurecomandes'])
def veurecomandes(missatge):
	if (missatge.chat.id==xatAdmin):
		for user in comandes:
			bot.send_message(missatge.chat.id,str(user)+" ha demanat "+str(comandes[user][0])+" i "+str(comandes[user][1]))
	else:
		bot.send_message(missatge.chat.id,"No ets l'administrador")

@bot.message_handler(commands=['start'])
def inici(missatge):
	global xatAdmin
	if (xatAdmin==0):
		xatAdmin=missatge.chat.id
		bot.send_message(missatge.chat.id,"Benvingut administrador, escriu els noms dels plats. Un cop complets, actives per rebre comandes amb /activar. Per eliminar menu es fa amb /reset.")
	else:
		bot.send_message(missatge.chat.id,"Ja hi ha administrador")

#Escoltar missatges per afegir plats
def listener(missatges):
	for missatge in missatges:
		if (missatge.chat.id==xatAdmin and missatge.text != "Primer" and missatge.text!="Segon" and missatge.text!="Error" and missatge.text[0]!="/"):
			global platActual
			platActual=missatge.text
			markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
			markup.add(types.KeyboardButton("Primer"),types.KeyboardButton("Segon"),types.KeyboardButton("Error"))
			resposta=bot.send_message(missatge.chat.id,"Què és primer o segon plat?",reply_markup=markup)
			bot.register_next_step_handler(resposta, afegirCarta)
			
def afegirCarta(resposta):
	if (resposta.text=="Primer"):
		primers.append(platActual)
		bot.send_message(resposta.chat.id,"Primer plat afegit")
	elif (resposta.text=="Segon"):
		segons.append(platActual)
		bot.send_message(resposta.chat.id,"Segon plat afegit")	
		

bot.set_update_listener(listener) 		
bot.polling() 
