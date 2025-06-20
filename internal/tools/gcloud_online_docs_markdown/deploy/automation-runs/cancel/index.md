# gcloud deploy automation-runs cancel  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/automation-runs/cancel](https://cloud.google.com/sdk/gcloud/reference/deploy/automation-runs/cancel)*

**NAME**

: **gcloud deploy automation-runs cancel - cancels a Cloud Deploy Automation Run**

**SYNOPSIS**

: **`gcloud deploy automation-runs cancel` (`[AUTOMATION_RUN](https://cloud.google.com/sdk/gcloud/reference/deploy/automation-runs/cancel#AUTOMATION_RUN)` : `[--delivery-pipeline](https://cloud.google.com/sdk/gcloud/reference/deploy/automation-runs/cancel#--delivery-pipeline)`=`DELIVERY_PIPELINE` `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/automation-runs/cancel#--region)`=`REGION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/automation-runs/cancel#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Cancels a Cloud Deploy Automation Run.

**EXAMPLES**

: To cancel an AutomationRun `test-run` for delivery pipeline
`test-pipeline` in region `us-central1`, run:

```
gcloud deploy automation-runs cancel test-run --delivery-pipeline=test-pipeline --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Automation run resource - The name of the AutomationRun. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `automation_run` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`AUTOMATION_RUN`**:
ID of the automation_run or fully qualified identifier for the automation_run.
To set the `name` attribute:

- provide the argument `automation_run` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--delivery-pipeline**:
The delivery pipeline associated with the automation_run. Alternatively, set the
property [deploy/delivery-pipeline].
To set the `delivery-pipeline` attribute:

- provide the argument `automation_run` on the command line with a
fully specified name;
- provide the argument `--delivery-pipeline` on the command line;
- set the property `deploy/delivery_pipeline`.

**--region**:
The Cloud region for the automation_run. Alternatively, set the property
[deploy/region].
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

**NOTES**

: These variants are also available:

```
gcloud alpha deploy automation-runs cancel
```

```
gcloud beta deploy automation-runs cancel
```