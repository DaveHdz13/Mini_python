houses = {
  "🦁 Gryffindor": 0,
  "🦅 Ravenclaw": 0,
  "🦡 Hufflepuff": 0,
  "🐍 Slytherin": 0
}

max_points = 0  # Start with a value lower than possible points

print("""Do you like Dawn or Dusk?
1) Dawn
2) Dusk
""")
res_q1 = int(input("- "))

if res_q1 == 1:
  houses["🦁 Gryffindor"] = houses["🦁 Gryffindor"] + 1
  houses["🦅 Ravenclaw"] = houses["🦅 Ravenclaw"] + 1
elif res_q1 == 2:
  houses["🦡 Hufflepuff"] = houses["🦡 Hufflepuff"] + 1
  houses["🐍 Slytherin"] = houses["🐍 Slytherin"] + 1
else:
  print("Wrong input")

print("""When I'm dead, I want people to remember me as:
1) The Good
2) The Great
3) The Wise
4) The Bold
""")
res_q2 = int(input("- "))

if res_q2 == 1:
  houses["🦡 Hufflepuff"] = houses["🦡 Hufflepuff"] + 2
elif res_q2 == 2:
  houses["🐍 Slytherin"] = houses["🐍 Slytherin"] + 2
elif res_q2 == 3:
  houses["🦅 Ravenclaw"] = houses["🦅 Ravenclaw"] + 2
elif res_q2 == 4:
  houses["🦁 Gryffindor"] = houses["🦁 Gryffindor"] + 2
else:
  print("Wrong input")

print("""Which kind of instrument most pleases your ear?
1) The violin
2) The trumpet
3) The piano
4) The drum
""")
res_q3 = int(input("- "))


if res_q3 == 1:
  houses["🐍 Slytherin"] = houses["🐍 Slytherin"] + 4
elif res_q3 == 2:
  houses["🦡 Hufflepuff"] = houses["🦡 Hufflepuff"] + 4
elif res_q3 == 3:
  houses["🦅 Ravenclaw"] = houses["🦅 Ravenclaw"] + 4
elif res_q3 == 4:
  houses["🦁 Gryffindor"] = houses["🦁 Gryffindor"] + 4
else:
  print("Wrong input")

for house, points in houses.items():
    if points > max_points:
        max_points = points
        winning_house = house

print(f"The house with the most points is {winning_house} with {max_points} points.")