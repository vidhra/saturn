# gcloud network-security client-tls-policies delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/client-tls-policies/delete](https://cloud.google.com/sdk/gcloud/reference/network-security/client-tls-policies/delete)*

**NAME**

: **gcloud network-security client-tls-policies delete - delete ClientTlsPolicy**

**SYNOPSIS**

: **`gcloud network-security client-tls-policies delete` (`[CLIENT_TLS_POLICY](https://cloud.google.com/sdk/gcloud/reference/network-security/client-tls-policies/delete#CLIENT_TLS_POLICY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/client-tls-policies/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/client-tls-policies/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/client-tls-policies/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete the specified ClientTlsPolicy.

**EXAMPLES**

: To delete a ClientTlsPolicy called 'my-client-tls-policy', run:

```
gcloud network-security client-tls-policies delete my-client-tls-policy --location=global
```

**POSITIONAL ARGUMENTS**

: **Client TLS policy resource - Name of the ClientTlsPolicy you want to delete. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `client_tls_policy` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CLIENT_TLS_POLICY`**:
ID of the client TLS policy or fully qualified identifier for the client TLS
policy.
To set the `client_tls_policy` attribute:

- provide the argument `client_tls_policy` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location Id.
To set the `location` attribute:

- provide the argument `client_tls_policy` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This command uses the `networksecurity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/networking](https://cloud.google.com/networking)

**NOTES**

: These variants are also available:

```
gcloud alpha network-security client-tls-policies delete
```

```
gcloud beta network-security client-tls-policies delete
```