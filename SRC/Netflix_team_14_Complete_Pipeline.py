#Import necessary libraries
import logging

from Netflix_team_14_Extract import extract_data
from Netflix_team_14_Transform import transform_data
from Netflix_team_14_Load_Report import load_report

logging.basicConfig(level=logging.INFO)
# PART 4: COMPLETE PIPELINE
def run_pipeline():
    logging.info("Starting pipeline...")

    extracted_data = extract_data()
    transformed_data = transform_data(*extracted_data)
    load_report(transformed_data)

    logging.info("Pipeline completed successfully.")

# Run it to test or debug the transformation (Main guard)
if __name__ == "__main__":
    run_pipeline()