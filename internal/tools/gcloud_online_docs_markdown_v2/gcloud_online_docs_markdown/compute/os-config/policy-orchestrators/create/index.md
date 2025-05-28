# gcloud compute os-config policy-orchestrators create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create)*

**NAME**

: **gcloud compute os-config policy-orchestrators create - create a policy orchestrator**

**SYNOPSIS**

: **`gcloud compute os-config policy-orchestrators create` (`[POLICY_ORCHESTRATOR](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create#POLICY_ORCHESTRATOR)` : `[--folder](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create#--folder)`=`FOLDER` `[--organization](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create#--organization)`=`ORGANIZATION`) `[--policy-type](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create#--policy-type)`=`POLICY_TYPE` [`[--action](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create#--action)`=`ACTION`; default="upsert"] [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create#--async)`] [`[--include-folders](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create#--include-folders)`=`INCLUDE_FOLDERS`] [`[--include-locations](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create#--include-locations)`=`INCLUDE_LOCATIONS`] [`[--include-projects](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create#--include-projects)`=`INCLUDE_PROJECTS`] [`[--policy-file](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create#--policy-file)`=`POLICY_FILE`] [`[--policy-id](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create#--policy-id)`=`POLICY_ID`] [`[--state](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create#--state)`=`STATE`; default="ACTIVE"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a policy orchestrator.

**EXAMPLES**

: To create a policy orchestrator `my-orchestrator` in folder
`123456` for OS policy assignment with config file
`/path/to/file/config.yaml`, run:

```
gcloud compute os-config policy-orchestrators create my-orchestrator --folder=123456 --policy-type os_policy_assignment_v1 --policy-file=/path/to/file/config.yaml
```

To create a policy orchestrator `my-orchestrator` in folder
`123456` that deletes OS Policy assignments with id
`my-policy`, run:

```
gcloud compute os-config policy-orchestrators create my-orchestrator --folder=123456 --policy-type os_policy_assignment_v1 --action delete --policy-id my-policy
```

**POSITIONAL ARGUMENTS**

: **Policy orchestrator resource - Policy orchestrator to create. The arguments in
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

**REQUIRED FLAGS**

: **--policy-type**:
Policy type to use. `POLICY_TYPE` must be (only one value
is supported):

**`os_policy_assignment_v1`**:
OS policy assignment v1.

**OPTIONAL FLAGS**

: **--action**:
Action to be taken on policy. `ACTION` must be one of:

**`delete`**:
Delete a policy with a given name. `policy-id` must be specified.

**`upsert`**:
Create or update a policy. `policy-file` must be specified.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--include-folders**:
Applies policy to selected folders. Comma-separated list of folder numbers. Can
beused together with `--include-projects`.

**--include-locations**:
Applies policy to selected locations, e.g. `us-central1-a`.

**--include-projects**:
Applies policy to selected projects. Comma-separated list of project numbers.
Can be used together with `--include-folders`.

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
Creates a policy orchestrator in `ACTIVE` state.

**`stopped`**:
Creates a policy orchestrator in `STOPPED` state.

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
gcloud alpha compute os-config policy-orchestrators create
```

```
gcloud beta compute os-config policy-orchestrators create
```