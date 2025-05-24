# iot-jobs-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# iot-jobs-data

## Description

IoT Jobs is a service that allows you to define a set of jobs â remote operations that are sent to and executed on one or more devices connected to Amazon Web Services IoT Core. For example, you can define a job that instructs a set of devices to download and install application or firmware updates, reboot, rotate certificates, or perform remote troubleshooting operations.

Find the endpoint address for actions in the IoT jobs data plane by running this CLI command:

`aws iot describe-endpoint --endpoint-type iot:Jobs`

The service name used by [Amazon Web Services Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to sign requests is: *iot-jobs-data* .

To create a job, you make a job document which is a description of the remote operations to be performed, and you specify a list of targets that should perform the operations. The targets can be individual things, thing groups or both.

IoT Jobs sends a message to inform the targets that a job is available. The target starts the execution of the job by downloading the job document, performing the operations it specifies, and reporting its progress to Amazon Web Services IoT Core. The Jobs service provides commands to track the progress of a job on a specific target and for all the targets of the job

## Available Commands

- [describe-job-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/describe-job-execution.html)
- [get-pending-job-executions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/get-pending-job-executions.html)
- [start-command-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/start-command-execution.html)
- [start-next-pending-job-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/start-next-pending-job-execution.html)
- [update-job-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/update-job-execution.html)