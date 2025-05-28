# gcloud privateca subordinates delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/delete](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/delete)*

**NAME**

: **gcloud privateca subordinates delete - delete a subordinate certificate authority**

**SYNOPSIS**

: **`gcloud privateca subordinates delete` (`[CERTIFICATE_AUTHORITY](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/delete#CERTIFICATE_AUTHORITY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/delete#--location)`=`LOCATION` `[--pool](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/delete#--pool)`=`POOL`) [`[--ignore-active-certificates](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/delete#--ignore-active-certificates)`] [`[--ignore-dependent-resources](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/delete#--ignore-dependent-resources)`] [`[--skip-grace-period](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/delete#--skip-grace-period)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Subordinate Certificate Authority. Deleted Subordinate Certificate
Authorities may be recovered with the `[gcloud privateca
subordinates undelete](https://cloud.google.com/sdk/gcloud/reference/privateca/subordinates/undelete)` command within a grace period of 30 days.
Use the --skip-grace-period flag to delete as soon as possible without the
30-day grace period to undelete.
Note that any user-managed KMS keys or Google Cloud Storage buckets will not be
affected by this operation. You will need to delete the user- managed resources
separately once the CA is deleted. Any Google-managed resources will be cleaned
up.
The CA specified in this command MUST:

```
1) be in the DISABLED or STAGED state.
2) have no un-revoked or un-expired certificates. Use the revoke command
   to revoke any active certificates.
```

Use the `--ignore-active-certificates` flag to remove 2) as a
requirement.

**EXAMPLES**

: To delete a subordinate CA:

```
gcloud privateca subordinates delete server-tls-1 --pool=my-pool --location=us-west1
```

To delete a CA while skipping the confirmation input:

```
gcloud privateca subordinates delete server-tls-1s --pool=my-pool --location=us-west1 --quiet
```

To undo the deletion for a subordinate CA:

```
gcloud privateca subordinates undelete server-tls-1 --pool=my-pool --location=us-west1
```

**POSITIONAL ARGUMENTS**

: **CERTIFICATE AUTHORITY resource - The certificate authority to delete. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CERTIFICATE_AUTHORITY`**:
ID of the CERTIFICATE_AUTHORITY or fully qualified identifier for the
CERTIFICATE_AUTHORITY.
To set the `certificate_authority` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the CERTIFICATE_AUTHORITY.
To set the `location` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line with
a fully specified name;
- provide the argument `--location` on the command line;
- set the property `privateca/location`.

**--pool**:
The parent CA Pool of the CERTIFICATE_AUTHORITY.
To set the `pool` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line with
a fully specified name;
- provide the argument `--pool` on the command line.**

**FLAGS**

: **--ignore-active-certificates**:
If this flag is set, the Certificate Authority will be deleted even if the
Certificate Authority has un-revoked or un-expired certificates after the grace
period.

**--ignore-dependent-resources**:
This field skips the integrity check that would normally prevent breaking a CA
Pool if it is used by another cloud resource and allows the CA Pool to be in a
state where it is not able to issue certificates. Doing so may result in
unintended and unrecoverable effects on any dependent resource(s) since the CA
Pool would not be able to issue certificates.

**--skip-grace-period**:
If this flag is set, the Certificate Authority will be deleted as soon as
possible without a 30-day grace period where undeletion would have been allowed.
If you proceed, there will be no way to recover this CA.

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