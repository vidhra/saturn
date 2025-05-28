# gcloud privateca certificates export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/export](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/export)*

**NAME**

: **gcloud privateca certificates export - export a pem-encoded certificate to a file**

**SYNOPSIS**

: **`gcloud privateca certificates export` (`[CERTIFICATE](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/export#CERTIFICATE)` : `[--issuer-location](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/export#--issuer-location)`=`ISSUER_LOCATION` `[--issuer-pool](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/export#--issuer-pool)`=`ISSUER_POOL`) `[--output-file](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/export#--output-file)`=`OUTPUT_FILE` [`[--include-chain](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/export#--include-chain)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/export#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To export a single pem-encoded certificate to a file, run the following:

```
gcloud privateca certificates export my-cert --issuer-pool=my-pool --issuer-location=us-west1 --output-file=cert.pem
```

To export a pem-encoded certificate along with its issuing chain in the same
file, run the following:

```
gcloud privateca certificates export my-cert --issuer-pool=my-pool --issuer-location=us-west1 --include-chain --output-file=chain.pem
```

You can omit the --issuer-location flag in both of the above examples if you've
already set the privateca/location property. For example:
$ [gcloud config set](https://cloud.google.com/sdk/gcloud/reference/config/set)
privateca/location us-west1

**The following is equivalent to the first example above.**

: ```
gcloud privateca certificates export my-cert --issuer-pool=my-pool --output-file=cert.pem
```

**The following is equivalent to the second example above.**

: ```
gcloud privateca certificates export my-cert --issuer-pool=my-pool --include-chain --output-file=chain.pem
```

**POSITIONAL ARGUMENTS**

: **CERTIFICATE resource - The certificate to export. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `CERTIFICATE` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CERTIFICATE`**:
ID of the CERTIFICATE or fully qualified identifier for the CERTIFICATE.
To set the `certificate` attribute:

- provide the argument `CERTIFICATE` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--issuer-location**:
The location of the CERTIFICATE.
To set the `issuer-location` attribute:

- provide the argument `CERTIFICATE` on the command line with a fully
specified name;
- provide the argument `--issuer-location` on the command line;
- set the property `privateca/location`.

**--issuer-pool**:
The parent CA Pool of the CERTIFICATE.
To set the `issuer-pool` attribute:

- provide the argument `CERTIFICATE` on the command line with a fully
specified name;
- provide the argument `--issuer-pool` on the command line.**

**REQUIRED FLAGS**

: **--output-file**:
The path where the resulting PEM-encoded certificate will be written.

**OPTIONAL FLAGS**

: **--include-chain**:
Whether to include the certificate's issuer chain in the exported file. If this
is set, the resulting file will contain the pem-encoded certificate and its
issuing chain, ordered from leaf to root.

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