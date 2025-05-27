# gcloud deploy rollouts describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/describe](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/describe)*

**NAME**

: **gcloud deploy rollouts describe - show details for a rollout**

**SYNOPSIS**

: **`gcloud deploy rollouts describe` (`[ROLLOUT](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/describe#ROLLOUT)` : `[--delivery-pipeline](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/describe#--delivery-pipeline)`=`DELIVERY_PIPELINE` `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/describe#--region)`=`REGION` `[--release](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/describe#--release)`=`RELEASE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Show details for a specified rollout.

**EXAMPLES**

: To show details about a rollout 'test-rollout', for delivery pipeline
'test-pipeline', and release 'test-release' in region 'us-central1', run:

```
gcloud deploy rollouts describe test-rollout --delivery-pipeline=test-pipeline --release=test-release --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Rollout resource - The name of the rollout you want to describe. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `rollout` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ROLLOUT`**:
ID of the rollout or fully qualified identifier for the rollout.
To set the `rollout` attribute:

- provide the argument `rollout` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--delivery-pipeline**:
The name of the Cloud Deploy delivery pipeline.
To set the `delivery-pipeline` attribute:

- provide the argument `rollout` on the command line with a fully
specified name;
- provide the argument `--delivery-pipeline` on the command line;
- set the property `deploy/delivery_pipeline`.

**--region**:
Location of the rollout.
To set the `region` attribute:

- provide the argument `rollout` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `deploy/region`.

**--release**:
The name of the Cloud Deploy release.
To set the `release` attribute:

- provide the argument `rollout` on the command line with a fully
specified name;
- provide the argument `--release` on the command line.**

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
gcloud alpha deploy rollouts describe
```

```
gcloud beta deploy rollouts describe
```