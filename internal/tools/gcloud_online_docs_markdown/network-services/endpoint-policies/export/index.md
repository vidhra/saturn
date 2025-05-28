# gcloud network-services endpoint-policies export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-services/endpoint-policies/export](https://cloud.google.com/sdk/gcloud/reference/network-services/endpoint-policies/export)*

**NAME**

: **gcloud network-services endpoint-policies export - export endpoint policy**

**SYNOPSIS**

: **`gcloud network-services endpoint-policies export` (`[ENDPOINT_POLICY](https://cloud.google.com/sdk/gcloud/reference/network-services/endpoint-policies/export#ENDPOINT_POLICY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-services/endpoint-policies/export#--location)`=`LOCATION`) [`[--destination](https://cloud.google.com/sdk/gcloud/reference/network-services/endpoint-policies/export#--destination)`=`DESTINATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-services/endpoint-policies/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export an endpoit policy.

**EXAMPLES**

: To export an endpoint policy named 'my-endpoint-policy', run:

```
gcloud network-services endpoint-policies export my-endpoint-policy --destination=my-endpoint-policy.yaml --location=global
```

**POSITIONAL ARGUMENTS**

: **Endpoint policy resource - Name of the endpoint policy to export. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `endpoint_policy` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENDPOINT_POLICY`**:
ID of the endpoint policy or fully qualified identifier for the endpoint policy.
To set the `endpoint_policy` attribute:

- provide the argument `endpoint_policy` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location Id.
To set the `location` attribute:

- provide the argument `endpoint_policy` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--destination**:
Path to a YAML file where the configuration will be exported. The exported data
will not contain any output-only fields. Alternatively, you may omit this flag
to write to standard output. For a schema describing the export/import format,
see $CLOUDSDKROOT/lib/googlecloudsdk/schemas/…

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

: This command uses the `networkservices/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/networking](https://cloud.google.com/networking)

**NOTES**

: These variants are also available:

```
gcloud alpha network-services endpoint-policies export
```

```
gcloud beta network-services endpoint-policies export
```