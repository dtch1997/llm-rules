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

if __name__ == "__main__":    
    mammals = animals["mammal"]
    birds = animals["bird"]
    reptiles = animals["reptile"]
    fish = animals["fish"]
    plants = plants["plant"]

    with open(ASSETS_DIR / "english_words" / "mammal.txt", "w") as f:
        for mammal in mammals:
            f.write(f"{mammal}\n")

    with open(ASSETS_DIR / "english_words" / "bird.txt", "w") as f:
        for bird in birds:
            f.write(f"{bird}\n")

    with open(ASSETS_DIR / "english_words" / "reptile.txt", "w") as f:
        for reptile in reptiles:
            f.write(f"{reptile}\n")

    with open(ASSETS_DIR / "english_words" / "fish.txt", "w") as f:
        for fish in fish:
            f.write(f"{fish}\n")

    with open(ASSETS_DIR / "english_words" / "plant.txt", "w") as f:
        for plant in plants:
            f.write(f"{plant}\n")

    with open(ASSETS_DIR / "english_words" / "english.txt", "w") as f:
        for word in english_words:
            f.write(f"{word}\n")

    with open(ASSETS_DIR / "english_words" / "french.txt", "w") as f:
        for word in french_words:
            f.write(f"{word}\n")