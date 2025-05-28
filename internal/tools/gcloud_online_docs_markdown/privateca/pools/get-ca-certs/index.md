# gcloud privateca pools get-ca-certs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/pools/get-ca-certs](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/get-ca-certs)*

**NAME**

: **gcloud privateca pools get-ca-certs - get the root CA certs for all active CAs in the CA pool**

**SYNOPSIS**

: **`gcloud privateca pools get-ca-certs` (`[CA_POOL](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/get-ca-certs#CA_POOL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/get-ca-certs#--location)`=`LOCATION`) `[--output-file](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/get-ca-certs#--output-file)`=`OUTPUT_FILE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/get-ca-certs#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To get the root CA certs for all active CAs in the CA pool:

```
gcloud privateca pools get-ca-certs my-pool --output-file=ca-certificates.pem --location=us-west1
```

**POSITIONAL ARGUMENTS**

: **CA POOL resource - The ca pool whose CA certificates should be fetched. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `CA_POOL` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CA_POOL`**:
ID of the CA_POOL or fully qualified identifier for the CA_POOL.
To set the `pool` attribute:

- provide the argument `CA_POOL` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the CA_POOL.
To set the `location` attribute:

- provide the argument `CA_POOL` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `privateca/location`.**

**REQUIRED FLAGS**

: **--output-file**:
The path where the concatenated PEM certificates will be written. This will
include the root CA certificate for each active CA in the CA pool.

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