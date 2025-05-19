# gcloud certificate-manager trust-configs delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/delete](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/delete)*

**NAME**

: **gcloud certificate-manager trust-configs delete - delete TrustConfig**

**SYNOPSIS**

: **`gcloud certificate-manager trust-configs delete` (`[TRUST_CONFIG](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/delete#TRUST_CONFIG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/delete#--async)`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/delete#--etag)`=`ETAG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete the specified TrustConfig.

**EXAMPLES**

: To delete a TrustConfig called 'my-trust-config', run:

```
gcloud certificate-manager trust-configs delete my-trust-config --location=global
```

**POSITIONAL ARGUMENTS**

: **TrustConfig resource - Name of the TrustConfig you want to delete. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `trust_config` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TRUST_CONFIG`**:
ID of the trustConfig or fully qualified identifier for the trustConfig.
To set the `trust_config` attribute:

- provide the argument `trust_config` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Certificate Manager location.
To set the `location` attribute:

- provide the argument `trust_config` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- default value of location is [global].**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--etag**:
The current etag of the asset. If an etag is provided and does not match the
current etag of the asset, the deletion will be blocked.

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

: This command uses the `certificatemanager/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/certificate-manager](https://cloud.google.com/certificate-manager)

**NOTES**

: These variants are also available:

```
gcloud alpha certificate-manager trust-configs delete
```

```
gcloud beta certificate-manager trust-configs delete
```