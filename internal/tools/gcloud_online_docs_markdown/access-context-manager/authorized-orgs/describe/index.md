# gcloud access-context-manager authorized-orgs describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/describe](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/describe)*

**NAME**

: **gcloud access-context-manager authorized-orgs describe - show details about an authorized organizations description**

**SYNOPSIS**

: **`gcloud access-context-manager authorized-orgs describe` (`[AUTHORIZED_ORGS_DESC](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/describe#AUTHORIZED_ORGS_DESC)` : `[--policy](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/describe#--policy)`=`POLICY`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/authorized-orgs/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Show details about an existing authorized organizations description.

**EXAMPLES**

: To get details about an existing authorized organizations description, run:

```
gcloud access-context-manager authorized-orgs describe my_authorized_orgs_desc_id
```

**POSITIONAL ARGUMENTS**

: **Authorized orgs desc resource - The authorized organizations description for
which you want to show details. The arguments in this group can be used to
specify the attributes of this resource.
This must be specified.

**`AUTHORIZED_ORGS_DESC`**:
ID of the authorized-orgs-desc or fully qualified identifier for the
authorized-orgs-desc.
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
- set the property `access_context_manager/policy`;
- automatically, if the current account belongs to an organization with exactly
one access policy..**

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

: This command uses the `accesscontextmanager/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/access-context-manager/docs/reference/rest/](https://cloud.google.com/access-context-manager/docs/reference/rest/)

**NOTES**

: This variant is also available:

```
gcloud alpha access-context-manager authorized-orgs describe
```