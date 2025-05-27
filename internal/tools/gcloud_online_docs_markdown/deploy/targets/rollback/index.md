# gcloud deploy targets rollback  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/targets/rollback](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/rollback)*

**NAME**

: **gcloud deploy targets rollback - rollbacks a target to a prior rollout**

**SYNOPSIS**

: **`gcloud deploy targets rollback` (`[TARGET](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/rollback#TARGET)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/rollback#--region)`=`REGION`) `[--delivery-pipeline](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/rollback#--delivery-pipeline)`=`DELIVERY_PIPELINE` [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/rollback#--annotations)`=[`KEY`=`VALUE`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/rollback#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/rollback#--labels)`=[`KEY`=`VALUE`,…]] [`[--override-deploy-policies](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/rollback#--override-deploy-policies)`=[`POLICY`,…]] [`[--release](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/rollback#--release)`=`RELEASE`] [`[--rollout-id](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/rollback#--rollout-id)`=`ROLLOUT_ID`] [`[--starting-phase-id](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/rollback#--starting-phase-id)`=`STARTING_PHASE_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/targets/rollback#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: If release is not specified, the command rollbacks the target with the last
successful deployed release. If optional rollout-id parameter is not specified,
a generated rollout ID will be used.

**EXAMPLES**

: To rollback a target 'prod' for delivery pipeline 'test-pipeline' in region
'us-central1', run:

```
gcloud deploy targets rollback prod --delivery-pipeline=test-pipeline --region=us-central1
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

**REQUIRED FLAGS**

: **--delivery-pipeline**:
The name of the Cloud Deploy delivery pipeline

**OPTIONAL FLAGS**

: **--annotations**:
Annotations to apply to the rollback. Annotations take the form of key/value
string pairs.
Examples:
Add annotations:

```
gcloud deploy targets rollback --annotations="from_target=test,status=stable"
```

**--description**:
Description of rollout created during a rollback.

**--labels**:
Labels to apply to the rollback. Labels take the form of key/value string pairs.
Examples:
Add labels:

```
gcloud deploy targets rollback --labels="commit=abc123,author=foo"
```

**--override-deploy-policies**:
Deploy policies to override

**--release**:
Name of the release to rollback to.

**--rollout-id**:
ID to assign to the generated rollout for promotion.

**--starting-phase-id**:
If set, starts the created rollout at the specified phase.
Start rollout at `stable` phase:

```
gcloud deploy targets rollback --starting-phase-id=stable
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
gcloud alpha deploy targets rollback
```

```
gcloud beta deploy targets rollback
```