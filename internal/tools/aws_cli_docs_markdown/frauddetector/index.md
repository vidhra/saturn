# frauddetectorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# frauddetector

## Description

This is the Amazon Fraud Detector API Reference. This guide is for developers who need detailed information about Amazon Fraud Detector API actions, data types, and errors. For more information about Amazon Fraud Detector features, see the [Amazon Fraud Detector User Guide](https://docs.aws.amazon.com/frauddetector/latest/ug/) .

We provide the Query API as well as AWS software development kits (SDK) for Amazon Fraud Detector in Java and Python programming languages.

The Amazon Fraud Detector Query API provides HTTPS requests that use the HTTP verb GET or POST and a Query parameter `Action` . AWS SDK provides libraries, sample code, tutorials, and other resources for software developers who prefer to build applications using language-specific APIs instead of submitting a request over HTTP or HTTPS. These libraries provide basic functions that automatically take care of tasks such as cryptographically signing your requests, retrying requests, and handling error responses, so that it is easier for you to get started. For more information about the AWS SDKs, go to [Tools to build on AWS](https://aws.amazon.com/developer/tools/) page, scroll down to the **SDK** section, and choose plus (+) sign to expand the section.

## Available Commands

- [batch-create-variable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/batch-create-variable.html)
- [batch-get-variable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/batch-get-variable.html)
- [cancel-batch-import-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/cancel-batch-import-job.html)
- [cancel-batch-prediction-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/cancel-batch-prediction-job.html)
- [create-batch-import-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-batch-import-job.html)
- [create-batch-prediction-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-batch-prediction-job.html)
- [create-detector-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-detector-version.html)
- [create-list](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-list.html)
- [create-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-model.html)
- [create-model-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-model-version.html)
- [create-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-rule.html)
- [create-variable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-variable.html)
- [delete-batch-import-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-batch-import-job.html)
- [delete-batch-prediction-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-batch-prediction-job.html)
- [delete-detector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-detector.html)
- [delete-detector-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-detector-version.html)
- [delete-entity-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-entity-type.html)
- [delete-event](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-event.html)
- [delete-event-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-event-type.html)
- [delete-events-by-event-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-events-by-event-type.html)
- [delete-external-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-external-model.html)
- [delete-label](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-label.html)
- [delete-list](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-list.html)
- [delete-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-model.html)
- [delete-model-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-model-version.html)
- [delete-outcome](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-outcome.html)
- [delete-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-rule.html)
- [delete-variable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-variable.html)
- [describe-detector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/describe-detector.html)
- [describe-model-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/describe-model-versions.html)
- [get-batch-import-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-batch-import-jobs.html)
- [get-batch-prediction-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-batch-prediction-jobs.html)
- [get-delete-events-by-event-type-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-delete-events-by-event-type-status.html)
- [get-detector-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-detector-version.html)
- [get-detectors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-detectors.html)
- [get-entity-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-entity-types.html)
- [get-event](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-event.html)
- [get-event-prediction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-event-prediction.html)
- [get-event-prediction-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-event-prediction-metadata.html)
- [get-event-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-event-types.html)
- [get-external-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-external-models.html)
- [get-kms-encryption-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-kms-encryption-key.html)
- [get-labels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-labels.html)
- [get-list-elements](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-list-elements.html)
- [get-lists-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-lists-metadata.html)
- [get-model-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-model-version.html)
- [get-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-models.html)
- [get-outcomes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-outcomes.html)
- [get-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-rules.html)
- [get-variables](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-variables.html)
- [list-event-predictions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/list-event-predictions.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/list-tags-for-resource.html)
- [put-detector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-detector.html)
- [put-entity-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-entity-type.html)
- [put-event-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-event-type.html)
- [put-external-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-external-model.html)
- [put-kms-encryption-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-kms-encryption-key.html)
- [put-label](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-label.html)
- [put-outcome](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-outcome.html)
- [send-event](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/send-event.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/untag-resource.html)
- [update-detector-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-detector-version.html)
- [update-detector-version-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-detector-version-metadata.html)
- [update-detector-version-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-detector-version-status.html)
- [update-event-label](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-event-label.html)
- [update-list](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-list.html)
- [update-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-model.html)
- [update-model-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-model-version.html)
- [update-model-version-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-model-version-status.html)
- [update-rule-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-rule-metadata.html)
- [update-rule-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-rule-version.html)
- [update-variable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-variable.html)