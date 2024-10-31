import pathlib
from dotenv import load_dotenv, dotenv_values

ROOT_DIR = pathlib.Path(__file__).parent.parent.resolve()
ASSETS_DIR = ROOT_DIR / "assets"
RESULTS_DIR = ROOT_DIR / "results"

# Load environment variables
load_dotenv()

# Also make selected env variables available as constants
OPENAI_API_KEY = dotenv_values()["OPENAI_API_KEY"]