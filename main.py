#imports
import discord
import os
import random
from keep_alive import keep_alive
from discord.ext import commands
from tinydb import TinyDB, Query
import asyncio
import datetime

#declaring stuff

tdb = TinyDB('db.json')

mdb = TinyDB('map_db.json')
intents1 = discord.Intents.all() # Enable all intents

bot = commands.Bot(command_prefix = ["!", "/"], intents=intents1)

tdb_user = Query()



#exp for levels

lvl_exp =[1, 2, 5, 10, 25, 50, 100, 150, 200, 300, 400, 700, 1500, 5000, 20000, 40000, 61000, 93000, 140000, 200000, 500000, 750000, 1000000, 4000000, 8000000,   20000000, 100000000, 500000000, 1000000000, 3000000000, 6000000000, 10000000000, 20000000000, 40000000000, 100000000000, 200000000000, 3200000000000, 370000000000, 600000000000, 734000000000, 1000000000000, 2000000000000, 3100000000000, 3200000000000, 50000000000000, 620000000000000, 10000000000000, 25000000000000, 50000000000000, 100000000000000, 200000000000000, 310000000000000, 420000000000000, 600000000000000, 1000000000000000, 1300000000000000, 1600000000000000, 2000000000000000, 3000000000000000, 4000000000000000, 5000000000000000, 8000000000000000, 10000000000000000, 20000000000000000, 50000000000000000,  100000000000000000, 500000000000000000, 1000000000000000000, 5000000000000000000, 10000000000000000000, 20000000000000000000, 30000000000000000000, 40000000000000000000, 50000000000000000000, 60000000000000000000, 70000000000000000000, 100000000000000000000, 300000000000000000000, 600000000000000000000, 1000000000000000000000, 2000000000000000000000, 3000000000000000000000, 8405000000000000000000, 10000000000000000000000, 33300000000000000000000, 66600000000000000000000,  100000000000000000000000, 200000000000000000000000, 210000000000000000000000, 3000000000000000000000000, 400000000000000000000000, 500000000000000000000000,  6000000000000000000000000, 7000000000000000000000000, 10000000000000000000000000, 260000000000000000000000000, 34000000000000000000000000, 100000000000000000000000000, 150000000000000000000000000, 200000000000000000000000000, 300000000000000000000000000, 400000000000000000000000000, 1000000000000000000000000000, 2500000000000000000000000000, 5000000000000000000000000000, 7500000000000000000000000000, 10000000000000000000000000000, 11000000000000000000000000000, 12000000000000000000000000000, 13000000000000000000000000000, 14000000000000000000000000000, 15000000000000000000000000000, 17000000000000000000000000000, 22000000000000000000000000000, 33000000000000000000000000000, 50000000000000000000000000000, 60000000000000000000000000000, 70000000000000000000000000000,  80000000000000000000000000000, 100000000000000000000000000000, 200000000000000000000000000000, 300000000000000000000000000000, 400000000000000000000000000000, 500000000000000000000000000000, 600000000000000000000000000000, 700000000000000000000000000000, 800000000000000000000000000000, 900000000000000000000000000000, 1000000000000000000000000000000, 2000000000000000000000000000000, 3000000000000000000000000000000, 4000000000000000000000000000000, 5000000000000000000000000000000, 8700000000000000000000000000000,10000000000000000000000000000000, 25000000000000000000000000000000, 50000000000000000000000000000000, 75000000000000000000000000000000,100000000000000000000000000000000, 200000000000000000000000000000000, 500000000000000000000000000000000, 700000000000000000000000000000000, 1000000000000000000000000000000000, 2000000000000000000000000000000000, 3800000000000000000000000000000000, 5000000000000000000000000000000000, 6000000000000000000000000000000000, 7000000000000000000000000000000000, 8000000000000000000000000000000000,
10000000000000000000000000000000000, 20000000000000000000000000000000000, 30000000000000000000000000000000000, 40000000000000000000000000000000000,50000000000000000000000000000000000, 60000000000000000000000000000000000, 70000000000000000000000000000000000, 80000000000000000000000000000000000,
90000000000000000000000000000000000,
100000000000000000000000000000000000, 150000000000000000000000000000000000, 200000000000000000000000000000000000, 300000000000000000000000000000000000, 500000000000000000000000000000000000,
1000000000000000000000000000000000000, 1100000000000000000000000000000000000, 1200000000000000000000000000000000000, 1300000000000000000000000000000000000, 1400000000000000000000000000000000000, 1500000000000000000000000000000000000, 1600000000000000000000000000000000000, 1700000000000000000000000000000000000, 1800000000000000000000000000000000000, 1900000000000000000000000000000000000, 2800000000000000000000000000000000000, 3800000000000000000000000000000000000, 5000000000000000000000000000000000000, 6000000000000000000000000000000000000, 7000000000000000000000000000000000000, 8000000000000000000000000000000000000, 9000000000000000000000000000000000000,
10000000000000000000000000000000000000, 15000000000000000000000000000000000000, 30000000000000000000000000000000000000, 50000000000000000000000000000000000000, 80000000000000000000000000000000000000,
100000000000000000000000000000000000000, 150000000000000000000000000000000000000, 200000000000000000000000000000000000000, 250000000000000000000000000000000000000, 300000000000000000000000000000000000000, 350000000000000000000000000000000000000, 500000000000000000000000000000000000000, 800000000000000000000000000000000000000, 810000000000000000000000000000000000000, 840000000000000000000000000000000000000, 90000000000000000000000000000000000000, 94000000000000000000000000000000000000,
94150000000000000000000000000000000000, 99990000000000000000000000000000000000,
1000000000000000000000000000000000000000]


global wooden_helmet
global bone_necklace
global bone_ring
global wooden_chestplate
global wooden_leggings
global wooden_slippers

global stone_helmet
global amber_necklace
global amber_ring
global stone_chestplate
global stone_leggings
global sandals

class mob:
  def __init__(self, close_defense, magic_defense, ranged_defense, vitality, max_hp, max_mp, max_dexterity, wisdom, speed, name, drops, chances):
    self.cqcd = close_defense
    self.md = magic_defense
    self.rd = ranged_defense
    self.vit = vitality
    self.mx_hp = max_hp
    self.mx_mp = max_mp
    self.mx_dex = max_dexterity
    self.wis = wisdom
    self.spd = speed
    self.nm = name


wooden_helmet = {
  "name": "wooden_helmet",
  "price": 10,
  "weight": 1,
  "defense": 3,
  "health": 15,
  "hits": 10,
  "item_health": 10,
  "weakness": "fire",
  "type": "helmet",
  "slot": "head",
}

bone_necklace = {
  "name": "bone_necklace",
  "price": 5,
  "defense": 1,
  "health": 5,
  "mana": 10,
  "slot": "necklace",
  "type": "necklace",
}

bone_ring = {
  "price": 5,
  "name": "bone_ring",
  "defense": 2,
  "health": 5,
  "mana": 10,
  "slot": "ring",
  "type": "ring",
}

wooden_chestplate = {
  "name": "wooden_chestplate",
  "price": 20,
  "weight": 3,
  "defense": 5,
  "health": 25,
  "weakness": "fire",
  "slot": "chest",
  "type": "chestplate",
}

wooden_leggings = {
  "name": "wooden_leggings",
  "price": 15,
  "weight": 3,
  "defense": 4,
  "health": 20,
  "weakness": "fire",
  "slot": "legs",
  "type": "leggings",
}

wooden_slippers = {
  "name": "wooden_slippers",
  "price": 10,
  "weight": 2,
  "defense": 3,
  "health": 10,
  "weakness": "fire",
  "slots": "feet",
  "type": "boots",
}

stone_helmet = {
  "name": "stone_helmet",
  "price": 100,
  "weight": 2,
  "defense": 5,
  "health": 20,
  "slot": "head",
  "type": "helmet",
}

amber_necklace = {
  "name": "amber_necklace",
  "price": 50,
  "defense": 2,
  "health": 10,
  "mana": 15,
  "slot": "necklace",
  "type": "necklace",
}

amber_ring = {
  "name": "amber_ring",
  "price": 50,
  "defense": 2,
  "health": 10,
  "mana": 15,
  "slot": "necklace",
  "type": "ring",
}

stone_chestplate = {
  "name": "stone_chestplate",
  "price": 200,
  "weight": 5,
  "defense": 10,
  "health": 40,
  "type": "chestplate",
  "slot": "chest",
}

stone_leggings = {
  "name": "stone_leggings",
  "price": 150,
  "weight": 4,
  "defense": 7,
  "health": 30,
  "slot": "legs",
  "type": "leggings",
}

sandals = {
  "name": "sandals",
  "price": 100,
  "weight": 1,
  "defense": 1,
  "health": 7,
  "type": "boots",
  "slot": "feet",

}


helmets = [wooden_helmet, stone_helmet]

helmets_string = ""

for x in range(len(helmets)):
        helmets_string = helmets_string + helmets[x]["name"] + " costs " + str(helmets[x]["price"]) + " gold. \n"

necklaces = [bone_necklace, amber_necklace]

necklaces_string = ""

for x in range(len(necklaces)):
        necklaces_string = necklaces_string + necklaces[x]["name"] + " costs " + str(necklaces[x]["price"]) + " gold. \n"

rings = [bone_ring, amber_ring]

rings_string = ""

for x in range(len(rings)):
        rings_string = rings_string + rings[x]["name"] + " costs " + str(rings[x]["price"]) + " gold. \n"

chests = [wooden_chestplate, stone_chestplate]

chests_string = ""

for x in range(len(chests)):
        chests_string = chests_string + chests[x]["name"] + " costs " + str(chests[x]["price"]) + " gold. \n"

leggings = [wooden_leggings, stone_leggings]

leggings_string = ""

for x in range(len(leggings)):
        leggings_string = leggings_string + leggings[x]["name"] + " costs " + str(leggings[x]["price"]) + " gold. \n"

boots = [wooden_slippers, sandals]

boots_string = ""

for x in range(len(boots)):
        boots_string = boots_string + boots[x]["name"] + " costs " + str(boots[x]["price"]) + " gold. \n"


#Weapons

#daggers can use poison. Swords can not. 

wooden_sword = {
  "name": "wooden_sword",
  "dexterity_take": 10,
  "price": 10,
  "hits": 10,
  "damage": 10,
  "weakness": "fire",
  "slot": "hand",
  "type": "sword",
}

wooden_dagger = {
  "name": "wooden_dagger",
  "dexterity_take": 5,
  "price": 10,
  "hits": 10,
  "damage": 7,
  "weakness": "fire",
  "slot": "hand",
  "type": "dagger",
}

stone_sword = {
  "name": "wooden_sword",
  "dexterity_take": 15,
  "price": 100,
  "hits": 40,
  "damage": 20,
  "weakness": "fire",
  "slot": "hand",
  "type": "sword",
}

stone_dagger = {
  "name": "stone_dagger",
  "dexterity_take": 10,
  "price": 100,
  "hits": 40,
  "damage": 14,
  "slot": "hand",
  "type": "dagger",
}

#ranged

lesser_wooden_bow = {
  "name": "lesser_wooden_bow",
  "dexterity_take": 8,
  "price": 10,
  "hits": 20,
  "damage": 5,
  "ap": 5,
  "weakness": "fire",
  "accuracy": 30,
  "slot": "hand",
  "type": "bow",
}

greater_wooden_bow = {
  "name": "greater_wooden_bow",
  "dexterity_take": 16,
  "price": 100,
  "hits": 50,
  "damage": 12,
  "ap": 15,
  "weakness": "fire",
  "accuracy": 45,
  "slot": "hand",
  "type": "bow",
}

wooden_arrow = {
  "name": "wooden_arrow",
  "price": 1,
  "hits": 50,
  "damage": 5,
  "ap": 3,
  "weakness": "fire",
  "slot": "quiver",
  "type": "arrow",

}

stone_arrow = {
  "name": "stone_arrow",
  "price": 20,
  "hits": 50,
  "damage": 12,
  "ap": 5,
  "slot": "quiver",
  "type": "arrow",
}


#pickaxses
global stone_pickaxe
global copper_pickaxe
global tin_pickaxe
global iron_pickaxe
global steel_pickaxe
global titanium_pickaxe 
global cobalt_pickaxe
global mythic_pickaxe
global molten_pickaxe

stone_pickaxe = {
  "name": "stone_pickaxe",
  "stamina_take": 2,
  "gold_drop_rate": 3,
  "price": 0.25,
  "hits": 10,
  "hardness": 1,
  "drop_multiplier": 1,
  "type": "pickaxe",
}

copper_pickaxe = {
  "name": "copper_pickaxe",
  "stamina_take": 4,
  "gold_drop_rate": 9,
  "price": 4,
  "hits": 50,
  "hardness": 2,
  "drop_multiplier": 1,
  "type": "pickaxe",
}

tin_pickaxe = {
  "name": "tin_pickaxe",
  "stamina_take": 5,
  "gold_drop_rate": 20,
  "price": 13,
  "hits": 100,
  "hardness": 10,
  "drop_multiplier": 2,
  "type": "pickaxe",
}

iron_pickaxe = {
  "name": "iron_pickaxe",
  "stamina_take": 6,
  "gold_drop_rate": 25,
  "price": 80,
  "hits": 100,
  "hardness": 30,
  "drop_multiplier": 10,
  "type": "pickaxe",
}

steel_pickaxe = {
  "name": "steel_pickaxe",
  "stamina_take": 7,
  "gold_drop_rate": 30,
  "price": 2000,
  "hits": 300,
  "hardness": 35,
  "drop_multiplier": 60,
  "type": "pickaxe",
}

titanium_pickaxe = {
  "name": "titanium_pickaxe",
  "stamina_take": 3,
  "gold_drop_rate": 50,
  "price": 25000,
  "hits": 1000,
  "hardness": 100,
  "drop_multiplier": 360,
  "type": "pickaxe",
}

cobalt_pickaxe = {
  "name": "cobalt_pickaxe",
  "stamina_take": 10,
  "gold_drop_rate": 65,
  "price": 200000,
  "hits": 1000,
  "hardness": 300,
  "drop_multiplier": 1000,
  "type": "pickaxe",
}

mythic_pickaxe = {
  "name": "mythic_pickaxe",
  "stamina_take": 20,
  "gold_drop_rate": 70,
  "price": 1000000,
  "hits": 1000,
  "hardness": 1000,
  "drop_multiplier": 5000,
  "type": "pickaxe",
}

molten_pickaxe = {
  "name": "molten_pickaxe",
  "stamina_take": 25,
  "gold_drop_rate": 75,
  "price": 15000000,
  "hits": 1000,
  "hardness": 3000,
  "drop_multiplier": 75000,
  "type": "pickaxe",
}

nuclear_pickaxe = {
  "name": "nuclear_pickaxe",
  "stamina_take": 20,
  "gold_drop_rate": 76,
  "price": 35000000,
  "hits": 1000,
  "hardness": 20000,
  "drop_multiplier": 5000000,
  "type": "pickaxe",
}

fusion_pickaxe = {
  "name": "fusion_pickaxe",
  "stamina_take": 15,
  "gold_drop_rate": 77,
  "price": 15000000,
  "hits": 100,
  "hardness": 100,
  "drop_multiplier": 100000000,
  "type": "pickaxe",
}

quantum_pickaxe = {
  "name": "quantum_pickaxe",
  "stamina_take": 5,
  "gold_drop_rate": 78,
  "price": 15000000,
  "hits": 1000,
  "hardness": 3000,
  "drop_multiplier": 75000,
  "type": "pickaxe",

}
pickaxes = [stone_pickaxe, copper_pickaxe, tin_pickaxe, iron_pickaxe, steel_pickaxe, titanium_pickaxe, cobalt_pickaxe, mythic_pickaxe, molten_pickaxe]

pickaxes_string = ""

for x in range(len(pickaxes)):
        pickaxes_string = pickaxes_string + pickaxes[x]["name"] + " costs " + str(pickaxes[x]["price"]) + " gold. \n"

fuck_you1 = ["https://tenor.com/view/pixel-art-crawling-scary-onii-chan-anime-gif-17533676","fuck you då", "jävla inavel barn svär åt mig jävla hora jävla", "JAGSYDJNWHSJSHWHTSHUTTHEFUCKUPBITCYOUFUCKENGIDIOTOMGYOURSOFUCKENDUMYOUFUCKENIDIOTOMGGGG", "https://www.youtube.com/watch?v=lptc0NjIHq8", "https://tenor.com/view/anime-manga-onii-chan-japanese-anime-japanese-manga-gif-5510123", "Vi kör for**nut** varje dag", "Jag är död inombords", "Anal-Kanal", "https://discordapp.com/channels/808768243115622480/809488642099380274", "Göld digger?", "ANKA?!", "böld i anal körteln på en fin fin anka mmmmmmm ge mig dina referater *NU*!","BBB (Big black böld)", "Käften jävla oompa loompa", "wafan- WIlliam", "discord.ctx.kukböld","https://tenor.com/view/jeppelm-not-gay-jlm15-cutie-smuk-gif-16998589", "https://tenor.com/view/soy-rage-soy-gay-soyboy-gif-13738989","-1","äpple = -1", "https://tenor.com/view/tian-ling-qian-ye-gif-anime-dance-anime-girl-dancing-girl-gif-15203084", "hamudi habubi"

]

factions = ["Anals","B-soceity","Farmers","TTHFFT"]















#defining stuff
def element_damage_cal(attacker_element, defender_element):
  pass



def Betala(giving, getting, amount):
  """Pay by updating db gold the getting(id) the amount(float) and subtract the giving persons db gold that amount. Cannot pay more than you own. No going minus.
   """

  #getting and giving are in ID

  amount = float(amount)
  current_balance_getter = (tdb.search(tdb_user.id == int(getting)))[0]["gold"]

  current_balance_giver = (tdb.search(tdb_user.id == int(giving)))[0]["gold"]

  #checking so no one goes minus or sending - money

  if current_balance_giver < amount or amount < 0:
    return False

  #math

  set_getter_gold_to = current_balance_getter + amount

  set_giver_gold_to = current_balance_giver - amount

  #setting the db to the new values

  #giver set
  tdb.update({"gold" : float(set_giver_gold_to)}, tdb_user.id == int(giving))

  #getter set
  tdb.update({"gold" : float(set_getter_gold_to)}, tdb_user.id == int(getting))


def Get_ID(name):
  return tdb.search(tdb_user.name == name)[0]["id"]


def Add_Inv(item, inventory_id):

  inv_now = tdb.search(tdb_user.id == inventory_id)[0]["inventory"]
  set_inv_to = []

  for i in inv_now:
    set_inv_to.append(i)

  set_inv_to.append(item)

  tdb.update({"inventory":  set_inv_to}, tdb_user.id == inventory_id)

def Hand(item, id):
  wearing_now = tdb.search(tdb_user.id == id)[0]["wearing"]

  hand_now = wearing_now["hand"]

  inv_now = tdb.search(tdb_user.id == id)[0]["inventory"]

  set_hand_to = [item]

  set_inv_to = inv_now

  set_inv_to.remove(item)
  
  if len(hand_now) > 0:
    set_inv_to.append(hand_now[0])

  tdb.update({"inventory":  set_inv_to}, tdb_user.id == id)

  set_wearing_to = wearing_now
  set_wearing_to["hand"] = set_hand_to

  tdb.update({"wearing":  set_wearing_to}, tdb_user.id == id)

def Dequip(id):
  wearing_now = tdb.search(tdb_user.id == id)[0]["wearing"]
  hand = wearing_now["hand"]
  inv_now = tdb.search(tdb_user.id == id)[0]["inventory"]

  inv_now.append(hand[0])

  set_inv_to = inv_now

  set_wearing_to = wearing_now
  set_wearing_to["hand"] = []

  tdb.update({"wearing": set_wearing_to}, tdb_user.id == id)
  
  
  tdb.update({"inventory":  set_inv_to}, tdb_user.id == id)


def Mine(id):
  """Mines """
  wearing_now = tdb.search(tdb_user.id == id)
  hand = wearing_now["hand"]

  
  #minus hits
  damage = 1
  #Borken pick, 
  stats =[False, 0, False]
  hand[0]["hits"] = hand[0]["hits"] - damage
  updated_hits = hand

  set_wearing_to = wearing_now
  set_wearing_to["hand"] = updated_hits
  tdb.update({"wearing": set_wearing_to}, tdb_user.id == id)

  if wearing_now["hand"][0]["hits"] == 0:
    set_wearing_to["hand"] = []
    tdb.update({"wearing": set_wearing_to}, tdb_user.id == id)
    stats[0] = True
  
  #stmaina
  if (tdb.search(tdb_user.id == id)[0]["stamina"] - hand[0]["stamina_take"]) >= 0:
    new_value_for_stamina = tdb.search(tdb_user.id == id)[0]["stamina"]
    stamina_new = new_value_for_stamina - hand[0]["stamina_take"]
    tdb.update({"stamina": int(stamina_new)}, tdb_user.id == id)

    #mine gold
    drop = random.randint(0,1000)
    if drop <= 10 * hand[0]["gold_drop_rate"]:
      number_of_gold = 1 * hand[0]["drop_multiplier"]

      tdb.update({"gold": number_of_gold + tdb.search(tdb_user.id == id)[0]["gold"]}, tdb_user.id == id)
      stats[1] = number_of_gold

    set_stat = tdb.search(tdb_user.id == id)[0]["stats"]
    set_stat["mined"] = set_stat["mined"] + 1
    tdb.update({"stats": set_stat}, tdb_user.id == id)
  else:
    stats[2] = True
  #return the stats
  return stats
async def Stamina_Add(amount):

  while True:
  
    for x in tdb:
      

      if x["stamina"] == x["max_stamina"]:
        pass

      elif x["max_stamina"] - x["stamina"] >= amount:
        tdb.update({"stamina": x["stamina"] + amount}, tdb_user.id == x["id"])

      else:
        n_amount = x["max_stamina"] - x["stamina"]
        tdb.update({"stamina": x["stamina"] + n_amount}, tdb_user.id == x["id"])
    await asyncio.sleep(60)



#Login console
@bot.event
async def on_ready():
  print("Just logged in as {0.user}".format(bot))

@bot.command()
async def mine(ctx):
  """ You can mine using your pickaxe held in your hand. Mine only works in mines. """
  wearing_now = tdb.search(tdb_user.id == ctx.author.id)
  hand = wearing_now["hand"]

  if len(hand) == 0:
    await ctx.channel.send(ctx.author.name +" Your hand is empty, you can not mine.")

  elif hand[0]["type"] != "pickaxe":
    await ctx.channel.send(ctx.author.name +" You must be holding a pickaxe to mine.")
  elif str(ctx.channel) == "mine" or str(ctx.channel) == "mine-2" or str(ctx.channel) == "mine-3" or str(ctx.channel) == "mine-4" or str(ctx.channel) == "mine-5":
    
    x = Mine(ctx.author.id)
    if x[2] == False:
      if x[0]:
        if x[1] > 0:
          await ctx.channel.send(ctx.author.name +" Your pickaxe broke, but at least you got " + str(x[1]) + "gold. Your pickaxe has now got " + str(hand[0]["hits"]) + " hits left.\n\n  Your **stamina**:" + str(tdb.search(tdb_user.id == ctx.author.id)[0]["stamina"]))
        else:
          await ctx.channel.send(ctx.author.name +" Bad luck, your pickaxe broke, and you got 0 gold.\n\n Your **stamina**:" + str(tdb.search(tdb_user.id == ctx.author.id)[0]["stamina"]))
      else:
        if x[1] > 0:
          await ctx.channel.send(ctx.author.name+ " struck " + str(x[1]) + " **GOLD** after mining.\n\n Your pickaxe has now got " + str(hand[0]["hits"]) + " hits left.\n\nYour **stamina**:" + str(tdb.search(tdb_user.id == ctx.author.id)[0]["stamina"]))
        else:
          await ctx.channel.send(ctx.author.name+ " got no gold after mining.\n\n Your pickaxe has now got " + str(hand[0]["hits"]) + " **hits** left.\n\n Your **stamina**:" + str(tdb.search(tdb_user.id == ctx.author.id)[0]["stamina"]))
    else:
      await ctx.channel.send(ctx.author.name + " You don't have enough stamina to mine.\n\n **Your stamina**:" + str(tdb.search(tdb_user.id == ctx.author.id)[0]["stamina"]) + " .\n\n **Required stamina**: " + str(tdb.search(tdb_user.id == ctx.author.id)[0]["wearing"]["hand"][0]["stamina_take"]))

  else:

    await ctx.channel.send(ctx.author.name +" You must be at mine to mine.")

#!money
@bot.command()
async def money(ctx):
  """Writes amount of money (as in gold)"""
  await ctx.channel.send("You currently have " + str(tdb.search(tdb_user.id == ctx.author.id)[0]["gold"]) + " gold")


#Adds authors id to the db, giving them 10 gold in the process
#!register
@bot.command()
async def register(ctx):
  """Registers user to database """
  if tdb.search(tdb_user.id == ctx.author.id):
    await ctx.channel.send("You are already registered")
  else:

    user_insert_dict ={
      "id": ctx.author.id,
      "gold": 1,
      "name": ctx.author.name,
      "discriminator": ctx.author.discriminator,
      "inventory": [],
      "max_stamina": 100,
      "health": 100,
      "max_health": 100,
      "wearing": {
        "head": [],
        "necklace": [],
        "ring": [],
        "back": [],
        "chest":[],
        "legs": [],
        "feet": [],
        "hand": [],
      },
      "stats": [{"close_defense": 10,
        "magic_defense": 10,
        "ranged_defense": 10,
        "vitality": 30,
        "max_hp": 100,
        "max_mp": 100,
        "max_dexterity": 100,
        "wisdom": 30,
        "speed": 50,
        "wins": 0,
        "loses": 0,
        "mined": 0,
        "close_combat_level": 0,
        "ranged_combat_level": 0,
        "magic_combat_level": 0,
        "mining_level": 0}],
      "stamina": 100

    }
    tdb.insert(user_insert_dict)

    await ctx.channel.send("You are now registered and up to date in the DataBase with key: " + str(ctx.author.id)  )

#!pay
@bot.command()
async def pay(ctx, person, amount):
  """With !pay (name of person you want to pay) (amount of money, decimals separated with .) you can pay people """



  reciver_id = Get_ID(person)
  Betala(ctx.author.id, reciver_id, float(amount))
  
  await ctx.channel.send(ctx.author.name +" You now have " + str(tdb.search(tdb_user.id == ctx.author.id)[0]["gold"]) + " gold. Your recipient:" + person  +" now has " + str(tdb.search(tdb_user.id == reciver_id)[0]["gold"]) + " gold.")

#!id
@bot.command()
async def id(ctx):
  """Sends your discord id """
  await ctx.channel.send(ctx.author.id)

#!fuck_you
@bot.command()
async def fuck_you(ctx):
  """Sends a random message from the fuck_you list"""
  await ctx.channel.send(random.choice(fuck_you1))

#!shop    
@bot.command()
async def shop(ctx):
  """Sends content of shop. Only usable at shop. """
  if str(ctx.channel) == "shop":

    await ctx.channel.send(f'{pickaxes_string}\n{helmets_string}\n{necklaces_string}\n{rings_string}\n{chests_string}\n{leggings_string}\n{boots_string}')

  else:
    x = random.randint(1,9)
    if x == 3:
      await ctx.channel.send("You must be at a shop to shop, dummy.")
    else:
      await ctx.channel.send("You must be at a shop to shop.")

#!buy
@bot.command()
async def buy(ctx, to_buy):
  """Buys item from shop you specified after !buy. !buy (item_name) (amount of stuff) """
  if str(ctx.channel) == "shop":

    if len(ctx.message.content.split(" ")) == 1:
      return

    elif len(ctx.message.content.split(" ")) == 2:
      num_of_items = 1
    else:
      num_of_items = int(ctx.message.content.split(" ")[-1])
    #buy right amount of stuff
    for x in range (0, num_of_items):
      #chekc if user able to pay 
      if tdb.search(tdb_user.id == ctx.author.id)[0]["gold"] < globals()[to_buy]["price"]:
        await ctx.send("You don't have enough money to buy that")
      else:
        #take away price of item
        tdb.update({"gold": tdb.search(tdb_user.id == ctx.author.id)[0]["gold"] - globals()[to_buy]["price"] }, tdb_user.id == ctx.author.id)

        #add item to inventory
        Add_Inv(globals()[to_buy], ctx.author.id)

        await ctx.channel.send(ctx.author.name +" You have bought a " + to_buy)

  else:
    x = random.randint(1,9)
    if x == 3:
      await ctx.channel.send("You must be at a shop to shop, dummy.")
    else:
      await ctx.channel.send("You must be at a shop to shop.")


@bot.command()
async def inventory(ctx):
  """Writes your inventory """
  inv_string = " "

  if len(tdb.search(tdb_user.id == ctx.author.id)[0]["inventory"]) == 0:
    await ctx.channel.send("Your inventory is empty")

  else:
    for x in tdb.search(tdb_user.id == ctx.author.id)[0]["inventory"]:
      inv_string = inv_string + x["name"] + ", "
    
    inv_string = inv_string[:-2]

    await ctx.channel.send(ctx.author.name +"s inventory is: " + inv_string)
    
@bot.command()
async def hand(ctx):
  """Puts stuff in your hand. !hand (item_name)"""
  if len(str(ctx.message.content).split(" ")) == 1:
    pass
  else:
    
    item_name = str(ctx.message.content).split(" ")[1]

    user_inv = tdb.search(tdb_user.id == ctx.author.id)[0]["inventory"]    

    out = ""
    for x in user_inv:
      if x["name"] == item_name:
        out = x
        break
    if out == "":
      await ctx.channel.send(ctx.author.name +" The item you wanted to hand is not in your inventory")
    Hand(out, ctx.author.id)
    
    await ctx.channel.send(ctx.author.name +" Your are now holding: " + str(tdb.search(tdb_user.id == ctx.author.id)[0]["wearing"]["hand"][0]["name"]))


@bot.command()
async def in_hand(ctx):
  """Shows whats in your hand """
  hand = tdb.search(tdb_user.id == ctx.author.id)[0]["wearing"]["hand"]

  if len(hand) > 0:
    await ctx.send(ctx.author.name +" In your hand you have: " + hand[0]["name"])
  else:
    await ctx.send(ctx.author.name +" You hand is empty")


@bot.command()             
async def dehand(ctx):
  "Makes your hand empty"  
  in_hand = tdb.search(tdb_user.id == ctx.author.id)[0]["wearing"]["hand"]

  if len(in_hand) > 0:
    item = in_hand[0]["name"]
    Dequip(ctx.author.id)

    await ctx.channel.send(ctx.author.name +" You have dehanded your " + item + ". It is no longer in your hand.")
  else:
    await ctx.channel.send(ctx.author.name +" You hand is already empty")

@bot.command()
async def stamina(ctx):
  """Writes your stamina """
  await ctx.channel.send(ctx.author.name +" You have " + str(tdb.search(tdb_user.id == ctx.author.id)[0]["stamina"]) +  " stamina points, and your **max** amount of stamina is: " + str(tdb.search(tdb_user.id == ctx.author.id)[0]["max_stamina"]))

@bot.command()
async def dance(ctx):
  """1337"""
  with open('ezgif.com-gif-maker.gif', 'rb') as fp:
    await ctx.channel.send(file=discord.File(fp, 'new_filename.gif'))

#!leaderTboard
@bot.command()
async def leaderboard(ctx):
  """Shows leading gold accounts, top 7"""
  
  gold_names = []
  for x in tdb:
    gn = x["gold"]
    gold_names.append(gn)
  
  gold_names.sort(reverse = True)

  suma = 0
  for x in gold_names:
    suma = suma + x
  gold_names = gold_names[0:7]
  out = ""
  for x in gold_names:
    out = out + "#" + str(gold_names.index(x) +1) + ": " + tdb.search(tdb_user.gold == x)[0]["name"] + ": " + str(x) + "  " + str((x / suma) * 100)[:5] + "%, \n \n"
  x = datetime.datetime.now()

  await ctx.send(x.strftime("%c")+ "\n" + out[:-5])
  

@bot.command()
async def update_name(ctx):
  """If you've changed name since you registered, this command can be used to update your name in the database to your new one. """

  tdb.update({"name": ctx.author.name}, ctx.author.id == tdb_user.id)
  tdb.update({"discriminator": ctx.author.discriminator}, ctx.author.id == tdb_user.id)
  await ctx.send("Your name is now up to date")

@bot.command()
async def duel(ctx, opponent, wager):
  """With !duel (name of opponent) (wager) you can send your opponent a request for a duel. If they accept you can fight and the winner will double their wager while the loser will lose their wager. """
  await ctx.send("WIP")

@bot.command()
async def stats(ctx):
  await ctx.send(tdb.search(tdb_user.id == ctx.author.id)[0]["stats"])

@bot.command()
async def equip(ctx, item):

  if tdb.search(tdb_user.id == ctx.author.id)[0]["wearing"][globals()[item]["type"]] == {}:

    update = tdb.search(tdb_user.id == ctx.author.id)[0]["wearing"]

    update[globals()[item]["type"]] = globals()[item]

    tdb.update({"wearing": update}, tdb_user.id == ctx.author.id)

    inv_now = tdb.search(tdb_user.id == ctx.author.id)[0]["inventory"]

    inv_now.remove(globals()[item])

    tdb.update({"inventory": inv_now}, tdb_user.id == ctx.author.id)    

    await ctx.send("You have equiped " + item)

  else:
    slot_now = tdb.search(tdb_user.id == ctx.author.id)[0]["wearing"][globals()[item]["type"]]

    inv_now = tdb.search(tdb_user.id == ctx.author.id)[0]["inventory"]

    inv_now.append(slot_now)

    inv_now.remove(globals()[item])

    print(inv_now)
    
    tdb.update({"inventory": inv_now}, tdb_user.id == ctx.author.id)

    update = tdb.search(tdb_user.id == ctx.author.id)[0]["wearing"]

    update[globals()[item]["type"]] = globals()[item]

    tdb.update({"wearing": update}, tdb_user.id == ctx.author.id)

    await ctx.send("You have dequipped your " + slot_now["name"] + " and you have equipped your " + item)

@bot.command()
async def dequip(ctx, item):
  slot_now = globals()[item]["slot"]

  inv_now = tdb.search(tdb_user.id == ctx.author.id)[0]["inventory"]

  inv_now.append(slot_now)

  tdb.update({"inventory": inv_now}, tdb_user.id == ctx.author.id)
    
  await ctx.send("You have dequipped your " +item)


@bot.command()
async def wearing(ctx):
  out = str(tdb.search(tdb_user.id == ctx.author.id)[0]["wearing"])

  out = out.replace("{", "")
  out = out.replace("}", "")
  out = out.replace("'", "")
  out = out.replace(",", "\n")
  await ctx.send(out)

#Keeps bot running by pinging with UptimeRobot on https://uptimerobot.com/dashboard#787220625

keep_alive()



async def runner():
  await bot.connect()
  await asyncio.sleep(0.001)

loop = asyncio.get_event_loop()
try:
  loop.run_until_complete(bot.login(os.getenv('TOKEN')))
  asyncio.ensure_future(runner())
  asyncio.ensure_future(Stamina_Add(100))
  loop.run_forever()  
finally:
  pass


#Runs bot with key found in the env file





