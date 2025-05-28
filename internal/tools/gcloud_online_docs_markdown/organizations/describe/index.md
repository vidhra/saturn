# gcloud organizations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/organizations/describe](https://cloud.google.com/sdk/gcloud/reference/organizations/describe)*

**NAME**

: **gcloud organizations describe - show metadata for an organization**

**SYNOPSIS**

: **`gcloud organizations describe` `[ORGANIZATION_ID](https://cloud.google.com/sdk/gcloud/reference/organizations/describe#ORGANIZATION_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/organizations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Shows metadata for an organization, given a valid organization ID. If an
organization domain is supplied instead, this command will attempt to find the
organization by domain name.
This command can fail for the following reasons:

- The organization specified does not exist.
- The active account does not have permission to access the given organization.
- The domain name supplied does not correspond to a unique organization ID.

**EXAMPLES**

: The following command prints metadata for an organization with the ID
`3589215982`:

```
gcloud organizations describe 3589215982
```

The following command prints metadata for an organization associated with the
domain ``example.com``:

```
gcloud organizations describe example.com
```

**POSITIONAL ARGUMENTS**

: **`ORGANIZATION_ID`**:
ID or domain for the organization you want to describe.

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
gcloud alpha organizations describe
```

```
gcloud beta organizations describe
```