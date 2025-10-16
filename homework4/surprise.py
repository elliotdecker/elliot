# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "-16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "-08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---

# 1) Write a function that uses a loop to print the name of each star.
def print_star_names(stars):
	for name in stars:
		print(name)
print_star_names(targets)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_star_and_spectral_type(stars):
	for name, info in stars.items():
		print(f"{name}: {info.get('Spectral Type', 'Unknown')}")
print_star_and_spectral_type(targets)

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def stars_with_higher_magnitude(stars):
	for name in stars:
		magnitude = stars[name]["Magnitude"]
		if magnitude > 0.1:
			print(name, "has magnitude", magnitude)
stars_with_higher_magnitude(targets)

# 4) Look up another target, add all the necessary information to the targets list. 
targets["Arcturus"] = {
	"RA": "14h 15m 39.7s",
	"Dec": "+19° 10' 56\"",
	"Magnitude": -0.05,
	"Spectral Type": "K 1.5 III Fe-0.5"
}

print(targets["Arcturus"])

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def brightest_star_closest_to_declination_20(stars):
	closest = None
	for name, info in stars.items():
		declination = float(info["Dec"].split("°")[0])
		magnitude = info["Magnitude"]
		difference = abs(declination - 20)
		if not closest or difference < closest[1] or (difference == closest[1] and magnitude < closest[2]):
			closest = (name, difference, magnitude)
	return closest[0]
print(brightest_star_closest_to_declination_20(targets))

# 6) What is your favorite constellation?
#Orion :)
