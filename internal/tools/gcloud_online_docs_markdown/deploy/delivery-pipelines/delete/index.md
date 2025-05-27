# gcloud deploy delivery-pipelines delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/delete](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/delete)*

**NAME**

: **gcloud deploy delivery-pipelines delete - delete a delivery pipeline**

**SYNOPSIS**

: **`gcloud deploy delivery-pipelines delete` [[`[DELIVERY_PIPELINE](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/delete#DELIVERY_PIPELINE)`] `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/delete#--region)`=`REGION`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/delete#--async)`] [`[--force](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/delete#--force)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a delivery pipeline.

**EXAMPLES**

: The following command will delete delivery pipeline 'test-pipeline', in region
'us-central1', but only if the delivery pipeline doesn't have any sub-resources
(targets, releases or rollouts):

```
gcloud deploy delivery-pipelines delete test-pipeline --region=us-central1
```

The following command will delete delivery pipeline 'test-pipeline', in region
'us-central1' and its sub-resources (targets, releases or rollouts):

```
gcloud deploy delivery-pipelines delete test-pipeline --region=us-central1 --force
```

**POSITIONAL ARGUMENTS**

: **Delivery pipeline resource - The Cloud Deploy delivery pipeline to delete. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
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
To set the `delivery_pipeline` attribute:

- provide the argument `delivery_pipeline` on the command line;
- set the property `deploy/delivery_pipeline`.

**--region**:
Location of the delivery_pipeline.
To set the `region` attribute:

- provide the argument `delivery_pipeline` on the command line with a
fully specified name;
- set the property `deploy/delivery_pipeline` with a fully specified
name;
- provide the argument `--region` on the command line;
- set the property `deploy/region`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--force**:
If true, the delivery pipeline with sub-resources will be deleted and its
sub-resources will also be deleted.

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

**API REFERENCE**

: This command uses the `clouddeploy/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/deploy/](https://cloud.google.com/deploy/)

**NOTES**

: These variants are also available:

```
gcloud alpha deploy delivery-pipelines delete
```

```
gcloud beta deploy delivery-pipelines delete
```