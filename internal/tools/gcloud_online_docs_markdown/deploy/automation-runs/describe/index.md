# gcloud deploy automation-runs describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/automation-runs/describe](https://cloud.google.com/sdk/gcloud/reference/deploy/automation-runs/describe)*

**NAME**

: **gcloud deploy automation-runs describe - show details for an Automation Run**

**SYNOPSIS**

: **`gcloud deploy automation-runs describe` (`[AUTOMATION_RUN](https://cloud.google.com/sdk/gcloud/reference/deploy/automation-runs/describe#AUTOMATION_RUN)` : `[--delivery-pipeline](https://cloud.google.com/sdk/gcloud/reference/deploy/automation-runs/describe#--delivery-pipeline)`=`DELIVERY_PIPELINE` `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/automation-runs/describe#--region)`=`REGION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/automation-runs/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Show details for a specified automation run.

**EXAMPLES**

: To show details about a automation run 'test-automationrun', for delivery
pipeline 'test-pipeline', in region 'us-central1', run:

```
gcloud deploy automation-runs describe test-automationrun --delivery-pipeline=test-pipeline --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Automation run resource - The name of the automation run you want to describe.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `automation_run` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`AUTOMATION_RUN`**:
ID of the automation run or fully qualified identifier for the automation run.
To set the `automation_run` attribute:

- provide the argument `automation_run` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--delivery-pipeline**:
The name of the Cloud Deploy delivery pipeline.
To set the `delivery-pipeline` attribute:

- provide the argument `automation_run` on the command line with a
fully specified name;
- provide the argument `--delivery-pipeline` on the command line;
- set the property `deploy/delivery_pipeline`.

**--region**:
Location of the automation run.
To set the `region` attribute:

- provide the argument `automation_run` on the command line with a
fully specified name;
- provide the argument `--region` on the command line;
- set the property `deploy/region`.**

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
gcloud alpha deploy automation-runs describe
```

```
gcloud beta deploy automation-runs describe
```