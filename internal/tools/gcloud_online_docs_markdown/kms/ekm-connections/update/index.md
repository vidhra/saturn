# gcloud kms ekm-connections update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/update](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/update)*

**NAME**

: **gcloud kms ekm-connections update - update an ekmconnection**

**SYNOPSIS**

: **`gcloud kms ekm-connections update` (`[EKM_CONNECTION](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/update#EKM_CONNECTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/update#--location)`=`LOCATION`) [`[--endpoint-filter](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/update#--endpoint-filter)`=`ENDPOINT_FILTER`] [`[--hostname](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/update#--hostname)`=`HOSTNAME`] [`[--server-certificates-files](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/update#--server-certificates-files)`=[`SERVER_CERTIFICATES`,…]] [`[--service-directory-service](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/update#--service-directory-service)`=`SERVICE_DIRECTORY_SERVICE`] [`[--crypto-space-path](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/update#--crypto-space-path)`=`CRYPTO_SPACE_PATH` `[--key-management-mode](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/update#--key-management-mode)`=`KEY_MANAGEMENT_MODE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud kms ekm-connections update can be used to update the ekmconnection.
Updates can be made to the ekmconnection's service resolver's fields.

**EXAMPLES**

: The following command updates an ekm-connection named `laplace`
service resolver's hostname within location `us-east1`:

```
gcloud kms ekm-connections update laplace --location=us-east1 --hostname=newhostname.foo
```

The following command updates an ekm-connection named `laplace`
service resolver's service_directory_service, endpoint_filter, hostname, and
server_certificates within location `us-east1`:

```
gcloud kms ekm-connections update laplace --location=us-east1 --service-directory-service="foo" --endpoint-filter="foo > bar" --hostname="newhostname.foo" --server-certificates-files=foo.pem,bar.pem
```

The following command updates an ekm-connection named `laplace`
key_management_mode within location `us-east1`:

```
gcloud kms ekm-connections update laplace --location=us-east1 --key-management-mode=manual
```

**POSITIONAL ARGUMENTS**

: **Ekmconnection resource - The KMS ekm connection resource. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `ekm_connection` on the command line with a
fully specified name;
- set the property `core/project`.

This must be specified.

**`EKM_CONNECTION`**:
ID of the ekmconnection or fully qualified identifier for the ekmconnection.
To set the `ekmconnection` attribute:

- provide the argument `ekm_connection` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Google Cloud location for the ekmconnection.
To set the `location` attribute:

- provide the argument `ekm_connection` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--endpoint-filter**:
The filter applied to the endpoints of the resolved service. If no filter is
specified, all endpoints will be considered.

**--hostname**:
The hostname of the EKM replica used at TLS and HTTP layers.

**--server-certificates-files**:
A list of filenames of leaf server certificates used to authenticate HTTPS
connections to the EKM replica in PEM format. If files are not in PEM, the
assumed format will be DER.

**--service-directory-service**:
The resource name of the Service Directory service pointing to an EKM replica.

**--crypto-space-path**

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

**NOTES**

: These variants are also available:

```
gcloud alpha kms ekm-connections update
```

```
gcloud beta kms ekm-connections update
```