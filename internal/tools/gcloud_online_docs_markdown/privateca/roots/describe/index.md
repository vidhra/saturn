# gcloud privateca roots describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/roots/describe](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/describe)*

**NAME**

: **gcloud privateca roots describe - get metadata for a root Certificate Authority**

**SYNOPSIS**

: **`gcloud privateca roots describe` (`[CERTIFICATE_AUTHORITY](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/describe#CERTIFICATE_AUTHORITY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/describe#--location)`=`LOCATION` `[--pool](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/describe#--pool)`=`POOL`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Returns metadata for the given Certificate Authority.

**EXAMPLES**

: To get metadata for the root CA 'prod-root' in location 'us-west1' and CA Pool
'my-pool':

```
gcloud privateca roots describe server-tls-1 --location=us-west1 --pool=my-pool
```

To download the PEM-encoded CA certificate chain for the 'prod-root' CA in
location 'us-west1' and CA Pool 'my-pool' to a file called 'prod-root.crt':

```
gcloud privateca roots describe prod-root --location=us-west1 --pool=my-pool --format="value(pemCaCertificates)" > ./prod-root.crt
```

**POSITIONAL ARGUMENTS**

: **CERTIFICATE AUTHORITY resource - The certificate authority for which to obtain
metadata. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `certificate_authority` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CERTIFICATE_AUTHORITY`**:
ID of the CERTIFICATE_AUTHORITY or fully qualified identifier for the
CERTIFICATE_AUTHORITY.
To set the `certificate_authority` attribute:

- provide the argument `certificate_authority` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the CERTIFICATE_AUTHORITY.
To set the `location` attribute:

- provide the argument `certificate_authority` on the command line with
a fully specified name;
- provide the argument `--location` on the command line;
- set the property `privateca/location`.

**--pool**:
The ID of the CA Pool.
To set the `pool` attribute:

- provide the argument `certificate_authority` on the command line with
a fully specified name;
- provide the argument `--pool` on the command line.**

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

: This command uses the `privateca/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/](https://cloud.google.com/)