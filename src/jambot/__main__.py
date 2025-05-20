import sys
import argparse
import logging
from importlib.metadata import version

from .server import server

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("jambot")

def main():
    parser = argparse.ArgumentParser(description="Jambot")
    parser.parse_args()

    logger.info(f"Starting Jambot v{version('jambot')}...")
    try:
        server.run()
    except Exception as e:
        logger.error(f"Server failed to start: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
