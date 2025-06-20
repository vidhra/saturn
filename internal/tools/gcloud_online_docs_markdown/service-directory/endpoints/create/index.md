# gcloud service-directory endpoints create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/service-directory/endpoints/create](https://cloud.google.com/sdk/gcloud/reference/service-directory/endpoints/create)*

**NAME**

: **gcloud service-directory endpoints create - creates an endpoint**

**SYNOPSIS**

: **`gcloud service-directory endpoints create` (`[ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/service-directory/endpoints/create#ENDPOINT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/service-directory/endpoints/create#--location)`=`LOCATION` `[--namespace](https://cloud.google.com/sdk/gcloud/reference/service-directory/endpoints/create#--namespace)`=`NAMESPACE` `[--service](https://cloud.google.com/sdk/gcloud/reference/service-directory/endpoints/create#--service)`=`SERVICE`) [`[--address](https://cloud.google.com/sdk/gcloud/reference/service-directory/endpoints/create#--address)`=`ADDRESS`] [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/service-directory/endpoints/create#--annotations)`=[`KEY`=`VALUE`,…]] [`[--network](https://cloud.google.com/sdk/gcloud/reference/service-directory/endpoints/create#--network)`=`NETWORK`] [`[--port](https://cloud.google.com/sdk/gcloud/reference/service-directory/endpoints/create#--port)`=`PORT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/service-directory/endpoints/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates an endpoint.

**EXAMPLES**

: To create a Service Directory endpoint, run:

```
gcloud service-directory endpoints create my-endpoint --service=my-service --namespace=my-namespace --location=us-east1 --address=1.2.3.4 --port=5 --annotations=a=b,c=d --network=projects/123456789/locations/global/networks/default
```

**POSITIONAL ARGUMENTS**

: **Endpoint resource - The Service Directory endpoint to create. The endpoint id
must be 1-63 characters long and match the regular expression
`[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?` which means the first character
must be a lowercase letter, and all following characters must be a dash,
lowercase letter, or digit, except the last character, which cannot be a dash.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `endpoint` on the command line with a fully
specified name;
- set the property `core/project`.

This must be specified.

**`ENDPOINT`**:
ID of the endpoint or fully qualified identifier for the endpoint.
To set the `endpoint` attribute:

- provide the argument `endpoint` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The name of the region for the endpoint.
To set the `location` attribute:

- provide the argument `endpoint` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--namespace**:
The name of the namespace for the endpoint.
To set the `namespace` attribute:

- provide the argument `endpoint` on the command line with a fully
specified name;
- provide the argument `--namespace` on the command line.

**--service**:
The name of the service for the endpoint.
To set the `service` attribute:

- provide the argument `endpoint` on the command line with a fully
specified name;
- provide the argument `--service` on the command line.**

**FLAGS**

: **--address**:
IPv4 or IPv6 address of the endpoint. The default is empty string.

**--annotations**:
Annotations for the endpoint.
Annotations take the form of key/value string pairs. Keys are composed of an
optional prefix and a name segment, separated by a slash(/). Prefixes and names
must be composed of alphanumeric characters, dashes, and dots. Names may also
use underscores. There are no character restrictions on what may go into the
value of an annotation. The entire dictionary is limited to 512 characters,
spread across all key-value pairs.

**--network**:
Specifies the Google Compute Engine Network (VPC) of the Endpoint. Network and
Project existence is not checked. Example:
`projects/<PROJECT_NUM>/locations/global/networks/<NETWORK_NAME>`
The default is empty string.

**--port**:
Port that the endpoint is running on, must be in the range of [0, 65535]. The
default is 0.

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
gcloud alpha service-directory endpoints create
```

```
gcloud beta service-directory endpoints create
```