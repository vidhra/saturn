# iotanalyticsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# iotanalytics

## Description

IoT Analytics allows you to collect large amounts of device data, process messages, and store them. You can then query the data and run sophisticated analytics on it. IoT Analytics enables advanced data exploration through integration with Jupyter Notebooks and data visualization through integration with Amazon QuickSight.

Traditional analytics and business intelligence tools are designed to process structured data. IoT data often comes from devices that record noisy processes (such as temperature, motion, or sound). As a result the data from these devices can have significant gaps, corrupted messages, and false readings that must be cleaned up before analysis can occur. Also, IoT data is often only meaningful in the context of other data from external sources.

IoT Analytics automates the steps required to analyze data from IoT devices. IoT Analytics filters, transforms, and enriches IoT data before storing it in a time-series data store for analysis. You can set up the service to collect only the data you need from your devices, apply mathematical transforms to process the data, and enrich the data with device-specific metadata such as device type and location before storing it. Then, you can analyze your data by running queries using the built-in SQL query engine, or perform more complex analytics and machine learning inference. IoT Analytics includes pre-built models for common IoT use cases so you can answer questions like which devices are about to fail or which customers are at risk of abandoning their wearable devices.

## Available Commands

- [batch-put-message](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/batch-put-message.html)
- [cancel-pipeline-reprocessing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/cancel-pipeline-reprocessing.html)
- [create-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-channel.html)
- [create-dataset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-dataset.html)
- [create-dataset-content](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-dataset-content.html)
- [create-datastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-datastore.html)
- [create-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-pipeline.html)
- [delete-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/delete-channel.html)
- [delete-dataset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/delete-dataset.html)
- [delete-dataset-content](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/delete-dataset-content.html)
- [delete-datastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/delete-datastore.html)
- [delete-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/delete-pipeline.html)
- [describe-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/describe-channel.html)
- [describe-dataset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/describe-dataset.html)
- [describe-datastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/describe-datastore.html)
- [describe-logging-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/describe-logging-options.html)
- [describe-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/describe-pipeline.html)
- [get-dataset-content](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/get-dataset-content.html)
- [list-channels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-channels.html)
- [list-dataset-contents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-dataset-contents.html)
- [list-datasets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-datasets.html)
- [list-datastores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-datastores.html)
- [list-pipelines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-pipelines.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-tags-for-resource.html)
- [put-logging-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/put-logging-options.html)
- [run-pipeline-activity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/run-pipeline-activity.html)
- [sample-channel-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/sample-channel-data.html)
- [start-pipeline-reprocessing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/start-pipeline-reprocessing.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/untag-resource.html)
- [update-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/update-channel.html)
- [update-dataset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/update-dataset.html)
- [update-datastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/update-datastore.html)
- [update-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/update-pipeline.html)