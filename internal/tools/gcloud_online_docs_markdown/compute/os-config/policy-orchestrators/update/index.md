# gcloud compute os-config policy-orchestrators update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update)*

**NAME**

: **gcloud compute os-config policy-orchestrators update - update a policy orchestrator**

**SYNOPSIS**

: **`gcloud compute os-config policy-orchestrators update` (`[POLICY_ORCHESTRATOR](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update#POLICY_ORCHESTRATOR)` : `[--folder](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update#--folder)`=`FOLDER` `[--organization](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update#--organization)`=`ORGANIZATION`) [`[--action](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update#--action)`=`ACTION`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update#--async)`] [`[--policy-file](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update#--policy-file)`=`POLICY_FILE`] [`[--policy-id](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update#--policy-id)`=`POLICY_ID`] [`[--state](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update#--state)`=`STATE`] [`[--clear-folders](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update#--clear-folders)`     | `[--include-folders](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update#--include-folders)`=`INCLUDE_FOLDERS`] [`[--clear-locations](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update#--clear-locations)`     | `[--include-locations](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update#--include-locations)`=`INCLUDE_LOCATIONS`] [`[--clear-projects](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update#--clear-projects)`     | `[--include-projects](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update#--include-projects)`=`INCLUDE_PROJECTS`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a policy orchestrator.

**EXAMPLES**

: To update an policy orchestrator `my-orchestrator` in folder
`123456` with config file `/path/to/file/config.yaml`,
run:

```
gcloud compute os-config policy-orchestrators update my-orchestrator --folder=123456 --policy-file=/path/to/file/config.yaml
```

To update an policy orchestrator `my-orchestrator` in folder
`123456` with state STOPPED, run:

```
gcloud compute os-config policy-orchestrators update my-orchestrator --folder=123456 --state=stopped
```

**POSITIONAL ARGUMENTS**

: **Policy orchestrator resource - Policy orchestrator to update. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `policy_orchestrator` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`. This resource can be one of the
following types: [policy_orchestrator_project, policy_orchestrator_folder,
policy_orchestrator_organization].

This must be specified.

**`POLICY_ORCHESTRATOR`**:
ID of the policy_orchestrator or fully qualified identifier for the
policy_orchestrator.
To set the `policy_orchestrator` attribute:

- provide the argument `policy_orchestrator` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--folder**:
Folder of the policy_orchestrator.
To set the `folder` attribute:

- provide the argument `policy_orchestrator` on the command line with a
fully specified name;
- provide the argument `--folder` on the command line. Must be
specified for resource of type [policy_orchestrator_folder].

**--organization**:
Organization of the policy_orchestrator.
To set the `organization` attribute:

- provide the argument `policy_orchestrator` on the command line with a
fully specified name;
- provide the argument `--organization` on the command line. Must be
specified for resource of type [policy_orchestrator_organization].**

**FLAGS**

: **--action**:
Action to be taken on policy. `ACTION` must be one of:

**`delete`**:
Delete a policy with a given name. `policy-id` must be specified.

**`upsert`**:
Create or update a policy. `policy-file` must be specified.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--policy-file**:
Absolute path to the OS policy assignment file on your local client. File must
be in either JSON or YAML format. This file defines the OS policies that you
want to apply to your VMs, the target VMs that you want to apply the policies
to, and the rollout rate at which to apply the OS policies on a zonal level. For
more information about this resource and sample OS policy assignment files, see
[https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies#os-policy-assignment](https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies#os-policy-assignment).

**--policy-id**:
Policy id. Must be specified for `DELETE` action.

**--state**:
State of the policy orchestrator. `STATE` must be one of:

**`active`**:
Updates the policy orchestrator to `ACTIVE` state.

**`stopped`**:
Updates the policy orchestrator to `STOPPED` state.

**--include-folders**

**Locations to include in the policy orchestrator, e.g.
`us-central1-a`. If `include-locations` is set,
`clear-locations` must not be set.
At most one of these can be specified:

**--clear-locations**:
Clears included locations from policy orchestrator selectors.

**--include-locations**:
Applies policy to selected locations only.**

**Projects to include in the policy orchestrator. Comma separated list of project
numbers. If `include-projects` is set, `clear-projects`
must not be set.
At most one of these can be specified:

**--clear-projects**:
Clears included projects from policy orchestrator selectors.

**--include-projects**:
Applies policy to selected projects only.**

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

: This command uses the `osconfig/v2` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/docs/osconfig/rest](https://cloud.google.com/compute/docs/osconfig/rest)

**NOTES**

: These variants are also available:

```
gcloud alpha compute os-config policy-orchestrators update
```

```
gcloud beta compute os-config policy-orchestrators update
```