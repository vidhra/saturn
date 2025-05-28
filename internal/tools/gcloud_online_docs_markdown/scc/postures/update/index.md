# gcloud scc postures update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/postures/update](https://cloud.google.com/sdk/gcloud/reference/scc/postures/update)*

**NAME**

: **gcloud scc postures update - update the given Cloud Security Command Center posture**

**SYNOPSIS**

: **`gcloud scc postures update` (`[POSTURE](https://cloud.google.com/sdk/gcloud/reference/scc/postures/update#POSTURE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/scc/postures/update#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/postures/update#--organization)`=`ORGANIZATION`) `[--posture-from-file](https://cloud.google.com/sdk/gcloud/reference/scc/postures/update#--posture-from-file)`=`PATH_TO_FILE` `[--revision-id](https://cloud.google.com/sdk/gcloud/reference/scc/postures/update#--revision-id)`=`REVISION_ID` [`[--async](https://cloud.google.com/sdk/gcloud/reference/scc/postures/update#--async)`] [`[--update-mask](https://cloud.google.com/sdk/gcloud/reference/scc/postures/update#--update-mask)`=`UPDATE_MASK`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/postures/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud Security Command Center (SCC) posture.
Fields specified in update-mask flag are updated. Updatable fields are state,
description and policy_sets. State of the posture can't be updated along with
update of other fields. An empty or "`" as field mask will result in update
of policy_sets and description. In case of the update of policy_sets, the value
mentioned in the update posture request overwrites the exisiting value of
policy_sets.
Valid state transitions are: a) ACTIVE to DRAFT b) ACTIVE to DEPRECATED c) DRAFT
to ACTIVE d) DEPRECATED to ACTIVE
The update operation will result in the update of the revision-id specified in
the request, unless the posture revision is currently deployed on a workload. A
new revision is created for an already deployed posture revision.`

**EXAMPLES**

: Update the revision-id `abcdefgh` of the posture named
`foo-posture` in the organization
`organizations/123/locations/global`: Change State to ACTIVE.
```
gcloud scc postures update organizations/123/locations/global/postures/foo-posture --posture-from-file=update_posture.yaml --revision-id=abcdefgh update_mask=state
```

```
Contents of update_posture.yaml are |
    name: organizations/123/locations/global/postures/foo-posture
    state: ACTIVE
```

Update the revision-id `abcdefgh` of the posture named
`foo-posture` in the organization
`organizations/123/locations/global`: Change description and
policy_sets to the values mentioned in update_posture.yaml
```
gcloud scc postures update organizations/123/locations/global/postures/foo-posture --posture-from-file=update_posture.yaml --revision-id=abcdefgh update_mask=description,policy_sets
```

```
Contents of update_posture.yaml are |
    name: organizations/123/locations/global/postures/foo-posture
    description: updated description
    policy_sets:
    - policy_set_id: newPolicySet1
      policies:
        - policy_id: newPolicy
          constraint:
            org_policy_canned_constraint:
              canned_constraint_id: storage.uniformBucketLevelAccess
              policy_rules:
                enforce: false
    - policy_set_id: PolicySet2
      policies:
        - policy_id: Policy3
          constraint:
            org_policy_custom_constraint:
              custom_constraint:
                name: organizations/9454078371/customConstraints/custom.newConstraint
                resource_types: container.$$UNIVERSE_DOMAIN$$/NodePool
                method_types: UPDATE
                condition: resource.management.autoUpgrade == false
                action_type: ALLOW
              policy_rules:
                enforce: true
```

**POSITIONAL ARGUMENTS**

: **Posture resource - Arguments and flags that specify the Posture instance to be
updated. The arguments in this group can be used to specify the attributes of
this resource.
This must be specified.

**`POSTURE`**:
ID of the posture or fully qualified identifier for the posture.
To set the `posture` attribute:

- provide the argument `posture` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
ID of the location where the resource exists (for example, global).
To set the `location` attribute:

- provide the argument `posture` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--organization**:
ID of the organization which is the parent of the resource.
To set the `organization` attribute:

- provide the argument `posture` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line.**

**REQUIRED FLAGS**

: **--posture-from-file**:
Path of the file containing the details of the field to be updated. Contents
include the name of the posture to be updated and value of the fields to be
updated. Use a full or relative path to a local file containing the value of
posture.

**--revision-id**:
Revision ID of the posture to be updated. The same revision ID will be updated
in case the posture revision is not deployed on any workload. A new revision
will be created for a deployed posture.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--update-mask**:
Comma separated string containing list of fields to be updated.

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

: This command uses the `securityposture/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/security-command-center](https://cloud.google.com/security-command-center)

**NOTES**

: This variant is also available:

```
gcloud alpha scc postures update
```