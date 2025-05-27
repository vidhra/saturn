# gcloud deploy targets describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/targets/describe](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/describe)*

**NAME**

: **gcloud deploy targets describe - describes details specific to the individual target, delivery pipeline qualified**

**SYNOPSIS**

: **`gcloud deploy targets describe` (`[TARGET](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/describe#TARGET)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/describe#--region)`=`REGION`) [`[--delivery-pipeline](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/describe#--delivery-pipeline)`=`DELIVERY_PIPELINE`] [`[--list-all-pipelines](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/describe#--list-all-pipelines)`] [`[--skip-pipeline-lookup](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/describe#--skip-pipeline-lookup)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The output contains four sections:
Target:

```
detail of the target to be described.
```

Latest Release:

```
the detail of the active release in the target.
```

Latest Rollout:

```
the detail of the active rollout in the target.
```

Deployed:

```
timestamp of the last successful deployment.
```

Pending Approvals:

```
list of the rollouts that require approval.
```

**EXAMPLES**

: To describe a target called 'test' for delivery pipeline 'test-pipeline' in
region 'us-central1', run:

```
gcloud deploy targets describe test --delivery-pipeline=test-pipeline --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Target resource - The name of the Target. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `target` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TARGET`**:
ID of the target or fully qualified identifier for the target.
To set the `target` attribute:

- provide the argument `target` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Cloud region for the target. Alternatively, set the property
[deploy/region].
To set the `region` attribute:

- provide the argument `target` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `deploy/region`.**

**FLAGS**

: **--delivery-pipeline**:
The name of the Cloud Deploy delivery pipeline

**--list-all-pipelines**:
List all Delivery Pipelines associated with a target.
Usage:

```
gcloud deploy targets describe --list-all-pipelines
```

**--skip-pipeline-lookup**:
If set, skip fetching details of associated pipelines when describing a target.
Usage:

```
gcloud deploy targets describe --skip-pipeline-lookup
```

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
gcloud alpha deploy targets describe
```

```
gcloud beta deploy targets describe
```