# gcloud beta access-context-manager levels describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/describe](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/describe)*

**NAME**

: **gcloud beta access-context-manager levels describe - show details about an access level**

**SYNOPSIS**

: **`gcloud beta access-context-manager levels describe` (`[LEVEL](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/describe#LEVEL)` : `[--policy](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/describe#--policy)`=`POLICY`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` Show details about an access level in a given access policy.

**EXAMPLES**

: To show the details of the access policy
``my-policy``, run:

```
gcloud beta access-context-manager levels describe my-policy
```

**POSITIONAL ARGUMENTS**

: **Level resource - The access level you want to show details about. The arguments
in this group can be used to specify the attributes of this resource.
This must be specified.

**`LEVEL`**:
ID of the level or fully qualified identifier for the level.
To set the `level` attribute:

- provide the argument `level` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--policy**:
The ID of the access policy.
To set the `policy` attribute:

- provide the argument `level` on the command line with a fully
specified name;
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

: This command is currently in beta and might change without notice. These
variants are also available:

```
gcloud access-context-manager levels describe
```

```
gcloud alpha access-context-manager levels describe
```