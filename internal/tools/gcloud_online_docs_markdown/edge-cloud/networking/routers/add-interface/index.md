# gcloud edge-cloud networking routers add-interface  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-interface](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-interface)*

**NAME**

: **gcloud edge-cloud networking routers add-interface - add an interface to a Distributed Cloud Edge Network router**

**SYNOPSIS**

: **`gcloud edge-cloud networking routers add-interface` (`[ROUTER](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-interface#ROUTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-interface#--location)`=`LOCATION` `[--zone](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-interface#--zone)`=`ZONE`) `[--interface-name](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-interface#--interface-name)`=`INTERFACE_NAME` (`[--loopback-ip-addresses](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-interface#--loopback-ip-addresses)`=[`LOOPBACK_IP_ADDRESSES`,…]     | `[--subnetwork](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-interface#--subnetwork)`=`SUBNETWORK`     | `[--interconnect-attachment](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-interface#--interconnect-attachment)`=`INTERCONNECT_ATTACHMENT` `[--ip-address](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-interface#--ip-address)`=`IP_ADDRESS` `[--ip-mask-length](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-interface#--ip-mask-length)`=`IP_MASK_LENGTH`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-interface#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-interface#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an interface to a Distributed Cloud Edge Network router.

**EXAMPLES**

: To create and add a northbound interface for Distributed Cloud Edge Network
router 'my-router' in edge zone 'us-central1-edge-den1' , run:

```
gcloud edge-cloud networking routers add-interface my-router --interface-name=my-int-r1 --interconnect-attachment=my-link-attachment --ip-address=208.117.254.233 --ip-mask-length=31 --location=us-central1 --zone=us-central1-edge-den1
```

To create and add a southbound interface for Distributed Cloud Edge Network
router 'my-router' in edge zone 'us-central1-edge-den1', run:

```
gcloud edge-cloud networking routers add-interface my-router --interface-name=my-int-r2 --subnetwork=my-subnet --location=us-central1 --zone=us-central1-edge-den1
```

**POSITIONAL ARGUMENTS**

: **Router resource - The router to which we add an interface. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
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

: **--interface-name**:
The name of the interface being added.

**--loopback-ip-addresses**

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
gcloud alpha edge-cloud networking routers add-interface
```