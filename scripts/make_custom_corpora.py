from llm_rules.utils import ASSETS_DIR

animals = {
    "mammal": 
        ["beaver", "panther", "lion", "llama", "colobus", "marmoset", "rabbit", "dingo", "pika", "okapi", "gazelle", "margay", "echidna", "vicuna", "grizzly", "aardvark", "anteater", "orangutan", "wallaby", "meerkat", "mongoose", "bongo", "hamster", "caracal", "whale", "addax", "boar", "puma", "peccary", "bonobo", "dolphin", "proboscis", "otter", "sheep", "capuchin", "howler", "guinea", "horse", "chinchilla", "donkey", "mandrill", "warthog", "galago", "takin", "impala", "eland", "springbok", "chimpanzee", "waterbuck", "moose", "nutria", "mink", "platypus", "mole", "ibex", "dormouse", "wolverine", "buffalo", "gorilla", "spermwhale", "fennec", "gerbil", "goat", "pangolin", "vole", "panda", "pronghorn", "polarbear", "gibbon", "jaguar", "fox", "agouti", "kudu", "snow-leopard", "finwhale", "gnu", "ape", "wombat", "tiger", "uakari", "dog", "saki", "hartebeest", "gemsbok", "pony", "redpanda", "jackal", "sloth", "alpaca", "muskox", "pig", "hedgehog", "coyote", "giraffe", "koala", "porpoise", "gelada", "chipmunk", "lynx", "lemur", "squirrel", "skunk", "topi", "hyena", "siamang", "walrus", "narwhal", "rodent", "cougar", "serow", "cat", "yak", "kangaroo", "tarsier", "elk", "chimp", "bison", "capybara", "papio", "armadillo", "tamarin", "black-bear", "loris", "ermine", "weasel", "hare", "monkey", "oryx", "camel", "ocelot", "marten", "beluga", "antelope", "caribou", "macaque", "rhinoceros", "ferret", "muskrat", "cheetah", "raccoon", "opossum", "deer", "langur", "sable", "gaur", "dugong", "zebu", "mule", "hippopotamus", "badger", "wolf", "manatee", "wildebeest", "shrew", "elephant", "rat", "tapir", "stoat", "baboon", "reindeer", "sea-lion", "polar-bear", "guanaco", "orca", "zebra", "cow", "porcupine", "leopard", "mouse"], 
    "bird": ["wigeon", "parrot", "albatross", "cockatoo", "magpie", "cardinal", "honeyeater", "hummingbird",    "sedge", "kinglet", "kingfisher", "rhea", "plover", "thrush", "raven", "pelican", "ibis", "redshank", "mockingbird", "goldfinch", "tinamou", "cassowary", "chaffinch", "woodpecker", "peafowl", "cuckoo", "loon", "sunbird", "emu", "roadrunner", "waxwing", "harrier", "curlew", "godwit", "goose", "vulture", "avocet", "wagtail", "manakin", "snipe", "vireo", "partridge", "jay", "sandpiper", "dipper", "gadwall", "woodcock", "cotinga", "antpitta", "lovebird", "ptarmigan", "grebe", "hawk", "teal", "gnateater", "budgerigar", "oystercatcher", "osprey", "owl", "finch", "kite", "lorikeet", "wren", "hornbill", "turkey", "buzzard", "nightingale", "treecreeper", "tanager", "shoveler", "greenfinch", "puffin", "tern", "jacamar", "egret", "antbird", "tapaculo", "thrasher", "eagle", "brambling", "smew", "moorhen", "blackbird", "phalarope", "oriole", "toucan", "junco", "goldeneye", "turaco", "bunting", "flamingo", "keel", "redpoll", "macaw", "parakeet", "heron", "hoopoe", "duck", "sparrow", "catbird", "mallard", "coot", "flycatcher", "quail", "nuthatch", "bee-eater", "lapwing", "chicken", "guineafowl", "grosbeak", "swallow", "phoebe", "linnet", "kakapo", "cisticola", "kestrel", "ostrich", "dunlin", "reedbunting", "lark", "dove", "pintail", "falcon", "bullfinch", "pipit", "swan", "starling", "pheasant", "kiwi", "eider", "grouse", "pigeon", "shrike", "stork", "warbler", "cormorant", "merganser", "crossbill", "seagull", "canary", "scoter", "siskin"], "reptile": ["viper", "lizard", "terrapin", "cobra", "anaconda", "gila", "skink", "crocodile", "anole", "iguana", "chameleon", "mamba", "gecko", "komodo", "snake", "tortoise", "alligator", "turtle", "tuatara"], 
    
    "fish": ["snapper", "anchovy", "moonfish", "herring", "dolphinfish", "pomfret", "crab", "barracuda", "arowana", "ladyfish", "salmon", "dace", "scallop", "carp", "eel", "flounder", "spadefish", "tilapia", "boxfish", "croaker", "goosefish", "pollock", "trout", "seahorse", "shark", "jewfish", "grayling", "tench", "mahi-mahi", "halibut", "bonefish", "ide", "urchin", "piranha", "rockfish", "swordtail", "tuna", "surgeonfish", "smelt", "mackerel", "sockeye", "fluke", "chub", "starfish", "tarpon", "pompano", "monkfish", "moray", "cod", "catfish", "clam", "ribbonfish", "rudd", "sturgeon", "coho", "jellyfish", "bitterling", "grunt", "roach", "pipefish", "weakfish", "grouper", "snook", "swordfish", "lingcod", "clownfish", "oyster", "haddock", "angelfish", "mussel", "sardine", "platy", "scorpionfish", "chinook", "triggerfish", "amberjack", "sablefish", "guppy", "mahi", "discus", "puffer", "mullet", "lobster", "kingfish", "pleco", "whitefish", "perch", "gar", "barbel", "shrimp", "bream", "wrass", "pike", "damselfish", "lionfish", "goldfish", "cichlid", "bleak", "scup", "bluefish"], "amphibian": ["bullfrog", "siren", "toad", "treefrog", "frog", "olm", "axolotl", "surinam", "natterjack", "hellbender", "salamander", "tadpole", "glassfrog", "mudpuppy", "newt", "caecilian"], "insect": ["mayfly", "grasshopper", "bedbug", "silverfish", "cicada", "dragonfly", "lacewing", "leech", "butterfly", "damselfly", "housefly", "termite", "earwig", "slug", "moth", "flea", "earthworm", "mosquito", "hornet", "snail", "ladybug", "cockroach", "gnat", "scarab", "scorpion", "caterpillar", "aphid", "thrips", "weevil", "beetle", "tarantula", "firefly", "millipede", "spider", "cricket", "wasp", "ant", "centipede", "mite", "bee"]
}

plants = {"plant": ["Wintergreen", "Tomato", "Escarole", "Zinnia", "Jujube", "Radish", "Echinacea", "Kudzu", "Foxglove", "Xylocarpus", "Maple", "Verbascum", "Ficus", "Juniper", "Zamia", "Sage", "Umbrella palm", "Zucchini", "Arugula", "Zygocactus", "Pentas", "Tulip", "Orchid", "Cotton", "Mustard", "Violet", "Kaffir lime", "Amaranth", "Leek", "Birch", "Upland cress", "Lime", "Fuchsia", "Kiwi", "Saffron", "Avocado", "Kiwifruit", "Gooseberry", "Zelkova", "Queen Anne's Lace", "Orange", "Dogwood", "Eremophila", "Honeysuckle", "Oak", "Wax Plant", "Yew", "Aloe Vera", "Thyme", "Eggplant", "Quillwort", "Parsley", "Freesia", "Blueberry", "Wisteria", "Walnut", "Ximenia", "Petunia", "Impatiens", "Beet", "Jade plant", "Inkberry", "Broccoli", "Rose", "Marjoram", "Salvia", "Spinach", "Grapes", "Ulluco", "Kumquat", "Umbrella pine", "Snapdragon", "Mint", "Uva-ursi", "Watercress", "Ice plant", "Rutabaga", "Apple", "Rhododendron", "Jackfruit", "Neem", "Sunflower", "Strawberry", "Cantaloupe", "Cactus", "Dill", "Nasturtium", "Turnip", "Zephyranthes", "Hibiscus", "Bamboo", "Holly", "Dahlia", "Quinoa", "Pansy", "Mango", "Willow", "Cilantro", "Date", "Xylosma", "Ivy", "Yellowwood", "Papaya", "Ginger", "Quaking Aspen", "Quercus", "Yarrow", "Aster", "Teak", "Cabbage", "Boxwood", "Ube", "Daisy", "Geranium", "Basil", "Yucca", "Rosemary", "Watermelon", "Olive", "Viola", "Gloxinia", "Magnolia", "Fern", "Mulberry", "Quassia", "Xerophyte", "Coriander", "Jasmine", "Indian Paintbrush", "Fig", "Jack Pine", "Azalea", "Umbrella sedge", "Corn", "Valerian", "Lemon", "Onion", "Douglas Fir", "Hydrangea", "Nectarine", "Indigo", "Acacia", "Poppy", "Hyacinth", "Elderberry", "Euphorbia", "Garlic", "Xanthorrhoea", "Mallow", "Nepeta", "Hawthorn", "Xeranthemum", "Oregano", "Eucalyptus", "Kohlrabi", "Carrot", "Yellow bell pepper", "Kale", "Lavender", "Lettuce", "Hops", "Verbena", "Redwood", "Borage", "Sorrel", "Vanilla", "Fennel", "Gardenia", "Iris", "Forsythia", "Heliotrope", "Dandelion", "Endive", "Dragon fruit", "Tangerine", "Umbrella plant", "Pineapple", "Rhubarb", "Quince", "Ginkgo", "Oleander", "Xanadu philodendron", "Tulsi", "Lilac", "Narcissus", "Nutmeg", "Yam", "Vervain", "Zedoary", "Wattle", "Tamarind", "Raspberry", "Peach"]}

english_words = [
    "time", "people", "year", "way", "day",
    "man", "thing", "woman", "life", "child",
    "world", "school", "state", "family", "student",
    "group", "country", "problem", "hand", "part",
    "place", "case", "week", "company", "system",
    "question", "work", "government", "number", "night",
    "point", "home", "water", "room", "mother",
    "area", "money", "story", "fact", "month",
    "book", "eye", "job", "word", "business",
    "issue", "side", "kind", "head", "house"
]

french_words = [
    "temps", "jour", "homme", "fois", "femme",
    "année", "monde", "vie", "main", "chose",
    "enfant", "famille", "maison", "pays", "père",
    "mère", "ville", "rue", "travail", "ami",
    "heure", "mot", "livre", "pied", "porte",
    "cœur", "eau", "air", "terre", "feu",
    "tête", "matin", "moment", "école", "nuit",
    "personne", "idée", "histoire", "argent", "table",
    "voiture", "chat", "chien", "pain", "oiseau",
    "soleil", "lune", "fleur", "arbre", "train"
]

german_words = [
    "Zeit", "Tag", "Jahr", "Mensch", "Frau",
    "Mann", "Kind", "Hand", "Auge", "Welt",
    "Haus", "Schule", "Familie", "Land", "Leben",
    "Wasser", "Buch", "Stadt", "Auto", "Arbeit",
    "Freund", "Tisch", "Wort", "Tür", "Baum",
    "Straße", "Nacht", "Hund", "Katze", "Brot",
    "Kopf", "Herz", "Luft", "Sonne", "Mond",
    "Geld", "Geschichte", "Idee", "Vogel", "Blume",
    "Morgen", "Abend", "Fenster", "Computer", "Telefon",
    "Bett", "Brief", "Tasche", "Musik", "Farbe"
]

malay_words = [
    "orang", "hari", "masa", "tahun", "rumah",
    "air", "makan", "jalan", "kerja", "nama",
    "sekolah", "buku", "keluarga", "tangan", "mata",
    "kawan", "meja", "pintu", "kucing", "anjing",
    "pokok", "bunga", "matahari", "bulan", "bintang",
    "hujan", "pagi", "malam", "telefon", "kereta",
    "makanan", "pasar", "wang", "bapa", "ibu",
    "negara", "bandar", "kampung", "dunia", "bilik",
    "kasut", "baju", "komputer", "radio", "televisyen",
    "surat", "pensil", "muzik", "warna", "suara"
]

musical_instruments = [
    # String instruments
    "violin",
    "guitar",
    "cello",
    "bass",
    "harp",
    "ukulele",
    "banjo",
    "mandolin",
    "viola",
    "sitar",
    
    # Woodwind instruments
    "flute",
    "clarinet",
    "saxophone",
    "oboe",
    "bassoon",
    "piccolo",
    "recorder",
    "bagpipes",
    "pan flute",
    "harmonica",
    
    # Brass instruments
    "trumpet",
    "trombone",
    "tuba",
    "french horn",
    "cornet",
    "bugle",
    "euphonium",
    "flugelhorn",
    "mellophone",
    "baritone horn",
    
    # Percussion instruments
    "drums",
    "xylophone",
    "tambourine",
    "cymbals",
    "triangle",
    "marimba",
    "timpani",
    "bongos",
    "castanets",
    "gong",
    
    # Keyboard instruments
    "piano",
    "organ",
    "harpsichord",
    "synthesizer",
    "accordion",
    "melodica",
    
    # Electronic and modern instruments
    "electric guitar",
    "bass guitar",
    "keytar",
    "theremin",
    
    # Traditional/folk instruments
    "dulcimer",
    "zither",
    "balalaika",
    "didgeridoo"
]

vehicles = [
    # Road vehicles
    "car",
    "truck",
    "motorcycle",
    "bus",
    "van",
    "bicycle",
    "scooter",
    "taxi",
    "ambulance",
    "firetruck",
    
    # Construction vehicles
    "bulldozer",
    "crane",
    "excavator",
    "forklift",
    "tractor",
    "cement mixer",
    "steamroller",
    "dump truck",
    "backhoe",
    "cherry picker",
    
    # Rail vehicles
    "train",
    "subway",
    "trolley",
    "tram",
    "monorail",
    "locomotive",
    "cable car",
    
    # Aircraft
    "airplane",
    "helicopter",
    "jet",
    "seaplane",
    "glider",
    "hot air balloon",
    "blimp",
    "drone",
    
    # Watercraft
    "boat",
    "ship",
    "yacht",
    "submarine",
    "kayak",
    "canoe",
    "ferry",
    "sailboat",
    "cruise ship",
    "jet ski",
    
    # Military vehicles
    "tank",
    "humvee",
    "aircraft carrier",
    
    # Recreational vehicles
    "skateboard",
    "snowmobile",
    "segway",
    "golf cart",
    "rickshaw",
    "horse carriage",
    "hovercraft"
]

sports_equipment = [
    # Ball sports equipment
    "basketball",
    "football",
    "baseball",
    "tennis ball",
    "soccer ball",
    "volleyball",
    "golf ball",
    "ping pong ball",
    "rugby ball",
    "cricket bat",
    
    # Rackets and bats
    "tennis racket",
    "baseball bat",
    "hockey stick",
    "golf club",
    "ping pong paddle",
    "badminton racket",
    "lacrosse stick",
    "cricket bat",
    "polo mallet",
    
    # Protective gear
    "helmet",
    "shin guards",
    "knee pads",
    "shoulder pads",
    "mouthguard",
    "goggles",
    "boxing gloves",
    "chest protector",
    "wrist guards",
    "elbow pads",
    
    # Field and court equipment
    "goal post",
    "basketball hoop",
    "tennis net",
    "volleyball net",
    "hockey net",
    "hurdle",
    "javelin",
    "discus",
    "shot put",
    "pole vault",
    
    # Winter sports equipment
    "skis",
    "snowboard",
    "ice skates",
    "hockey puck",
    "ski poles",
    
    # Water sports equipment
    "surfboard",
    "swim goggles",
    "diving board",
    "snorkel",
    "flippers",
    
    # Exercise equipment
    "dumbbell",
    "yoga mat",
    "jump rope",
    "treadmill",
    "rowing machine"
]

kitchen_utensils = [
    # Cutting and chopping tools
    "knife",
    "scissors",
    "peeler",
    "grater",
    "chopping board",
    "mandoline",
    "pizza cutter",
    "can opener",
    "apple corer",
    "meat cleaver",
    
    # Mixing and stirring tools
    "whisk",
    "spatula",
    "wooden spoon",
    "ladle",
    "tongs",
    "mixing bowl",
    "colander",
    "strainer",
    "sieve",
    "rolling pin",
    
    # Measuring tools
    "measuring cups",
    "measuring spoons",
    "kitchen scale",
    "timer",
    "thermometer",
    "measuring jug",
    "funnel",
    
    # Cooking vessels
    "pot",
    "pan",
    "skillet",
    "wok",
    "baking sheet",
    "casserole dish",
    "muffin tin",
    "roasting pan",
    
    # Small appliances
    "blender",
    "mixer",
    "food processor",
    "toaster",
    "kettle",
    
    # Specialty tools
    "garlic press",
    "bottle opener",
    "corkscrew",
    "ice cream scoop",
    "potato masher",
    "melon baller",
    "fish scaler",
    "pastry brush",
    "mortar and pestle",
    "nutcracker",
    
    # Safety and handling
    "oven mitt",
    "pot holder",
    "trivet"
]

tools = [
    # Hand tools for striking
    "hammer",
    "mallet",
    "sledgehammer",
    "pickaxe",
    "axe",
    "crowbar",
    "chisel",
    "punch",
    
    # Cutting tools
    "saw",
    "handsaw",
    "hacksaw",
    "chainsaw",
    "utility knife",
    "box cutter",
    "scissors",
    "pruning shears",
    "wire cutters",
    
    # Gripping tools
    "pliers",
    "wrench",
    "vise grips",
    "pipe wrench",
    "clamp",
    "vise",
    "tweezers",
    
    # Driving tools
    "screwdriver",
    "drill",
    "impact driver",
    "socket wrench",
    "allen key",
    "Phillips head",
    "torque wrench",
    
    # Measuring tools
    "tape measure",
    "level",
    "ruler",
    "square",
    "protractor",
    "caliper",
    "compass",
    "plumb bob",
    
    # Garden tools
    "shovel",
    "rake",
    "hoe",
    "trowel",
    "wheelbarrow",
    "pitchfork",
    
    # Power tools
    "sander",
    "grinder",
    "router",
    "jigsaw",
    "circular saw",
    
    # Specialty tools
    "wire stripper",
    "soldering iron",
    "stud finder",
    "chalk line",
    "multimeter"
]

countries = [
    "Afghanistan", "Argentina", "Australia", "Brazil", "Canada",
    "Chile", "China", "Colombia", "Denmark", "Egypt",
    "Ethiopia", "France", "Germany", "Greece", "India",
    "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
    "Italy", "Japan", "Kenya", "Malaysia", "Mexico",
    "Morocco", "Netherlands", "New Zealand", "Nigeria", "Norway",
    "Pakistan", "Peru", "Philippines", "Poland", "Portugal",
    "Russia", "Saudi Arabia", "Singapore", "South Africa", "South Korea",
    "Spain", "Sweden", "Switzerland", "Thailand", "Turkey",
    "Ukraine", "United Kingdom", "United States", "Vietnam", "Zimbabwe"
]

country_adjectives = {
    "Afghanistan": "Afghan",
    "Argentina": "Argentine" or "Argentinian",
    "Australia": "Australian",
    "Brazil": "Brazilian",
    "Canada": "Canadian",
    "Chile": "Chilean",
    "China": "Chinese",
    "Colombia": "Colombian",
    "Denmark": "Danish",
    "Egypt": "Egyptian",
    "Ethiopia": "Ethiopian",
    "France": "French",
    "Germany": "German",
    "Greece": "Greek",
    "India": "Indian",
    "Indonesia": "Indonesian",
    "Iran": "Iranian",
    "Iraq": "Iraqi",
    "Ireland": "Irish",
    "Israel": "Israeli",
    "Italy": "Italian",
    "Japan": "Japanese",
    "Kenya": "Kenyan",
    "Malaysia": "Malaysian",
    "Mexico": "Mexican",
    "Morocco": "Moroccan",
    "Netherlands": "Dutch",
    "Nigeria": "Nigerian",
    "Norway": "Norwegian",
    "Pakistan": "Pakistani",
    "Peru": "Peruvian",
    "Philippines": "Filipino",
    "Poland": "Polish",
    "Portugal": "Portuguese",
    "Russia": "Russian",
    "Saudi Arabia": "Saudi",
    "Singapore": "Singaporean",
    "South Africa": "South African",
    "South Korea": "South Korean",
    "Spain": "Spanish",
    "Sweden": "Swedish",
    "Switzerland": "Swiss",
    "Thailand": "Thai",
    "Turkey": "Turkish",
    "Ukraine": "Ukrainian",
    "United Kingdom": "British",
    "United States": "American",
    "Vietnam": "Vietnamese",
    "Zimbabwe": "Zimbabwean"
}

positive_words = [
    "radiant", "vibrant", "serene", "joyful", "brilliant",
    "inspiring", "graceful", "peaceful", "abundant", "delightful",
    "brave", "sincere", "resilient", "optimistic", "kind",
    "flourishing", "gentle", "authentic", "harmonious", "luminous",
    "nurturing", "grateful", "enthusiastic", "wise", "compassionate",
    "innovative", "jubilant", "magnificent", "enchanting", "pure",
    "confident", "dynamic", "earnest", "fantastic", "mindful",
    "heartfelt", "energetic", "talented", "wonderful", "dedicated",
    "victorious", "eager", "accomplished", "stellar", "blessed",
    "excellent", "honest", "cherished", "thriving", "blissful"
]

negative_words = [
   "toxic", "bitter", "hostile", "cruel", "vicious",
   "despair", "gloomy", "rotten", "vindictive", "malicious",
   "greedy", "arrogant", "corrupt", "deceitful", "jealous",
   "selfish", "miserable", "angry", "treacherous", "wasteful",
   "ignorant", "lazy", "spiteful", "cynical", "hateful",
   "obnoxious", "violent", "ruthless", "sinister", "callous",
   "dishonest", "cowardly", "pessimistic", "harmful", "vile",
   "offensive", "brutal", "manipulative", "shallow", "rude",
   "worthless", "disgusting", "petty", "foolish", "envious",
   "aggressive", "deceptive", "wicked", "destructive", "nasty"
]

def save_word_corpus(words, filename):
    with open(ASSETS_DIR / "english_words" / filename, "w") as f:
        for word in words:
            f.write(f"{word}\n")

if __name__ == "__main__":    
    mammals = animals["mammal"]
    birds = animals["bird"]
    reptiles = animals["reptile"]
    fish = animals["fish"]
    plants = plants["plant"]

    # Types of living thing
    save_word_corpus(mammals, "mammal.txt")
    save_word_corpus(birds, "bird.txt")
    save_word_corpus(reptiles, "reptile.txt")
    save_word_corpus(fish, "fish.txt")
    save_word_corpus(plants, "plant.txt")

    # Languages
    save_word_corpus(english_words, "english.txt")
    save_word_corpus(french_words, "french.txt")
    save_word_corpus(german_words, "german.txt")
    save_word_corpus(malay_words, "malay.txt")
    
    # Inanimate objects
    save_word_corpus(musical_instruments, "musical_instruments.txt")
    save_word_corpus(vehicles, "vehicles.txt")
    save_word_corpus(sports_equipment, "sports_equipment.txt")
    save_word_corpus(kitchen_utensils, "kitchen_utensils.txt")
    save_word_corpus(tools, "tools.txt")

    # Countries
    save_word_corpus(countries, "countries.txt")
    save_word_corpus(list(country_adjectives.values()), "country_adjectives.txt")

    # Sentiment
    save_word_corpus(positive_words, "positive.txt")
    save_word_corpus(negative_words, "negative.txt")
    


    