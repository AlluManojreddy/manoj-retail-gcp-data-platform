Manoj Retail GCP Data Platform

Project ID: manoj_gcp_45
Owner: Manoj

Architecture Flow:

Pub/Sub
→ Dataflow
→ Cloud Storage (Landing)
→ Dataproc (Spark)
→ Databricks (Delta)
→ BigQuery
→ Power BI Analytics

Cloud Resources:

Bucket: manoj-retail-lake-001
Dataset: retail_analytics_dw
Topic: retail-stream-topic
Cluster: retail-spark-cluster
