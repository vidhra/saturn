# gcloud deploy releases abandon  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/releases/abandon](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/abandon)*

**NAME**

: **gcloud deploy releases abandon - abandons a release**

**SYNOPSIS**

: **`gcloud deploy releases abandon` (`[RELEASE](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/abandon#RELEASE)` : `[--delivery-pipeline](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/abandon#--delivery-pipeline)`=`DELIVERY_PIPELINE` `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/abandon#--region)`=`REGION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/abandon#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: After a release is abandoned, no new rollouts can be created from it.
Rollouts of abandoned releases can't be rolled back to.
Existing rollouts of abandoned releases will be unaffected.

**EXAMPLES**

: To abandon a release called `test-release` for delivery pipeline
`test-pipeline` in region `us-central1`, run:

```
gcloud deploy releases abandon test-release --delivery-pipeline=test-pipeline --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Release resource - The name of the Release. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `release` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`RELEASE`**:
ID of the release or fully qualified identifier for the release.
To set the `release` attribute:

- provide the argument `release` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--delivery-pipeline**:
The delivery pipeline associated with the release. Alternatively, set the
property [deploy/delivery-pipeline].
To set the `delivery-pipeline` attribute:

- provide the argument `release` on the command line with a fully
specified name;
- provide the argument `--delivery-pipeline` on the command line;
- set the property `deploy/delivery_pipeline`.

**--region**:
The Cloud region for the release. Alternatively, set the property
[deploy/region].
To set the `region` attribute:

- provide the argument `release` on the command line with a fully
specified name;
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
gcloud alpha deploy releases abandon
```

```
gcloud beta deploy releases abandon
```