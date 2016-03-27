CREATE DB.md

from videogames.models import *

Genre.objects.create(genre="Action")
Genre.objects.create(genre="Adventure")
Genre.objects.create(genre="Puzzle")
Genre.objects.create(genre="Racing")
Genre.objects.create(genre="Simulation")
Genre.objects.create(genre="RPG")


Platform.objects.create(
	platform="3DS", 
    manufactorer="Nintendo",
    consoleType=2
)

Platform.objects.create(
	platform="PS4", 
    manufactorer="Sony Computer Entertainment",
    consoleType=1
)


Platform.objects.create(
	platform="Xbox One", 
    manufactorer="Microsoft",
    consoleType=1
)

Developer.objects.create(
	developer = "Nintendo Worldwide",
	headquarters = "Tokyo, Japan",
	market = 1,
)

Developer.objects.create(
	developer = "AQ Interactive",
	headquarters = "London, UK",
	market = 1,
)

Developer.objects.create(
	developer = "Activision Inc.",
	headquarters = "Berlin, Germany",
	market = 1,
)



