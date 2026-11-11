# PART 4: COMPLETE PIPELINE
def run_pipeline():
    logging.info("Starting pipeline...")

    extracted_data = extract_data()
    transformed_data = transform_data(*extracted_data)
    load_report(transformed_data)

    logging.info("Pipeline completed successfully.")

# Execute
run_pipeline()