# gcloud kms ekm-connections create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/create](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/create)*

**NAME**

: **gcloud kms ekm-connections create - create a new ekm connection**

**SYNOPSIS**

: **`gcloud kms ekm-connections create` (`[EKM_CONNECTION](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/create#EKM_CONNECTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/create#--location)`=`LOCATION`) `[--hostname](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/create#--hostname)`=`HOSTNAME` `[--server-certificates-files](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/create#--server-certificates-files)`=[`SERVER_CERTIFICATES`,…] `[--service-directory-service](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/create#--service-directory-service)`=`SERVICE_DIRECTORY_SERVICE` [`[--endpoint-filter](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/create#--endpoint-filter)`=`ENDPOINT_FILTER`] [`[--crypto-space-path](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/create#--crypto-space-path)`=`CRYPTO_SPACE_PATH` `[--key-management-mode](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/create#--key-management-mode)`=`KEY_MANAGEMENT_MODE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new connection within the given location.

**EXAMPLES**

: The following command creates an ekm connection named `laplace`
within the location `us-central1`:

```
gcloud kms ekm-connections create laplace --location=us-central1 --service-directory-service="foo" --endpoint-filter="foo > bar" --hostname="hostname.foo" --server-certificates-files=foo.pem,bar.pem
```

The following command creates an ekm connection named `laplace`
within the location `us-central1` in `cloud-kms` key
management mode with the required crypto-space-path :

```
gcloud kms ekm-connections create laplace --location=us-central1 --service-directory-service="foo" --endpoint-filter="foo > bar" --hostname="hostname.foo" --key-management-mode=cloud-kms --crypto-space-path="foo" --server-certificates-files=foo.pem,bar.pem
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

**REQUIRED FLAGS**

: **--hostname**:
The hostname of the EKM replica used at TLS and HTTP layers.

**--server-certificates-files**:
A list of filenames of leaf server certificates used to authenticate HTTPS
connections to the EKM replica in PEM format. If files are not in PEM, the
assumed format will be DER.

**--service-directory-service**:
The resource name of the Service Directory service pointing to an EKM replica.

**OPTIONAL FLAGS**

: **--endpoint-filter**:
The filter applied to the endpoints of the resolved service. If no filter is
specified, all endpoints will be considered.

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
gcloud alpha kms ekm-connections create
```

```
gcloud beta kms ekm-connections create
```