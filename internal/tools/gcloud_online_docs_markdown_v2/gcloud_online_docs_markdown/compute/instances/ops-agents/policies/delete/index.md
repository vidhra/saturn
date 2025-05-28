# gcloud compute instances ops-agents policies delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/delete](https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/delete)*

**NAME**

: **gcloud compute instances ops-agents policies delete - delete a Google Cloud Observability agents policy for the Ops Agent**

**SYNOPSIS**

: **`gcloud compute instances ops-agents policies delete` `[POLICY_ID](https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/delete#POLICY_ID)` `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/delete#--zone)`=`ZONE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instances ops-agents policies delete` deletes a
policy that facilitates agent management across Compute Engine instances based
on user specified instance filters.
The command returns a response indicating whether the deletion succeeded. After
a policy is deleted, it takes 10-15 minutes to be wiped from the applicable
instances. Deleting a policy does not delete any existing agents managed by that
policy, but the agents become unmanaged by any policies. To remove the agents
from the instances, first update the policy to set the agent
``packageState`` to
``removed``, wait for the policy to take
effect, then delete the policy.
The command returns the content of the deleted policy. For instance:

```
agentsRule:
  packageState: installed
  version: latest
instanceFilter:
  inclusionLabels:
  - labels:
      env: prod
```

If no policies are found, or the policy is not an agents policy, then the
command returns a ``NOT_FOUND`` error.

**EXAMPLES**

: To delete an agents policy named
``ops-agents-test-policy`` in the current
project, run:

```
gcloud compute instances ops-agents policies delete ops-agents-test-policy --zone=ZONE
```

**POSITIONAL ARGUMENTS**

: **`POLICY_ID`**:
ID of the policy.
This ID must contain only lowercase letters, numbers, and hyphens, end with a
number or a letter, be between 1-63 characters, and be unique within the
project.

**REQUIRED FLAGS**

: **--zone**:
Zone of the agents policy you want to delete.

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
gcloud alpha compute instances ops-agents policies delete
```

```
gcloud beta compute instances ops-agents policies delete
```