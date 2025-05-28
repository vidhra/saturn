# gcloud iap oauth-brands describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iap/oauth-brands/describe](https://cloud.google.com/sdk/gcloud/reference/iap/oauth-brands/describe)*

**NAME**

: **gcloud iap oauth-brands describe - describe a Cloud OAuth brand**

**SYNOPSIS**

: **`gcloud iap oauth-brands describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/iap/oauth-brands/describe#NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iap/oauth-brands/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud iap oauth-brands describe` is used to describe a Cloud OAuth
brand.

**EXAMPLES**

: To describe a Cloud OAuth brand with name NAME, run:

```
gcloud iap oauth-brands describe NAME
```

To describe a Cloud OAuth brand with name NAME inside project PROJECT_ID, run:

```
gcloud iap oauth-brands describe NAME --project=PROJECT_ID
```

**POSITIONAL ARGUMENTS**

: **Brand resource - Name of the Cloud OAuth brand to describe. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `name` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NAME`**:
ID of the brand or fully qualified identifier for the brand.
To set the `brand` attribute:

- provide the argument `name` on the command line.**

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

: This command uses the `iap/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/iap](https://cloud.google.com/iap)

**NOTES**

: These variants are also available:

```
gcloud alpha iap oauth-brands describe
```

```
gcloud beta iap oauth-brands describe
```