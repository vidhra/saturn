# gcloud service-directory services create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/service-directory/services/create](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/create)*

**NAME**

: **gcloud service-directory services create - creates a service**

**SYNOPSIS**

: **`gcloud service-directory services create` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/create#SERVICE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/create#--location)`=`LOCATION` `[--namespace](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/create#--namespace)`=`NAMESPACE`) [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/create#--annotations)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a service.

**EXAMPLES**

: To create a Service Directory service, run:

```
gcloud service-directory services create my-service --namespace=my-namespace --location=us-east1 --annotations=a=b,c=d
```

**POSITIONAL ARGUMENTS**

: **Service resource - The Service Directory service to create. The service id must
be 1-63 characters long and match the regular expression
`[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?` which means the first character
must be a lowercase letter, and all following characters must be a dash,
lowercase letter, or digit, except the last character, which cannot be a dash.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- set the property `core/project`.

This must be specified.

**`SERVICE`**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument `service` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The name of the region for the service.
To set the `location` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--namespace**:
The name of the namespace for the service.
To set the `namespace` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--namespace` on the command line.**

**FLAGS**

: **--annotations**:
Annotations for the service.
Annotations take the form of key/value string pairs. Keys are composed of an
optional prefix and a name segment, separated by a slash(/). Prefixes and names
must be composed of alphanumeric characters, dashes, and dots. Names may also
use underscores. There are no character restrictions on what may go into the
value of an annotation. The entire dictionary is limited to 2000 characters,
spread across all key-value pairs.

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
gcloud alpha service-directory services create
```

```
gcloud beta service-directory services create
```