# Cloud Data Lake & Enterprise Analytics Platform on Google Cloud

---

## Project Overview

This project demonstrates an end-to-end Enterprise Cloud Data Lake and Analytics Platform built on Google Cloud Platform (GCP) using retail enterprise data.

The solution implements a layered data lake architecture (Raw -> Processed -> Curated) and integrates scalable batch and streaming pipelines to enable enterprise-grade analytics and reporting. It covers ingestion, transformation, warehousing, orchestration, and business intelligence integration using modern cloud-native data engineering tools.

---

## Architecture Overview

### 1. Data Lake Layer
- Google Cloud Storage (Raw / Processed / Curated Zones)
- Delta Lake (Databricks)

### 2. Data Ingestion Layer
- Google Pub/Sub (Streaming Ingestion)
- Batch Data Loads into GCS

### 3. Processing Layer
- Dataflow (Apache Beam) - Real-Time Processing
- Dataproc (Apache Spark) - Batch Transformations
- Databricks - SCD Type 2 and Delta Transformations

### 4. Data Warehouse Layer
- BigQuery (Partitioned and Clustered Tables)

### 5. Orchestration Layer
- Cloud Composer (Apache Airflow)

### 6. Analytics Layer
- Power BI (Enterprise Dashboards and Reporting)

---

## Project Structure

gcp-cloud-data-lake-enterprise-analytics/

├── infrastructure/
│   ├── gcs_setup.sh
│   ├── pubsub_setup.sh
│   ├── dataproc_cluster_setup.sh
│   └── bigquery_setup.sql
│
├── gcs/
│   └── bucket_layer_structure.md
│
├── pubsub/
│   └── retail_stream_producer.py
│
├── dataflow/
│   └── stream_processing_pipeline.py
│
├── dataproc/
│   └── spark_batch_transformation.py
│
├── databricks/
│   └── scd_type2_delta_pipeline.py
│
├── bigquery/
│   ├── create_datasets.sql
│   └── fact_sales_partitioned.sql
│
├── composer/
│   └── enterprise_data_pipeline_dag.py
│
├── analytics/
│   └── powerbi_dashboard_documentation.md
│
└── README.md


---

## Technologies Used

- Google Cloud Platform (GCP)
- Google Cloud Storage (GCS)
- Google Pub/Sub
- Apache Beam (Dataflow)
- Apache Spark (Dataproc)
- Databricks (Delta Lake)
- BigQuery
- Cloud Composer (Apache Airflow)
- Power BI
- SQL
- Python

---

## Data Pipeline Flow

1. Raw retail data is ingested into Google Cloud Storage (Raw Layer).
2. Streaming events are published to Google Pub/Sub.
3. Dataflow processes streaming data in real time and performs transformations.
4. Dataproc processes 100+ GB structured and semi-structured datasets using Apache Spark.
5. Curated datasets are stored in Delta Lake (Databricks).
6. Cleaned and modeled data is loaded into BigQuery using partitioning and clustering.
7. Airflow (Cloud Composer) orchestrates and automates the complete workflow.
8. Power BI connects to BigQuery for enterprise analytics and reporting.

---

## Key Features

- Layered Data Lake Architecture (Raw / Processed / Curated)
- Streaming and Batch Processing Implementation
- Distributed Spark Transformations
- SCD Type 2 Implementation using Delta Lake
- BigQuery Partitioning and Clustering for Cost Optimization
- Automated Orchestration using Airflow
- Enterprise Analytics Integration with Power BI
- Modular and Production-Ready Project Structure

---

## Performance Highlights

- Processed 100+ GB structured and semi-structured datasets using Spark
- Improved transformation performance through distributed processing
- Reduced BigQuery query cost using partitioning and clustering
- Automated enterprise reporting workflows using Airflow

---

## Key Learning Outcomes

- Designed enterprise-scale cloud data lake architecture on GCP
- Built real-time pipelines using Apache Beam (Dataflow)
- Implemented batch ETL workflows using Spark on Dataproc
- Applied Delta Lake concepts with SCD Type 2 modeling
- Integrated BigQuery as enterprise data warehouse
- Automated workflows using Airflow DAGs
- Developed BI-ready analytics pipelines

---

## Author

Manoj Reddy
GCP Data Engineer
Project ID: manoj_gcp_45
