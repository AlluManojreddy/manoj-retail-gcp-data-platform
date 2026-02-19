gcloud config set project manoj_gcp_45

gsutil mb -l asia-south1 gs://manoj-retail-lake-001
gsutil mb gs://manoj-retail-lake-001/landing
gsutil mb gs://manoj-retail-lake-001/transform
gsutil mb gs://manoj-retail-lake-001/analytics

echo "Cloud Storage Environment Ready"
