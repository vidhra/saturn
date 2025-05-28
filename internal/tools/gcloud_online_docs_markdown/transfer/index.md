# gcloud transfer  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer](https://cloud.google.com/sdk/gcloud/reference/transfer)*

**NAME**

: **gcloud transfer - manage Transfer Service jobs, operations, and agents**

**SYNOPSIS**

: **`gcloud transfer` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/transfer#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/transfer#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud transfer command group lets you create and manage Transfer Service
jobs, operations, and agents.
To get started, run: `gcloud transfer jobs create --help`
More info on prerequisite IAM permissions: [https://cloud.google.com/storage-transfer/docs/on-prem-set-up](https://cloud.google.com/storage-transfer/docs/on-prem-set-up)

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[agent-pools](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools)`**:
Manage on-premise transfer agent pools.

**`[agents](https://cloud.google.com/sdk/gcloud/reference/transfer/agents)`**:
Manage Transfer Service agents.

**`[jobs](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs)`**:
Manage transfer jobs.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/transfer/operations)`**:
Manage transfer operations.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[authorize](https://cloud.google.com/sdk/gcloud/reference/transfer/authorize)`**:
Authorize an account for all Transfer Service features.

**NOTES**

: This variant is also available:

```
gcloud alpha transfer
```