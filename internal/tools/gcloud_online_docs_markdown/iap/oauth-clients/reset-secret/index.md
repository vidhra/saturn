# gcloud iap oauth-clients reset-secret  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iap/oauth-clients/reset-secret](https://cloud.google.com/sdk/gcloud/reference/iap/oauth-clients/reset-secret)*

**NAME**

: **gcloud iap oauth-clients reset-secret - reset a Cloud IAP OAuth client secret**

**SYNOPSIS**

: **`gcloud iap oauth-clients reset-secret` (`[NAME](https://cloud.google.com/sdk/gcloud/reference/iap/oauth-clients/reset-secret#NAME)` : `[--brand](https://cloud.google.com/sdk/gcloud/reference/iap/oauth-clients/reset-secret#--brand)`=`BRAND`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iap/oauth-clients/reset-secret#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud iap oauth-clients reset-secret` is used to reset a Cloud IAP
OAuth client secret. Note this command cannot be used to reset the secret for
any other type of OAuth client in your project.

**EXAMPLES**

: To reset a Cloud IAP OAuth client secret, run:

```
gcloud iap oauth-clients reset-secret NAME
```

To reset a Cloud IAP OAuth client secret for a specific brand, run:

```
gcloud iap oauth-clients reset-secret NAME --brand=BRAND
```

**POSITIONAL ARGUMENTS**

: **Proxy client resource - Name of the Cloud IAP OAuth client whose secret will be
reset. The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `name` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NAME`**:
ID of the proxy client or fully qualified identifier for the proxy client.
To set the `identity_aware_proxy_clients` attribute:

- provide the argument `name` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--brand**:
The name of the OAuth brand.
To set the `brand` attribute:

- provide the argument `name` on the command line with a fully
specified name;
- provide the argument `--brand` on the command line.**

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
gcloud alpha iap oauth-clients reset-secret
```

```
gcloud beta iap oauth-clients reset-secret
```