# gcloud service-directory services delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/service-directory/services/delete](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/delete)*

**NAME**

: **gcloud service-directory services delete - deletes a service**

**SYNOPSIS**

: **`gcloud service-directory services delete` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/delete#SERVICE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/delete#--location)`=`LOCATION` `[--namespace](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/delete#--namespace)`=`NAMESPACE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/service-directory/services/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes a service.

**EXAMPLES**

: To delete a Service Directory service, run:

```
gcloud service-directory services delete my-service --namespace=my-namespace --location=us-east1
```

**POSITIONAL ARGUMENTS**

: **Service resource - The Service Directory service to delete. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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
gcloud alpha service-directory services delete
```

```
gcloud beta service-directory services delete
```