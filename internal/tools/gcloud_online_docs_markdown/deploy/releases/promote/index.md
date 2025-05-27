# gcloud deploy releases promote  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/releases/promote](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/promote)*

**NAME**

: **gcloud deploy releases promote - promotes a release from one target (source), to another (destination)**

**SYNOPSIS**

: **`gcloud deploy releases promote` (`[--release](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/promote#--release)`=`RELEASE` : `[--delivery-pipeline](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/promote#--delivery-pipeline)`=`DELIVERY_PIPELINE` `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/promote#--region)`=`REGION`) [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/promote#--annotations)`=[`KEY`=`VALUE`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/promote#--labels)`=[`KEY`=`VALUE`,…]] [`[--override-deploy-policies](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/promote#--override-deploy-policies)`=[`POLICY`,…]] [`[--rollout-id](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/promote#--rollout-id)`=`ROLLOUT_ID`] [`[--starting-phase-id](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/promote#--starting-phase-id)`=`STARTING_PHASE_ID`] [`[--to-target](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/promote#--to-target)`=`TO_TARGET`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/promote#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: If to-target is not specified the command promotes the release from the target
that is farthest along in the promotion sequence to its next stage in the
promotion sequence.

**EXAMPLES**

: To promote a release called 'test-release' for delivery pipeline 'test-pipeline'
in region 'us-central1' to target 'prod', run:

```
gcloud deploy releases promote --release=test-release --delivery-pipeline=test-pipeline --region=us-central1 --to-target=prod
```

**REQUIRED FLAGS**

: **Release resource - The name of the Release. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--release` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--release**:
ID of the release or fully qualified identifier for the release.
To set the `release` attribute:

- provide the argument `--release` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--delivery-pipeline**:
The delivery pipeline associated with the release. Alternatively, set the
property [deploy/delivery-pipeline].
To set the `delivery-pipeline` attribute:

- provide the argument `--release` on the command line with a fully
specified name;
- provide the argument `--delivery-pipeline` on the command line;
- set the property `deploy/delivery_pipeline`.

**--region**:
The Cloud region for the release. Alternatively, set the property
[deploy/region].
To set the `region` attribute:

- provide the argument `--release` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `deploy/region`.**

**OPTIONAL FLAGS**

: **--annotations**:
Annotations to apply to the rollout. Annotations take the form of key/value
string pairs.
Examples:
Add annotations:

```
gcloud deploy releases promote --annotations="from_target=test,status=stable"
```

**--labels**:
Labels to apply to the rollout. Labels take the form of key/value string pairs.
Examples:
Add labels:

```
gcloud deploy releases promote --labels="commit=abc123,author=foo"
```

**--override-deploy-policies**:
Deploy policies to override

**--rollout-id**:
ID to assign to the generated rollout for promotion.

**--starting-phase-id**:
If set, starts the created rollout at the specified phase.
Start rollout at `stable` phase:

```
gcloud deploy releases promote --starting-phase-id=stable
```

**--to-target**:
Destination target to promote into.

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
gcloud alpha deploy releases promote
```

```
gcloud beta deploy releases promote
```