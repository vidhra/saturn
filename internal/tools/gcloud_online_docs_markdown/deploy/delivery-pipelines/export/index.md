# gcloud deploy delivery-pipelines export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/export](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/export)*

**NAME**

: **gcloud deploy delivery-pipelines export - returns the .yaml definition of the specified delivery pipeline**

**SYNOPSIS**

: **`gcloud deploy delivery-pipelines export` [[`[DELIVERY_PIPELINE](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/export#DELIVERY_PIPELINE)`] `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/export#--region)`=`REGION`] [`[--destination](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/export#--destination)`=`DESTINATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The exported yaml definition can be applied by 'deploy apply' command.

**EXAMPLES**

: To return the .yaml definition of the delivery pipeline 'test-pipeline', in
region 'us-central1', run:

```
gcloud deploy delivery-pipelines export test-pipeline --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Delivery pipeline resource - The name of the Delivery Pipeline. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `delivery_pipeline` on the command line with a
fully specified name;
- set the property `deploy/delivery_pipeline` with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**[`DELIVERY_PIPELINE`]**:
ID of the delivery_pipeline or fully qualified identifier for the
delivery_pipeline.
To set the `delivery-pipeline` attribute:

- provide the argument `delivery_pipeline` on the command line;
- set the property `deploy/delivery_pipeline`.

**--region**:
The Cloud region for the delivery_pipeline. Alternatively, set the property
[deploy/region].
To set the `region` attribute:

- provide the argument `delivery_pipeline` on the command line with a
fully specified name;
- set the property `deploy/delivery_pipeline` with a fully specified
name;
- provide the argument `--region` on the command line;
- set the property `deploy/region`.**

**FLAGS**

: **--destination**:
Path to a YAML file where the configuration will be exported. Alternatively, you
may omit this flag to write to standard output.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: These variants are also available:

```
gcloud alpha deploy delivery-pipelines export
```

```
gcloud beta deploy delivery-pipelines export
```