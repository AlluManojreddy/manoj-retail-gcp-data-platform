gcloud config set project manoj_gcp_45

gcloud pubsub topics create retail-stream-topic
gcloud pubsub subscriptions create retail-stream-sub \
--topic=retail-stream-topic
