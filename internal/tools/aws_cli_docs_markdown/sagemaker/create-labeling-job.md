# create-labeling-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-labeling-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-labeling-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-labeling-job

## Description

Creates a job that uses workers to label the data objects in your input dataset. You can use the labeled data to train machine learning models.

You can select your workforce from one of three providers:

- A private workforce that you create. It can include employees, contractors, and outside experts. Use a private workforce when want the data to stay within your organization or when a specific set of skills is required.
- One or more vendors that you select from the Amazon Web Services Marketplace. Vendors provide expertise in specific areas.
- The Amazon Mechanical Turk workforce. This is the largest workforce, but it should only be used for public data or data that has been stripped of any personally identifiable information.

You can also use *automated data labeling* to reduce the number of data objects that need to be labeled by a human. Automated data labeling uses *active learning* to determine if a data object can be labeled by machine or if it needs to be sent to a human worker. For more information, see [Using Automated Data Labeling](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-automated-labeling.html) .

The data objects to be labeled are contained in an Amazon S3 bucket. You create a *manifest file* that describes the location of each object. For more information, see [Using Input and Output Data](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data.html) .

The output can be used as the manifest file for another labeling job or as training data for your machine learning models.

You can use this operation to create a static labeling job or a streaming labeling job. A static labeling job stops if all data objects in the input manifest file identified in `ManifestS3Uri` have been labeled. A streaming labeling job runs perpetually until it is manually stopped, or remains idle for 10 days. You can send new data objects to an active (`InProgress` ) streaming labeling job in real time. To learn how to create a static labeling job, see [Create a Labeling Job (API)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-create-labeling-job-api.html) in the Amazon SageMaker Developer Guide. To learn how to create a streaming labeling job, see [Create a Streaming Labeling Job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-create-job.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateLabelingJob)

## Synopsis

```
create-labeling-job
--labeling-job-name <value>
--label-attribute-name <value>
--input-config <value>
--output-config <value>
--role-arn <value>
[--label-category-config-s3-uri <value>]
[--stopping-conditions <value>]
[--labeling-job-algorithms-config <value>]
--human-task-config <value>
[--tags <value>]
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--labeling-job-name` (string)

The name of the labeling job. This name is used to identify the job in a list of labeling jobs. Labeling job names must be unique within an Amazon Web Services account and region. `LabelingJobName` is not case sensitive. For example, Example-job and example-job are considered the same labeling job name by Ground Truth.

`--label-attribute-name` (string)

The attribute name to use for the label in the output manifest file. This is the key for the key/value pair formed with the label that a worker assigns to the object. The `LabelAttributeName` must meet the following requirements.

- The name canât end with â-metadataâ.
- If you are using one of the following [built-in task types](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-task-types.html) , the attribute name *must* end with â-refâ. If the task type you are using is not listed below, the attribute name *must not* end with â-refâ.
- Image semantic segmentation (`SemanticSegmentation)` , and adjustment (`AdjustmentSemanticSegmentation` ) and verification (`VerificationSemanticSegmentation` ) labeling jobs for this task type.
- Video frame object detection (`VideoObjectDetection` ), and adjustment and verification (`AdjustmentVideoObjectDetection` ) labeling jobs for this task type.
- Video frame object tracking (`VideoObjectTracking` ), and adjustment and verification (`AdjustmentVideoObjectTracking` ) labeling jobs for this task type.
- 3D point cloud semantic segmentation (`3DPointCloudSemanticSegmentation` ), and adjustment and verification (`Adjustment3DPointCloudSemanticSegmentation` ) labeling jobs for this task type.
- 3D point cloud object tracking (`3DPointCloudObjectTracking` ), and adjustment and verification (`Adjustment3DPointCloudObjectTracking` ) labeling jobs for this task type.

### Warning

If you are creating an adjustment or verification labeling job, you must use a *different* `LabelAttributeName` than the one used in the original labeling job. The original labeling job is the Ground Truth labeling job that produced the labels that you want verified or adjusted. To learn more about adjustment and verification labeling jobs, see [Verify and Adjust Labels](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-verification-data.html) .

`--input-config` (structure)

Input data for the labeling job, such as the Amazon S3 location of the data objects and the location of the manifest file that describes the data objects.

You must specify at least one of the following: `S3DataSource` or `SnsDataSource` .

- Use `SnsDataSource` to specify an SNS input topic for a streaming labeling job. If you do not specify and SNS input topic ARN, Ground Truth will create a one-time labeling job that stops after all data objects in the input manifest file have been labeled.
- Use `S3DataSource` to specify an input manifest file for both streaming and one-time labeling jobs. Adding an `S3DataSource` is optional if you use `SnsDataSource` to create a streaming labeling job.

If you use the Amazon Mechanical Turk workforce, your input data should not include confidential information, personal information or protected health information. Use `ContentClassifiers` to specify that your data is free of personally identifiable information and adult content.

DataSource -> (structure)

The location of the input data.

S3DataSource -> (structure)

The Amazon S3 location of the input data objects.

ManifestS3Uri -> (string)

The Amazon S3 location of the manifest file that describes the input data objects.

The input manifest file referenced in `ManifestS3Uri` must contain one of the following keys: `source-ref` or `source` . The value of the keys are interpreted as follows:

- `source-ref` : The source of the object is the Amazon S3 object specified in the value. Use this value when the object is a binary object, such as an image.
- `source` : The source of the object is the value. Use this value when the object is a text value.

If you are a new user of Ground Truth, it is recommended you review [Use an Input Manifest File](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-input-data-input-manifest.html) in the Amazon SageMaker Developer Guide to learn how to create an input manifest file.

SnsDataSource -> (structure)

An Amazon SNS data source used for streaming labeling jobs. To learn more, see [Send Data to a Streaming Labeling Job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-labeling-job.html#sms-streaming-how-it-works-send-data) .

SnsTopicArn -> (string)

The Amazon SNS input topic Amazon Resource Name (ARN). Specify the ARN of the input topic you will use to send new data objects to a streaming labeling job.

DataAttributes -> (structure)

Attributes of the data specified by the customer.

ContentClassifiers -> (list)

Declares that your content is free of personally identifiable information or adult content. SageMaker may restrict the Amazon Mechanical Turk workers that can view your task based on this information.

(string)

Shorthand Syntax:

```
DataSource={S3DataSource={ManifestS3Uri=string},SnsDataSource={SnsTopicArn=string}},DataAttributes={ContentClassifiers=[string,string]}
```

JSON Syntax:

```
{
  "DataSource": {
    "S3DataSource": {
      "ManifestS3Uri": "string"
    },
    "SnsDataSource": {
      "SnsTopicArn": "string"
    }
  },
  "DataAttributes": {
    "ContentClassifiers": ["FreeOfPersonallyIdentifiableInformation"|"FreeOfAdultContent", ...]
  }
}
```

`--output-config` (structure)

The location of the output data and the Amazon Web Services Key Management Service key ID for the key used to encrypt the output data, if any.

S3OutputPath -> (string)

The Amazon S3 location to write output data.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service ID of the key used to encrypt the output data, if any.

If you provide your own KMS key ID, you must add the required permissions to your KMS key described in [Encrypt Output Data and Storage Volume with Amazon Web Services KMS](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-permission.html#sms-security-kms-permissions) .

If you donât provide a KMS key ID, Amazon SageMaker uses the default Amazon Web Services KMS key for Amazon S3 for your roleâs account to encrypt your output data.

If you use a bucket policy with an `s3:PutObject` permission that only allows objects with server-side encryption, set the condition key of `s3:x-amz-server-side-encryption` to `"aws:kms"` . For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide.*

SnsTopicArn -> (string)

An Amazon Simple Notification Service (Amazon SNS) output topic ARN. Provide a `SnsTopicArn` if you want to do real time chaining to another streaming job and receive an Amazon SNS notifications each time a data object is submitted by a worker.

If you provide an `SnsTopicArn` in `OutputConfig` , when workers complete labeling tasks, Ground Truth will send labeling task output data to the SNS output topic you specify here.

To learn more, see [Receive Output Data from a Streaming Labeling Job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-labeling-job.html#sms-streaming-how-it-works-output-data) .

Shorthand Syntax:

```
S3OutputPath=string,KmsKeyId=string,SnsTopicArn=string
```

JSON Syntax:

```
{
  "S3OutputPath": "string",
  "KmsKeyId": "string",
  "SnsTopicArn": "string"
}
```

`--role-arn` (string)

The Amazon Resource Number (ARN) that Amazon SageMaker assumes to perform tasks on your behalf during data labeling. You must grant this role the necessary permissions so that Amazon SageMaker can successfully complete data labeling.

`--label-category-config-s3-uri` (string)

The S3 URI of the file, referred to as a *label category configuration file* , that defines the categories used to label the data objects.

For 3D point cloud and video frame task types, you can add label category attributes and frame attributes to your label category configuration file. To learn how, see [Create a Labeling Category Configuration File for 3D Point Cloud Labeling Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-label-category-config.html) .

For named entity recognition jobs, in addition to `"labels"` , you must provide worker instructions in the label category configuration file using the `"instructions"` parameter: `"instructions": {"shortInstruction":"<h1>Add header</h1><p>Add Instructions</p>", "fullInstruction":"<p>Add additional instructions.</p>"}` . For details and an example, see [Create a Named Entity Recognition Labeling Job (API)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-named-entity-recg.html#sms-creating-ner-api) .

For all other [built-in task types](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-task-types.html) and [custom tasks](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates.html) , your label category configuration file must be a JSON file in the following format. Identify the labels you want to use by replacing `label_1` , `label_2` ,``â¦`` ,``label_n`` with your label categories.

`{`

`"document-version": "2018-11-28",`

`"labels": [{"label": "label_1"},{"label": "label_2"},...{"label": "label_n"}]`

`}`

Note the following about the label category configuration file:

- For image classification and text classification (single and multi-label) you must specify at least two label categories. For all other task types, the minimum number of label categories required is one.
- Each label category must be unique, you cannot specify duplicate label categories.
- If you create a 3D point cloud or video frame adjustment or verification labeling job, you must include `auditLabelAttributeName` in the label category configuration. Use this parameter to enter the ` `LabelAttributeName` [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateLabelingJob.html#sagemaker-CreateLabelingJob-request](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateLabelingJob.html#sagemaker-CreateLabelingJob-request)-LabelAttributeName`__ of the labeling job you want to adjust or verify annotations of.

`--stopping-conditions` (structure)

A set of conditions for stopping the labeling job. If any of the conditions are met, the job is automatically stopped. You can use these conditions to control the cost of data labeling.

MaxHumanLabeledObjectCount -> (integer)

The maximum number of objects that can be labeled by human workers.

MaxPercentageOfInputDatasetLabeled -> (integer)

The maximum number of input data objects that should be labeled.

Shorthand Syntax:

```
MaxHumanLabeledObjectCount=integer,MaxPercentageOfInputDatasetLabeled=integer
```

JSON Syntax:

```
{
  "MaxHumanLabeledObjectCount": integer,
  "MaxPercentageOfInputDatasetLabeled": integer
}
```

`--labeling-job-algorithms-config` (structure)

Configures the information required to perform automated data labeling.

LabelingJobAlgorithmSpecificationArn -> (string)

Specifies the Amazon Resource Name (ARN) of the algorithm used for auto-labeling. You must select one of the following ARNs:

- *Image classification* `arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/image-classification`
- *Text classification* `arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/text-classification`
- *Object detection* `arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/object-detection`
- *Semantic Segmentation* `arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/semantic-segmentation`

InitialActiveLearningModelArn -> (string)

At the end of an auto-label job Ground Truth sends the Amazon Resource Name (ARN) of the final model used for auto-labeling. You can use this model as the starting point for subsequent similar jobs by providing the ARN of the model here.

LabelingJobResourceConfig -> (structure)

Provides configuration information for a labeling job.

VolumeKmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training and inference jobs used for automated data labeling.

You can only specify a `VolumeKmsKeyId` when you create a labeling job with automated data labeling enabled using the API operation `CreateLabelingJob` . You cannot specify an Amazon Web Services KMS key to encrypt the storage volume used for automated data labeling model training and inference when you create a labeling job using the console. To learn more, see [Output Data and Storage Volume Encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security.html) .

The `VolumeKmsKeyId` can be any of the following formats:

- KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

VpcConfig -> (structure)

Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

JSON Syntax:

```
{
  "LabelingJobAlgorithmSpecificationArn": "string",
  "InitialActiveLearningModelArn": "string",
  "LabelingJobResourceConfig": {
    "VolumeKmsKeyId": "string",
    "VpcConfig": {
      "SecurityGroupIds": ["string", ...],
      "Subnets": ["string", ...]
    }
  }
}
```

`--human-task-config` (structure)

Configures the labeling task and how it is presented to workers; including, but not limited to price, keywords, and batch size (task count).

WorkteamArn -> (string)

The Amazon Resource Name (ARN) of the work team assigned to complete the tasks.

UiConfig -> (structure)

Information about the user interface that workers use to complete the labeling task.

UiTemplateS3Uri -> (string)

The Amazon S3 bucket location of the UI template, or worker task template. This is the template used to render the worker UI and tools for labeling job tasks. For more information about the contents of a UI template, see [Creating Your Custom Labeling Task Template](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step2.html) .

HumanTaskUiArn -> (string)

The ARN of the worker task template used to render the worker UI and tools for labeling job tasks.

Use this parameter when you are creating a labeling job for named entity recognition, 3D point cloud and video frame labeling jobs. Use your labeling job task type to select one of the following ARNs and use it with this parameter when you create a labeling job. Replace `aws-region` with the Amazon Web Services Region you are creating your labeling job in. For example, replace `aws-region` with `us-west-1` if you create a labeling job in US West (N. California).

**Named Entity Recognition**

Use the following `HumanTaskUiArn` for named entity recognition labeling jobs:

`arn:aws:sagemaker:aws-region:394669845002:human-task-ui/NamedEntityRecognition`

**3D Point Cloud HumanTaskUiArns**

Use this `HumanTaskUiArn` for 3D point cloud object detection and 3D point cloud object detection adjustment labeling jobs.

- `arn:aws:sagemaker:aws-region:394669845002:human-task-ui/PointCloudObjectDetection`

Use this `HumanTaskUiArn` for 3D point cloud object tracking and 3D point cloud object tracking adjustment labeling jobs.

- `arn:aws:sagemaker:aws-region:394669845002:human-task-ui/PointCloudObjectTracking`

Use this `HumanTaskUiArn` for 3D point cloud semantic segmentation and 3D point cloud semantic segmentation adjustment labeling jobs.

- `arn:aws:sagemaker:aws-region:394669845002:human-task-ui/PointCloudSemanticSegmentation`

**Video Frame HumanTaskUiArns**

Use this `HumanTaskUiArn` for video frame object detection and video frame object detection adjustment labeling jobs.

- `arn:aws:sagemaker:region:394669845002:human-task-ui/VideoObjectDetection`

Use this `HumanTaskUiArn` for video frame object tracking and video frame object tracking adjustment labeling jobs.

- `arn:aws:sagemaker:aws-region:394669845002:human-task-ui/VideoObjectTracking`

PreHumanTaskLambdaArn -> (string)

The Amazon Resource Name (ARN) of a Lambda function that is run before a data object is sent to a human worker. Use this function to provide input to a custom labeling job.

For [built-in task types](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-task-types.html) , use one of the following Amazon SageMaker Ground Truth Lambda function ARNs for `PreHumanTaskLambdaArn` . For custom labeling workflows, see [Pre-annotation Lambda](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step3.html#sms-custom-templates-step3-prelambda) .

**Bounding box** - Finds the most similar boxes from different workers based on the Jaccard index of the boxes.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-BoundingBox`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-BoundingBox`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-BoundingBox`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-BoundingBox`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-BoundingBox`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-BoundingBox`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-BoundingBox`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-BoundingBox`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-BoundingBox`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-BoundingBox`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-BoundingBox`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-BoundingBox`

**Image classification** - Uses a variant of the Expectation Maximization approach to estimate the true class of an image based on annotations from individual workers.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-ImageMultiClass`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-ImageMultiClass`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-ImageMultiClass`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-ImageMultiClass`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-ImageMultiClass`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-ImageMultiClass`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-ImageMultiClass`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-ImageMultiClass`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-ImageMultiClass`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-ImageMultiClass`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-ImageMultiClass`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-ImageMultiClass`

**Multi-label image classification** - Uses a variant of the Expectation Maximization approach to estimate the true classes of an image based on annotations from individual workers.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-ImageMultiClassMultiLabel`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-ImageMultiClassMultiLabel`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-ImageMultiClassMultiLabel`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-ImageMultiClassMultiLabel`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-ImageMultiClassMultiLabel`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-ImageMultiClassMultiLabel`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-ImageMultiClassMultiLabel`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-ImageMultiClassMultiLabel`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-ImageMultiClassMultiLabel`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-ImageMultiClassMultiLabel`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-ImageMultiClassMultiLabel`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-ImageMultiClassMultiLabel`

**Semantic segmentation** - Treats each pixel in an image as a multi-class classification and treats pixel annotations from workers as âvotesâ for the correct label.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-SemanticSegmentation`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-SemanticSegmentation`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-SemanticSegmentation`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-SemanticSegmentation`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-SemanticSegmentation`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-SemanticSegmentation`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-SemanticSegmentation`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-SemanticSegmentation`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-SemanticSegmentation`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-SemanticSegmentation`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-SemanticSegmentation`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-SemanticSegmentation`

**Text classification** - Uses a variant of the Expectation Maximization approach to estimate the true class of text based on annotations from individual workers.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-TextMultiClass`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-TextMultiClass`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-TextMultiClass`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-TextMultiClass`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-TextMultiClass`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-TextMultiClass`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-TextMultiClass`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-TextMultiClass`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-TextMultiClass`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-TextMultiClass`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-TextMultiClass`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-TextMultiClass`

**Multi-label text classification** - Uses a variant of the Expectation Maximization approach to estimate the true classes of text based on annotations from individual workers.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-TextMultiClassMultiLabel`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-TextMultiClassMultiLabel`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-TextMultiClassMultiLabel`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-TextMultiClassMultiLabel`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-TextMultiClassMultiLabel`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-TextMultiClassMultiLabel`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-TextMultiClassMultiLabel`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-TextMultiClassMultiLabel`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-TextMultiClassMultiLabel`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-TextMultiClassMultiLabel`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-TextMultiClassMultiLabel`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-TextMultiClassMultiLabel`

**Named entity recognition** - Groups similar selections and calculates aggregate boundaries, resolving to most-assigned label.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-NamedEntityRecognition`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-NamedEntityRecognition`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-NamedEntityRecognition`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-NamedEntityRecognition`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-NamedEntityRecognition`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-NamedEntityRecognition`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-NamedEntityRecognition`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-NamedEntityRecognition`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-NamedEntityRecognition`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-NamedEntityRecognition`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-NamedEntityRecognition`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-NamedEntityRecognition`

**Video Classification** - Use this task type when you need workers to classify videos using predefined labels that you specify. Workers are shown videos and are asked to choose one label for each video.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-VideoMultiClass`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-VideoMultiClass`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-VideoMultiClass`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-VideoMultiClass`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-VideoMultiClass`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-VideoMultiClass`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-VideoMultiClass`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-VideoMultiClass`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-VideoMultiClass`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-VideoMultiClass`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-VideoMultiClass`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-VideoMultiClass`

**Video Frame Object Detection** - Use this task type to have workers identify and locate objects in a sequence of video frames (images extracted from a video) using bounding boxes. For example, you can use this task to ask workers to identify and localize various objects in a series of video frames, such as cars, bikes, and pedestrians.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-VideoObjectDetection`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-VideoObjectDetection`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-VideoObjectDetection`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-VideoObjectDetection`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-VideoObjectDetection`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-VideoObjectDetection`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-VideoObjectDetection`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-VideoObjectDetection`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-VideoObjectDetection`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-VideoObjectDetection`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-VideoObjectDetection`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-VideoObjectDetection`

**Video Frame Object Tracking** - Use this task type to have workers track the movement of objects in a sequence of video frames (images extracted from a video) using bounding boxes. For example, you can use this task to ask workers to track the movement of objects, such as cars, bikes, and pedestrians.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-VideoObjectTracking`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-VideoObjectTracking`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-VideoObjectTracking`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-VideoObjectTracking`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-VideoObjectTracking`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-VideoObjectTracking`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-VideoObjectTracking`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-VideoObjectTracking`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-VideoObjectTracking`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-VideoObjectTracking`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-VideoObjectTracking`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-VideoObjectTracking`

**3D Point Cloud Modalities**

Use the following pre-annotation lambdas for 3D point cloud labeling modality tasks. See [3D Point Cloud Task types](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-task-types.html) to learn more.

**3D Point Cloud Object Detection** - Use this task type when you want workers to classify objects in a 3D point cloud by drawing 3D cuboids around objects. For example, you can use this task type to ask workers to identify different types of objects in a point cloud, such as cars, bikes, and pedestrians.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-3DPointCloudObjectDetection`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-3DPointCloudObjectDetection`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-3DPointCloudObjectDetection`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-3DPointCloudObjectDetection`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-3DPointCloudObjectDetection`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-3DPointCloudObjectDetection`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-3DPointCloudObjectDetection`

**3D Point Cloud Object Tracking** - Use this task type when you want workers to draw 3D cuboids around objects that appear in a sequence of 3D point cloud frames. For example, you can use this task type to ask workers to track the movement of vehicles across multiple point cloud frames.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-3DPointCloudObjectTracking`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-3DPointCloudObjectTracking`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-3DPointCloudObjectTracking`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-3DPointCloudObjectTracking`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-3DPointCloudObjectTracking`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-3DPointCloudObjectTracking`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-3DPointCloudObjectTracking`

**3D Point Cloud Semantic Segmentation** - Use this task type when you want workers to create a point-level semantic segmentation masks by painting objects in a 3D point cloud using different colors where each color is assigned to one of the classes you specify.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-3DPointCloudSemanticSegmentation`

**Use the following ARNs for Label Verification and Adjustment Jobs**

Use label verification and adjustment jobs to review and adjust labels. To learn more, see [Verify and Adjust Labels](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-verification-data.html) .

**Bounding box verification** - Uses a variant of the Expectation Maximization approach to estimate the true class of verification judgement for bounding box labels based on annotations from individual workers.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-VerificationBoundingBox`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-VerificationBoundingBox`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-VerificationBoundingBox`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-VerificationBoundingBox`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-VerificationBoundingBox`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-VerificationBoundingBox`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-VerificationBoundingBox`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-VerificationBoundingBox`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-VerificationBoundingBox`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-VerificationBoundingBox`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-VerificationBoundingBox`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-VerificationBoundingBox`

**Bounding box adjustment** - Finds the most similar boxes from different workers based on the Jaccard index of the adjusted annotations.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-AdjustmentBoundingBox`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-AdjustmentBoundingBox`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-AdjustmentBoundingBox`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-AdjustmentBoundingBox`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-AdjustmentBoundingBox`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-AdjustmentBoundingBox`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-AdjustmentBoundingBox`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-AdjustmentBoundingBox`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-AdjustmentBoundingBox`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-AdjustmentBoundingBox`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-AdjustmentBoundingBox`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-AdjustmentBoundingBox`

**Semantic segmentation verification** - Uses a variant of the Expectation Maximization approach to estimate the true class of verification judgment for semantic segmentation labels based on annotations from individual workers.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-VerificationSemanticSegmentation`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-VerificationSemanticSegmentation`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-VerificationSemanticSegmentation`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-VerificationSemanticSegmentation`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-VerificationSemanticSegmentation`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-VerificationSemanticSegmentation`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-VerificationSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-VerificationSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-VerificationSemanticSegmentation`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-VerificationSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-VerificationSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-VerificationSemanticSegmentation`

**Semantic segmentation adjustment** - Treats each pixel in an image as a multi-class classification and treats pixel adjusted annotations from workers as âvotesâ for the correct label.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-AdjustmentSemanticSegmentation`

**Video Frame Object Detection Adjustment** - Use this task type when you want workers to adjust bounding boxes that workers have added to video frames to classify and localize objects in a sequence of video frames.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-AdjustmentVideoObjectDetection`

**Video Frame Object Tracking Adjustment** - Use this task type when you want workers to adjust bounding boxes that workers have added to video frames to track object movement across a sequence of video frames.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-AdjustmentVideoObjectTracking`

**3D point cloud object detection adjustment** - Adjust 3D cuboids in a point cloud frame.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-Adjustment3DPointCloudObjectDetection`

**3D point cloud object tracking adjustment** - Adjust 3D cuboids across a sequence of point cloud frames.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-Adjustment3DPointCloudObjectTracking`

**3D point cloud semantic segmentation adjustment** - Adjust semantic segmentation masks in a 3D point cloud.

- `arn:aws:lambda:us-east-1:432418664414:function:PRE-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:us-east-2:266458841044:function:PRE-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:us-west-2:081040173940:function:PRE-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:eu-west-1:568282634449:function:PRE-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:PRE-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-south-1:565803892007:function:PRE-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:eu-central-1:203001061592:function:PRE-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:PRE-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:eu-west-2:487402164563:function:PRE-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:PRE-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ca-central-1:918755190332:function:PRE-Adjustment3DPointCloudSemanticSegmentation`

TaskKeywords -> (list)

Keywords used to describe the task so that workers on Amazon Mechanical Turk can discover the task.

(string)

TaskTitle -> (string)

A title for the task for your human workers.

TaskDescription -> (string)

A description of the task for your human workers.

NumberOfHumanWorkersPerDataObject -> (integer)

The number of human workers that will label an object.

TaskTimeLimitInSeconds -> (integer)

The amount of time that a worker has to complete a task.

If you create a custom labeling job, the maximum value for this parameter is 8 hours (28,800 seconds).

If you create a labeling job using a [built-in task type](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-task-types.html) the maximum for this parameter depends on the task type you use:

- For [image](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-label-images.html) and [text](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-label-text.html) labeling jobs, the maximum is 8 hours (28,800 seconds).
- For [3D point cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud.html) and [video frame](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video.html) labeling jobs, the maximum is 30 days (2952,000 seconds) for non-AL mode. For most users, the maximum is also 30 days.

TaskAvailabilityLifetimeInSeconds -> (integer)

The length of time that a task remains available for labeling by human workers. The default and maximum values for this parameter depend on the type of workforce you use.

- If you choose the Amazon Mechanical Turk workforce, the maximum is 12 hours (43,200 seconds). The default is 6 hours (21,600 seconds).
- If you choose a private or vendor workforce, the default value is 30 days (2592,000 seconds) for non-AL mode. For most users, the maximum is also 30 days.

MaxConcurrentTaskCount -> (integer)

Defines the maximum number of data objects that can be labeled by human workers at the same time. Also referred to as batch size. Each object may have more than one worker at one time. The default value is 1000 objects. To increase the maximum value to 5000 objects, contact Amazon Web Services Support.

AnnotationConsolidationConfig -> (structure)

Configures how labels are consolidated across human workers.

AnnotationConsolidationLambdaArn -> (string)

The Amazon Resource Name (ARN) of a Lambda function implements the logic for [annotation consolidation](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-annotation-consolidation.html) and to process output data.

For [built-in task types](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-task-types.html) , use one of the following Amazon SageMaker Ground Truth Lambda function ARNs for `AnnotationConsolidationLambdaArn` . For custom labeling workflows, see [Post-annotation Lambda](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step3.html#sms-custom-templates-step3-postlambda) .

**Bounding box** - Finds the most similar boxes from different workers based on the Jaccard index of the boxes.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-BoundingBox`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-BoundingBox`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-BoundingBox`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-BoundingBox`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-BoundingBox`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-BoundingBox`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-BoundingBox`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-BoundingBox`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-BoundingBox`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-BoundingBox`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-BoundingBox`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-BoundingBox`

**Image classification** - Uses a variant of the Expectation Maximization approach to estimate the true class of an image based on annotations from individual workers.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-ImageMultiClass`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-ImageMultiClass`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-ImageMultiClass`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-ImageMultiClass`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-ImageMultiClass`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-ImageMultiClass`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-ImageMultiClass`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-ImageMultiClass`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-ImageMultiClass`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-ImageMultiClass`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-ImageMultiClass`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-ImageMultiClass`

**Multi-label image classification** - Uses a variant of the Expectation Maximization approach to estimate the true classes of an image based on annotations from individual workers.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-ImageMultiClassMultiLabel`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-ImageMultiClassMultiLabel`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-ImageMultiClassMultiLabel`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-ImageMultiClassMultiLabel`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-ImageMultiClassMultiLabel`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-ImageMultiClassMultiLabel`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-ImageMultiClassMultiLabel`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-ImageMultiClassMultiLabel`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-ImageMultiClassMultiLabel`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-ImageMultiClassMultiLabel`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-ImageMultiClassMultiLabel`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-ImageMultiClassMultiLabel`

**Semantic segmentation** - Treats each pixel in an image as a multi-class classification and treats pixel annotations from workers as âvotesâ for the correct label.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-SemanticSegmentation`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-SemanticSegmentation`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-SemanticSegmentation`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-SemanticSegmentation`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-SemanticSegmentation`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-SemanticSegmentation`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-SemanticSegmentation`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-SemanticSegmentation`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-SemanticSegmentation`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-SemanticSegmentation`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-SemanticSegmentation`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-SemanticSegmentation`

**Text classification** - Uses a variant of the Expectation Maximization approach to estimate the true class of text based on annotations from individual workers.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-TextMultiClass`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-TextMultiClass`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-TextMultiClass`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-TextMultiClass`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-TextMultiClass`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-TextMultiClass`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-TextMultiClass`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-TextMultiClass`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-TextMultiClass`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-TextMultiClass`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-TextMultiClass`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-TextMultiClass`

**Multi-label text classification** - Uses a variant of the Expectation Maximization approach to estimate the true classes of text based on annotations from individual workers.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-TextMultiClassMultiLabel`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-TextMultiClassMultiLabel`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-TextMultiClassMultiLabel`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-TextMultiClassMultiLabel`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-TextMultiClassMultiLabel`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-TextMultiClassMultiLabel`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-TextMultiClassMultiLabel`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-TextMultiClassMultiLabel`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-TextMultiClassMultiLabel`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-TextMultiClassMultiLabel`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-TextMultiClassMultiLabel`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-TextMultiClassMultiLabel`

**Named entity recognition** - Groups similar selections and calculates aggregate boundaries, resolving to most-assigned label.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-NamedEntityRecognition`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-NamedEntityRecognition`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-NamedEntityRecognition`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-NamedEntityRecognition`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-NamedEntityRecognition`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-NamedEntityRecognition`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-NamedEntityRecognition`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-NamedEntityRecognition`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-NamedEntityRecognition`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-NamedEntityRecognition`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-NamedEntityRecognition`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-NamedEntityRecognition`

**Video Classification** - Use this task type when you need workers to classify videos using predefined labels that you specify. Workers are shown videos and are asked to choose one label for each video.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-VideoMultiClass`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-VideoMultiClass`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-VideoMultiClass`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-VideoMultiClass`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-VideoMultiClass`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-VideoMultiClass`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-VideoMultiClass`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-VideoMultiClass`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-VideoMultiClass`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-VideoMultiClass`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-VideoMultiClass`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-VideoMultiClass`

**Video Frame Object Detection** - Use this task type to have workers identify and locate objects in a sequence of video frames (images extracted from a video) using bounding boxes. For example, you can use this task to ask workers to identify and localize various objects in a series of video frames, such as cars, bikes, and pedestrians.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-VideoObjectDetection`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-VideoObjectDetection`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-VideoObjectDetection`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-VideoObjectDetection`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-VideoObjectDetection`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-VideoObjectDetection`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-VideoObjectDetection`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-VideoObjectDetection`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-VideoObjectDetection`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-VideoObjectDetection`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-VideoObjectDetection`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-VideoObjectDetection`

**Video Frame Object Tracking** - Use this task type to have workers track the movement of objects in a sequence of video frames (images extracted from a video) using bounding boxes. For example, you can use this task to ask workers to track the movement of objects, such as cars, bikes, and pedestrians.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-VideoObjectTracking`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-VideoObjectTracking`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-VideoObjectTracking`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-VideoObjectTracking`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-VideoObjectTracking`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-VideoObjectTracking`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-VideoObjectTracking`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-VideoObjectTracking`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-VideoObjectTracking`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-VideoObjectTracking`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-VideoObjectTracking`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-VideoObjectTracking`

**3D Point Cloud Object Detection** - Use this task type when you want workers to classify objects in a 3D point cloud by drawing 3D cuboids around objects. For example, you can use this task type to ask workers to identify different types of objects in a point cloud, such as cars, bikes, and pedestrians.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-3DPointCloudObjectDetection`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-3DPointCloudObjectDetection`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-3DPointCloudObjectDetection`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-3DPointCloudObjectDetection`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-3DPointCloudObjectDetection`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-3DPointCloudObjectDetection`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-3DPointCloudObjectDetection`

**3D Point Cloud Object Tracking** - Use this task type when you want workers to draw 3D cuboids around objects that appear in a sequence of 3D point cloud frames. For example, you can use this task type to ask workers to track the movement of vehicles across multiple point cloud frames.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-3DPointCloudObjectTracking`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-3DPointCloudObjectTracking`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-3DPointCloudObjectTracking`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-3DPointCloudObjectTracking`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-3DPointCloudObjectTracking`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-3DPointCloudObjectTracking`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-3DPointCloudObjectTracking`

**3D Point Cloud Semantic Segmentation** - Use this task type when you want workers to create a point-level semantic segmentation masks by painting objects in a 3D point cloud using different colors where each color is assigned to one of the classes you specify.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-3DPointCloudSemanticSegmentation`

**Use the following ARNs for Label Verification and Adjustment Jobs**

Use label verification and adjustment jobs to review and adjust labels. To learn more, see [Verify and Adjust Labels](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-verification-data.html) .

**Semantic Segmentation Adjustment** - Treats each pixel in an image as a multi-class classification and treats pixel adjusted annotations from workers as âvotesâ for the correct label.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-AdjustmentSemanticSegmentation`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-AdjustmentSemanticSegmentation`

**Semantic Segmentation Verification** - Uses a variant of the Expectation Maximization approach to estimate the true class of verification judgment for semantic segmentation labels based on annotations from individual workers.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-VerificationSemanticSegmentation`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-VerificationSemanticSegmentation`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-VerificationSemanticSegmentation`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-VerificationSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-VerificationSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-VerificationSemanticSegmentation`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-VerificationSemanticSegmentation`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-VerificationSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-VerificationSemanticSegmentation`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-VerificationSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-VerificationSemanticSegmentation`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-VerificationSemanticSegmentation`

**Bounding Box Adjustment** - Finds the most similar boxes from different workers based on the Jaccard index of the adjusted annotations.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-AdjustmentBoundingBox`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-AdjustmentBoundingBox`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-AdjustmentBoundingBox`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-AdjustmentBoundingBox`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-AdjustmentBoundingBox`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-AdjustmentBoundingBox`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-AdjustmentBoundingBox`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-AdjustmentBoundingBox`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-AdjustmentBoundingBox`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-AdjustmentBoundingBox`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-AdjustmentBoundingBox`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-AdjustmentBoundingBox`

**Bounding Box Verification** - Uses a variant of the Expectation Maximization approach to estimate the true class of verification judgement for bounding box labels based on annotations from individual workers.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-VerificationBoundingBox`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-VerificationBoundingBox`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-VerificationBoundingBox`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-VerificationBoundingBox`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-VerificationBoundingBox`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-VerificationBoundingBox`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-VerificationBoundingBox`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-VerificationBoundingBox`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-VerificationBoundingBox`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-VerificationBoundingBox`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-VerificationBoundingBox`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-VerificationBoundingBox`

**Video Frame Object Detection Adjustment** - Use this task type when you want workers to adjust bounding boxes that workers have added to video frames to classify and localize objects in a sequence of video frames.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-AdjustmentVideoObjectDetection`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-AdjustmentVideoObjectDetection`

**Video Frame Object Tracking Adjustment** - Use this task type when you want workers to adjust bounding boxes that workers have added to video frames to track object movement across a sequence of video frames.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-AdjustmentVideoObjectTracking`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-AdjustmentVideoObjectTracking`

**3D Point Cloud Object Detection Adjustment** - Use this task type when you want workers to adjust 3D cuboids around objects in a 3D point cloud.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-Adjustment3DPointCloudObjectDetection`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-Adjustment3DPointCloudObjectDetection`

**3D Point Cloud Object Tracking Adjustment** - Use this task type when you want workers to adjust 3D cuboids around objects that appear in a sequence of 3D point cloud frames.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-Adjustment3DPointCloudObjectTracking`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-Adjustment3DPointCloudObjectTracking`

**3D Point Cloud Semantic Segmentation Adjustment** - Use this task type when you want workers to adjust a point-level semantic segmentation masks using a paint tool.

- `arn:aws:lambda:us-east-1:432418664414:function:ACS-3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:us-east-1:432418664414:function:ACS-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:us-east-2:266458841044:function:ACS-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:us-west-2:081040173940:function:ACS-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:eu-west-1:568282634449:function:ACS-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-2:454466003867:function:ACS-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-south-1:565803892007:function:ACS-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:eu-central-1:203001061592:function:ACS-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-northeast-2:845288260483:function:ACS-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:eu-west-2:487402164563:function:ACS-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ap-southeast-1:377565633583:function:ACS-Adjustment3DPointCloudSemanticSegmentation`
- `arn:aws:lambda:ca-central-1:918755190332:function:ACS-Adjustment3DPointCloudSemanticSegmentation`

PublicWorkforceTaskPrice -> (structure)

The price that you pay for each task performed by an Amazon Mechanical Turk worker.

AmountInUsd -> (structure)

Defines the amount of money paid to an Amazon Mechanical Turk worker in United States dollars.

Dollars -> (integer)

The whole number of dollars in the amount.

Cents -> (integer)

The fractional portion, in cents, of the amount.

TenthFractionsOfACent -> (integer)

Fractions of a cent, in tenths.

Shorthand Syntax:

```
WorkteamArn=string,UiConfig={UiTemplateS3Uri=string,HumanTaskUiArn=string},PreHumanTaskLambdaArn=string,TaskKeywords=string,string,TaskTitle=string,TaskDescription=string,NumberOfHumanWorkersPerDataObject=integer,TaskTimeLimitInSeconds=integer,TaskAvailabilityLifetimeInSeconds=integer,MaxConcurrentTaskCount=integer,AnnotationConsolidationConfig={AnnotationConsolidationLambdaArn=string},PublicWorkforceTaskPrice={AmountInUsd={Dollars=integer,Cents=integer,TenthFractionsOfACent=integer}}
```

JSON Syntax:

```
{
  "WorkteamArn": "string",
  "UiConfig": {
    "UiTemplateS3Uri": "string",
    "HumanTaskUiArn": "string"
  },
  "PreHumanTaskLambdaArn": "string",
  "TaskKeywords": ["string", ...],
  "TaskTitle": "string",
  "TaskDescription": "string",
  "NumberOfHumanWorkersPerDataObject": integer,
  "TaskTimeLimitInSeconds": integer,
  "TaskAvailabilityLifetimeInSeconds": integer,
  "MaxConcurrentTaskCount": integer,
  "AnnotationConsolidationConfig": {
    "AnnotationConsolidationLambdaArn": "string"
  },
  "PublicWorkforceTaskPrice": {
    "AmountInUsd": {
      "Dollars": integer,
      "Cents": integer,
      "TenthFractionsOfACent": integer
    }
  }
}
```

`--tags` (list)

An array of key/value pairs. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what) in the *Amazon Web Services Billing and Cost Management User Guide* .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Output

LabelingJobArn -> (string)

The Amazon Resource Name (ARN) of the labeling job. You use this ARN to identify the labeling job.