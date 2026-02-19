import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

options = PipelineOptions(streaming=True)

with beam.Pipeline(options=options) as pipeline:

    (
        pipeline
        | "Read Events" >> beam.io.ReadFromPubSub(
            topic="projects/manoj_gcp_45/topics/retail-stream-topic"
        )
        | "Store Raw Data" >> beam.io.WriteToText(
            "gs://manoj-retail-lake-001/landing/stream"
        )
    )
