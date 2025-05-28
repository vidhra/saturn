# gcloud alpha compute instances ops-agents policies delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/delete)*

**NAME**

: **gcloud alpha compute instances ops-agents policies delete - delete a Google Cloud's operations suite agents (Ops Agents) policy**

**SYNOPSIS**

: **`gcloud alpha compute instances ops-agents policies delete` `[POLICY_ID](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/delete#POLICY_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instances ops-agents policies
delete` deletes a policy that facilitates agent management across Compute
Engine instances based on user specified instance filters. This policy installs,
specifies versioning, enables autoupgrade, and removes Ops Agents.
The command returns a response indicating whether the deletion succeeded. After
a policy is deleted, it takes 10-15 minutes to be wiped from the applicable
instances. Deleting a policy does not delete any existing agents managed by that
policy, but the agents become unmanaged by any policies. To remove the agents
from the instances, first update the policy to set the agent
``package-state`` to
``removed``, wait for the policy to take
effect, then delete the policy.

**EXAMPLES**

: To delete an Ops agents policy named
``ops-agents-test-policy`` in the current
project, run:

```
gcloud alpha compute instances ops-agents policies delete ops-agents-test-policy
```

**POSITIONAL ARGUMENTS**

: **`POLICY_ID`**:
ID of the policy.
This ID must start with ``ops-agents-``,
contain only lowercase letters, numbers, and hyphens, end with a number or a
letter, be between 1-63 characters, and be unique within the project. The goal
of the prefix ``ops-agents-`` is to easily
distinguish these Ops Agents specific policies from other generic policies and
lower the chance of naming conflicts.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instances ops-agents policies delete
```

```
gcloud beta compute instances ops-agents policies delete
```