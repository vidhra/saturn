# gcloud edge-cloud networking routers remove-interface  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/remove-interface](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/remove-interface)*

**NAME**

: **gcloud edge-cloud networking routers remove-interface - remove an interface on a Distributed Cloud Edge Network router**

**SYNOPSIS**

: **`gcloud edge-cloud networking routers remove-interface` (`[ROUTER](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/remove-interface#ROUTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/remove-interface#--location)`=`LOCATION` `[--zone](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/remove-interface#--zone)`=`ZONE`) (`[--interface-name](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/remove-interface#--interface-name)`=`INTERFACE_NAME`     | `[--interface-names](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/remove-interface#--interface-names)`=[`INTERFACE_NAME`,…]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/remove-interface#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/remove-interface#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Remove an interface on a Distributed Cloud Edge Network router.

**EXAMPLES**

: To remove the interface 'my-int-r1' on Distributed Cloud Edge Network router
'my-router' in edge zone 'us-central1-edge-den1' , run:

```
gcloud edge-cloud networking routers remove-interface my-router --interface-name=my-int-r1 --location=us-central1 --zone=us-central1-edge-den1
```

**POSITIONAL ARGUMENTS**

: **Router resource - The router from which we remove an interface. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `router` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ROUTER`**:
ID of the router or fully qualified identifier for the router.
To set the `router` attribute:

- provide the argument `router` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Cloud location for the router.
To set the `location` attribute:

- provide the argument `router` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--zone**:
The zone of the router.
To set the `zone` attribute:

- provide the argument `router` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line.**

**REQUIRED FLAGS**

: **--interface-name**

**OPTIONAL FLAGS**

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

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cloud networking routers remove-interface
```