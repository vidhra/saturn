# gcloud compute instances ops-agents policies update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/update](https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/update)*

**NAME**

: **gcloud compute instances ops-agents policies update - update a Google Cloud Observability agents policy for the Ops Agent**

**SYNOPSIS**

: **`gcloud compute instances ops-agents policies update` `[POLICY_ID](https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/update#POLICY_ID)` `[--file](https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/update#--file)`=`FILE` `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/update#--zone)`=`ZONE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instances ops-agents policies update` modifies a
policy that facilitates agent management across Compute Engine instances based
on user specified instance filters. This policy installs, specifies versioning,
and removes Ops Agents.
The command returns the content of the modified policy or an error indicating
why the modification fails. The modified policy takes effect asynchronously. It
can take 10-15 minutes for the VMs to enforce the newly modified policy.

**EXAMPLES**

: To update a Google Cloud Observability agents policy, run:
```
gcloud compute instances ops-agents policies update agent-policy --project=PROJECT --zone=ZONE --file=config.yaml
```

**POSITIONAL ARGUMENTS**

: **`POLICY_ID`**:
ID of the policy.
This ID must contain only lowercase letters, numbers, and hyphens, end with a
number or a letter, be between 1-63 characters, and be unique within the
project.

**REQUIRED FLAGS**

: **--file**:
YAML file with a subset of agents policy fields you wish to update. For
information about the agents policy format, see [https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/agent-policies#config-files](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/agent-policies#config-files).

**--zone**:
Zone where the agents policy is located.

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
gcloud alpha compute instances ops-agents policies update
```

```
gcloud beta compute instances ops-agents policies update
```