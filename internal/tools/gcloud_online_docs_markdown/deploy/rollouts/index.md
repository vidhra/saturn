# gcloud deploy rollouts  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts)*

**NAME**

: **gcloud deploy rollouts - create and manage Rollout resources for Cloud Deploy**

**SYNOPSIS**

: **`gcloud deploy rollouts` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create and manage Rollout resources for Cloud Deploy.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[advance](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/advance)`**:
Advances a rollout.

**`[approve](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/approve)`**:
Approves a rollout having an Approval state of "Required".

**`[cancel](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/cancel)`**:
Cancel a Rollout.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/describe)`**:
Show details for a rollout.

**`[ignore-job](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/ignore-job)`**:
Ignores a specified job and phase combination on a rollout.

**`[list](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/list)`**:
List the rollouts.

**`[reject](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/reject)`**:
Rejects a rollout having an Approval state of "Required".

**`[retry-job](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/retry-job)`**:
Retries a specified job, phase combination on a rollout.

**NOTES**

: These variants are also available:

```
gcloud alpha deploy rollouts
```

```
gcloud beta deploy rollouts
```