# gcloud access-context-manager authorized-orgs update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/update](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/update)*

**NAME**

: **gcloud access-context-manager authorized-orgs update - update the organizations for an existing authorized organizations description**

**SYNOPSIS**

: **`gcloud access-context-manager authorized-orgs update` (`[AUTHORIZED_ORGS_DESC](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/update#AUTHORIZED_ORGS_DESC)` : `[--policy](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/update#--policy)`=`POLICY`) [`[--add-orgs](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/update#--add-orgs)`=[`ORGS`,…]     | `[--clear-orgs](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/update#--clear-orgs)`     | `[--remove-orgs](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/update#--remove-orgs)`=[`ORGS`,…]     | `[--set-orgs](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/update#--set-orgs)`=[`ORGS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command updates an authorized organizations description.

**EXAMPLES**

: To update the organizations for an authorized organizations description:

```
gcloud access-context-manager authorized-orgs update my-authorized-orgs --add-orgs="organizations/123,organizations/456"
```

**POSITIONAL ARGUMENTS**

: **Authorized orgs desc resource - The authorized orgs desc to update. The
arguments in this group can be used to specify the attributes of this resource.
This must be specified.

**`AUTHORIZED_ORGS_DESC`**:
ID of the authorized_orgs_desc or fully qualified identifier for the
authorized_orgs_desc.
To set the `authorized_orgs_desc` attribute:

- provide the argument `authorized_orgs_desc` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--policy**:
The ID of the access policy.
To set the `policy` attribute:

- provide the argument `authorized_orgs_desc` on the command line with
a fully specified name;
- provide the argument `--policy` on the command line;
- set the property `access_context_manager/policy`.**

**FLAGS**

: **These flags modify the member orgs of this authorized_orgs_desc. Orgs must be
organizations, in the form
`organizations/<organizationsnumber>`.
At most one of these can be specified:

**--add-orgs**:
Append the given values to the current orgs.

**--clear-orgs**:
Empty the current orgs.

**--remove-orgs**:
Remove the given values from the current orgs.

**--set-orgs**:
Completely replace the current orgs with the given values.**

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

: This variant is also available:

```
gcloud alpha access-context-manager authorized-orgs update
```