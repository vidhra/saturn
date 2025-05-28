# gcloud privateca pools create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/pools/create](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/create)*

**NAME**

: **gcloud privateca pools create - create a new CA Pool**

**SYNOPSIS**

: **`gcloud privateca pools create` (`[CA_POOL](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/create#CA_POOL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/create#--location)`=`LOCATION`) [`[--issuance-policy](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/create#--issuance-policy)`=`ISSUANCE_POLICY`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--no-publish-ca-cert](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/create#--publish-ca-cert)`] [`[--no-publish-crl](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/create#--publish-crl)`] [`[--publishing-encoding-format](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/create#--publishing-encoding-format)`=`PUBLISHING_ENCODING_FORMAT`; default="pem"] [`[--tier](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/create#--tier)`=`TIER`; default="enterprise"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/create#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create a CA pool in the dev ops tier:

```
gcloud privateca pools create my-pool --location=us-west1 --tier=devops
```

To create a CA pool and restrict what it can issue:

```
gcloud privateca pools create my-pool --location=us-west1 --issuance-policy=policy.yaml
```

To create a CA pool that doesn't publicly publish CA certificates and CRLs:

```
gcloud privateca pools create my-pool --location=us-west1 --issuance-policy=policy.yaml --no-publish-ca-cert --no-publish-crl
```

**POSITIONAL ARGUMENTS**

: **CA POOL resource - The ca pool to create. The arguments in this group can be
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

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--publish-ca-cert**:
If this is enabled, the following will happen: 1) The CA certificates will be
written to a known location within the CA distribution point. 2) The AIA
extension in all issued certificates will point to the CA cert URL in that
distribition point.
Note that the same bucket may be used for the CRLs if --publish-crl is set.
Enabled by default, use `--no-publish-ca-cert` to disable.

**--publish-crl**:
If this gets enabled, the following will happen: 1) CRLs will be written to a
known location within the CA distribution point. 2) The CDP extension in all
future issued certificates will point to the CRL URL in that distribution point.
Note that the same bucket may be used for the CA cert if --publish-ca-cert is
set.
CRL publication is not supported for CAs in the DevOps tier.
Enabled by default, use `--no-publish-crl` to disable.

**--publishing-encoding-format**:
The encoding format of the content published to storage buckets.
`PUBLISHING_ENCODING_FORMAT` must be one of:
`der`, `pem`.

**--tier**:
The tier for the Certificate Authority. `TIER` must be one
of: `devops`, `enterprise`.

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