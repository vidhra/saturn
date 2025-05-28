# gcloud network-connectivity service-connection-policies delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/delete](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/delete)*

**NAME**

: **gcloud network-connectivity service-connection-policies delete - delete a service connection policy**

**SYNOPSIS**

: **`gcloud network-connectivity service-connection-policies delete` (`[SERVICE_CONNECTION_POLICY](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/delete#SERVICE_CONNECTION_POLICY)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/delete#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete the specified service connection policy.

**EXAMPLES**

: To delete a service connection policy with name
``pol1`` in region
``us-central1``, run:

```
gcloud network-connectivity service-connection-policies delete pol1 --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Service connection policy resource - Name of the Service Connection Policy to be
deleted. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `service_connection_policy` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SERVICE_CONNECTION_POLICY`**:
ID of the service connection policy or fully qualified identifier for the
service connection policy.
To set the `service_connection_policy` attribute:

- provide the argument `service_connection_policy` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The location Id.
To set the `region` attribute:

- provide the argument `service_connection_policy` on the command line
with a fully specified name;
- provide the argument `--region` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This command uses the `networkconnectivity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)