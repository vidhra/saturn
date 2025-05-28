# gcloud privateca pools update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/pools/update](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/update)*

**NAME**

: **gcloud privateca pools update - update an existing  CA Pool**

**SYNOPSIS**

: **`gcloud privateca pools update` (`[CA_POOL](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/update#CA_POOL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/update#--location)`=`LOCATION`) [`[--issuance-policy](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/update#--issuance-policy)`=`ISSUANCE_POLICY`] [`[--no-publish-ca-cert](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/update#--publish-ca-cert)`] [`[--no-publish-crl](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/update#--publish-crl)`] [`[--publishing-encoding-format](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/update#--publishing-encoding-format)`=`PUBLISHING_ENCODING_FORMAT`; default="pem"] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To update labels on a CA pool:

```
gcloud privateca pools update my-pool --location=us-west1 --update-labels=foo=bar
```

To disable publishing CRLs on a CA pool:

```
gcloud privateca pools update my-pool --location=us-west1 --no-publish-crl
```

**POSITIONAL ARGUMENTS**

: **CA POOL resource - The ca pool to update. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
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

**FLAGS**

: **--issuance-policy**:
A YAML file describing this CA Pool's issuance policy.

**--publish-ca-cert**:
If this is enabled, the following will happen: 1) The CA certificates will be
written to a known location within the CA distribution point. 2) The AIA
extension in all issued certificates will point to the CA cert URL in that
distribution point.
If this gets disabled, the AIA extension will not be written to any future
certificates issued by this CA. However, an existing bucket will not be deleted,
and the CA certificates will not be removed from that bucket.
Note that the same bucket may be used for the CRLs if --publish-crl is set.
Enabled by default, use `--no-publish-ca-cert` to disable.

**--publish-crl**:
If this gets enabled, the following will happen: 1) CRLs will be written to a
known location within the CA distribution point. 2) The CDP extension in all
future issued certificates will point to the CRL URL in that distribution point.
If this gets disabled, the CDP extension will not be written to any future
certificates issued by CAs in this pool, and new CRLs will not be published to
that bucket (which affects existing certs). However, an existing bucket will not
be deleted, and any existing CRLs will not be removed from that bucket.
Note that the same bucket may be used for the CA cert if --publish-ca-cert is
set.
CRL publication is not supported for CAs in the DevOps tier.
Enabled by default, use `--no-publish-crl` to disable.

**--publishing-encoding-format**:
The encoding format of the content published to storage buckets.
`PUBLISHING_ENCODING_FORMAT` must be one of:
`der`, `pem`.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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