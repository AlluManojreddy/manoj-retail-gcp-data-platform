gcloud config set project manoj_gcp_45

gcloud dataproc clusters create retail-spark-cluster \
--region=asia-south1 \
--master-machine-type=n1-standard-4 \
--num-workers=2
