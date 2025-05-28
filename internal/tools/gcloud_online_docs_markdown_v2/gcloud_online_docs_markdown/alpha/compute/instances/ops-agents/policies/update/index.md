# gcloud alpha compute instances ops-agents policies update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update)*

**NAME**

: **gcloud alpha compute instances ops-agents policies update - update a Google Cloud operations suite agent (Ops Agent) policy**

**SYNOPSIS**

: **`gcloud alpha compute instances ops-agents policies update` `[POLICY_ID](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update#POLICY_ID)` [`[--agent-rules](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update#--agent-rules)`=`type`=`TYPE`,`version`=`VERSION`,`package-state`=`PACKAGE-STATE`,`enable-autoupgrade`=`ENABLE-AUTOUPGRADE`;[…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update#--description)`=`DESCRIPTION`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update#--etag)`=`ETAG`] [`[--os-types](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update#--os-types)`=`short-name`=`SHORT-NAME`,`version`=`VERSION`;[…]] [`[--clear-group-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update#--clear-group-labels)`     | `[--group-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update#--group-labels)`=[`LABEL_NAME`=`LABEL_VALUE`,`[LABEL_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update#LABEL_NAME)`=`LABEL_VALUE`,…;…]] [`[--clear-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update#--clear-instances)`     | `[--instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update#--instances)`=[`zones`/`[ZONE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update#ZONE_NAME)`/`instances`/`[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update#INSTANCE_NAME)`,…]] [`[--clear-zones](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update#--clear-zones)`     | `[--zones](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update#--zones)`=[`ZONE_NAME`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/ops-agents/policies/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instances ops-agents policies
update` updates a policy that facilitates agent management across Compute
Engine instances based on user specified instance filters. This policy installs,
specifies versioning, enables autoupgrade, and removes Ops Agents.
The command returns the content of the updated policy or an error indicating why
the update fails. The updated policy takes effect asynchronously. It can take
10-15 minutes for the VMs to enforce the updated policy.
The available flags for the ``update`` command
are similar to the flags for the ``create``
command. All the flags for ``update`` are
optional. If a flag is not specified, it retains the original value. The full
value of each flag needs to be re-stated during
``update``. Take the
``--agents`` flag for example:
If the original policy specified two agents
(``--agents="type=logging;type=metrics"``), and
only one agent (``--agents="type=logging"``) is
specified in a `gcloud alpha compute instances ops-agents policies
update` command, then the policy stops managing and enforcing the
unspecified agent. In order to remove the metrics agent in this case, set the
package state explicitly to ``removed``
(``--agents="type=logging;type=metrics,package-state=removed"``).
In order to explicitly clear the
``--group-labels``,
``--instances``, and
``--zones`` instance filters, use the following
flags as documented below:
``--clear-group-labels``,
``--clear-instances``, and
``--clear-zones`` flags.

**EXAMPLES**

: To update a policy named
``ops-agents-test-policy`` to target a single
CentOS 7 VM instance named
``zones/us-central1-a/instances/test-instance``
for testing or development, and install both Logging and Monitoring Agents on
that VM instance, run:

```
gcloud alpha compute instances ops-agents policies update ops-agents-test-policy --agent-rules="type=logging,enable-autoupgrade=false;type=metrics,enable-autoupgrade=false" --instances=zones/us-central1-a/instances/test-instance --os-types=short-name=centos,version=7
```

To update a policy named
``ops-agents-prod-policy`` to target all CentOS
7 VMs in zone ``us-central1-a`` with either
``env=prod,product=myapp`` labels or
``env=staging,product=myapp`` labels, and make
sure the logging agent and metrics agent versions are pinned to specific major
versions for staging and production, run:

```
gcloud alpha compute instances ops-agents policies update ops-agents-prod-policy --agent-rules="type=logging,version=1.*.*,enable-autoupgrade=false;type=metrics,version=6.*.*,enable-autoupgrade=false" --group-labels="env=prod,product=myapp;env=staging,product=myapp" --os-types=short-name=centos,version=7 --zones=us-central1-a
```

To update a policy named
``ops-agents-labels-policy`` to clear the
instances filters and use a group labels filter instead to target VMs with
either ``env=prod,product=myapp`` or
``env=staging,product=myapp`` labels, run:

```
gcloud alpha compute instances ops-agents policies update ops-agents-labels-policy --clear-instances --group-labels="env=prod,product=myapp;env=staging,product=myapp"
```

To perform the same update as above, conditionally on the fact that the policy's
etag (retrieved by an earlier command) is
``f59741c8-bb5e-4ee6-bf6f-c4ebeb6b06e0``, run:

```
gcloud alpha compute instances ops-agents policies update ops-agents-labels-policy --clear-instances --group-labels="env=prod,product=myapp;env=staging,product=myapp" --etag=f59741c8-bb5e-4ee6-bf6f-c4ebeb6b06e0
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

**FLAGS**

: **--agent-rules**:
A non-empty list of agent rules to be enforced by the policy.
This flag must be quoted. Items in the list are separated by ";". Each item in
the list is a <key, value> map that represents a logging or metrics agent.
The allowed values of the key are as follows.

**`type`**:
Type of agent to manage.
`Required`. Allowed values:
``logging``,
``metrics`` and
``ops-agent``. Use
``logging`` for the Logging Agent
(https://cloud.google.com/logging/docs/agent). Use
``metrics`` for the Monitoring Agent
(https://cloud.google.com/monitoring/agent). Use
``ops-agent`` for the Ops Agent
(https://cloud.google.com/stackdriver/docs/solutions/ops-agent). The Ops Agent
has both a logging module and a metrics module already. So other types of agents
are not allowed when there is an agent with type
``ops-agent``. See [https://cloud.google.com/stackdriver/docs/solutions/agents#which-agent-should-you-choose](https://cloud.google.com/stackdriver/docs/solutions/agents#which-agent-should-you-choose)
for which agent to use.

**`enable-autoupgrade`**:
Whether to enable autoupgrade of the agent.
`Required`. Allowed values: ``true``
or ``false``. This has to be
``false`` if the agent version is set to a
specific patch version in the format of
``version=MAJOR_VERSION.MINOR_VERSION.PATCH_VERSION``.

**`version`**:
Version of the agent to install.
Optional. Default to ``version=current-major``.
The allowed values and formats are as follows.

**`version=latest`**:
With this setting, the latest version of the agent is installed at the time when
the policy is applied to an instance.
If multiple instances are created at different times but they all fall into the
instance filter rules of an existing policy, they may end up with different
versions of the agent, depending on what the latest version of the agent is at
the policy application time (in this case the instance creation time). One way
to avoid this is to set
``enable-autoupgrade=true``. This guarantees
that the installed agents on all instances that are managed by this policy are
always up to date and conform to the same version.
While this ``version=latest`` setting makes it
easier to keep the agent version up to date, this setting does come with a
potential risk. When a new major version is released, the policy may install the
latest version of the agent from that new major release, which may introduce
breaking changes. For production environments, consider using the
`version=MAJOR_VERSION.*.*` setting below for safer agent
deployments.

**`version=MAJOR_VERSION.*.*`**:
With this setting, the latest version of agent from a specific major version is
installed at the time when the policy is applied to an instance.
If multiple instances are created at different times but they all fall into the
instance filter rules of an existing policy, they may end up with different
versions of the agent, depending on what the latest version of the agent is at
the policy application time (in this case the instance creation time). One way
to avoid this is to set
``enable-autoupgrade=true``. This guarantees
that the installed agents on all instances that are managed by this policy are
always up to date within that major version and conform to the same version.
When a new major release is out, this setting ensures that only the latest
version from the specified major version is installed, which avoids accidentally
introducing breaking changes. This is recommended for production environments to
ensure safer agent deployments.

**`version=current-major`**:
With this setting, the version field is automatically set to
`version=MAJOR_VERSION.*.*`, where
``MAJOR_VERSION`` is the current latest major
version released. Refer to the `version=MAJOR_VERSION.*.*` section
for the expected behavior.

**`version=MAJOR_VERSION.MINOR_VERSION.PATCH_VERSION`**:
With this setting, the specified exact version of agent is installed at the time
when the policy is applied to an instance.
``enable-autoupgrade`` must be false for this
setting.
This setting is not recommended since it prevents the policy from installing new
versions of the agent that include bug fixes and other improvements.
One limitation of this setting is that if the agent gets manually uninstalled
from the instances after the policy gets applied, the policy can only ensure
that the agent is re-installed. It is not able to restore the expected exact
version of the agent.

**`version=5.5.2-BUILD_NUMBER`**:
Allowed for the metrics agent
(``type=metrics``) only.
With this setting, the specified exact build number of the deprecated 5.5.2
metrics agent is installed at the time when the policy is applied to an
instance. enable-autoupgrade must be false for this setting.
This setting is deprecated and will be decommissioned along with the 5.5.2
metrics agent on Apr 28, 2021
(https://cloud.google.com/stackdriver/docs/deprecations/mon-agent). It is not
recommended since it prevents the policy from installing new versions of the
agent that include bug fixes and other improvements.
One limitation of this setting is that if the agent gets manually uninstalled
from the instances after the policy gets applied, the policy can only ensure
that the agent is re-installed. It is not able to restore the expected exact
version of the agent.

**`package-state`**:
Desired package state of the agent.
Optional. Default to
``package-state=installed``. The allowed values
are as follows.

**`package-state=installed`**:
With this setting, the policy will ensure the agent package is installed on the
instances and the agent service is running.

**`package-state=removed`**:
With this setting, the policy will ensure the agent package is removed from the
instances, which stops the service from running.

**--description**:
Description of the policy.

**--etag**:
Etag of the policy.
``etag`` is used for optimistic concurrency
control as a way to help prevent simultaneous updates of a policy from
overwriting each other. It is strongly suggested that systems make use of the
``etag`` in the read-modify-write cycle to
perform policy updates in order to avoid race conditions: an
``etag`` is returned in the response of a
``describe`` command, and systems are expected
to put that ``etag`` in the request to an
``update`` command to ensure that their change
will be applied to the same version of the policy.

**--os-types**:
A non-empty list of OS types to filter instances that the policy applies to.
For Alpha and Beta, exactly one OS type needs to be specified. The support for
multiple OS types will be added later for more flexibility. Each OS type is
defined by the combination of ``short-name``
and ``version`` fields.
Sample values:

```
OS Short Name      OS Version
centos             8
centos             7
debian             12
debian             11
debian             10
debian             9
rhel               9.*
rhel               8.*
rhel               7.*
rocky              9.*
rocky              8.*
sles               12.*
sles               15.*
sles_sap           12.*
sles_sap           15.*
ubuntu             16.04
ubuntu             18.04
ubuntu             19.10
ubuntu             20.04
ubuntu             21.04
ubuntu             21.10
ubuntu             22.04
ubuntu             23.04
ubuntu             23.10
ubuntu             24.04
ubuntu             24.10
windows            10.*
windows            6.*
```

**`short-name`**:
Short name of the OS.
`Required`. Allowed values:
``centos``,
``debian``,
``rhel``,
``rocky``,
``sles``,
``sles_sap``,
``ubuntu``.
To inspect the exact OS short name of an instance, run:

```
gcloud beta compute instances os-inventory describe INSTANCE_NAME | grep "^ShortName: "
```

Under the hood, this value is derived from the
``ID`` field in the
``/etc/os-release`` file for most operating
systems.

**`version`**:
Version of the OS.
`Required`. This can be either an exact match or a prefix followed by
the `*` wildcard.
To inspect the exact OS version of an instance, run:

```
gcloud beta compute instances os-inventory describe INSTANCE_NAME | grep "^Version: "
```

Under the hood, this value is derived from the
``VERSION_ID`` field in the
``/etc/os-release`` file for most operating
systems.

**--clear-group-labels**

**--clear-instances**

**--clear-zones**

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
gcloud compute instances ops-agents policies update
```

```
gcloud beta compute instances ops-agents policies update
```