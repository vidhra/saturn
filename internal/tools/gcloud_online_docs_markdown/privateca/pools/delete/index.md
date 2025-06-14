# gcloud privateca pools delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/pools/delete](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/delete)*

**NAME**

: **gcloud privateca pools delete - delete a CA pool**

**SYNOPSIS**

: **`gcloud privateca pools delete` (`[CA_POOL](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/delete#CA_POOL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/delete#--location)`=`LOCATION`) [`[--ignore-dependent-resources](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/delete#--ignore-dependent-resources)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/pools/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Note that all certificate authorities must be removed from the CA Pool before
the CA pool can be deleted.

**EXAMPLES**

: To delete a CA pool:

```
gcloud privateca pools delete my-pool --location=us-west1
```

To delete a CA pool while skipping the confirmation input:

```
gcloud privateca pools delete my-pool --location=us-west1 --quiet
```

**POSITIONAL ARGUMENTS**

: **CA POOL resource - The ca pool to delete. The arguments in this group can be
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

: **--ignore-dependent-resources**:
This field skips the integrity check that would normally prevent breaking a CA
Pool if it is used by another cloud resource and allows the CA Pool to be in a
state where it is not able to issue certificates. Doing so may result in
unintended and unrecoverable effects on any dependent resource(s) since the CA
Pool would not be able to issue certificates.

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