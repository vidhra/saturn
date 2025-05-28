# gcloud compute instances get-serial-port-output  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/get-serial-port-output](https://cloud.google.com/sdk/gcloud/reference/compute/instances/get-serial-port-output)*

**NAME**

: **gcloud compute instances get-serial-port-output - read output from a virtual machine instance's serial port**

**SYNOPSIS**

: **`gcloud compute instances get-serial-port-output` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instances/get-serial-port-output#INSTANCE_NAME)` [`[--port](https://cloud.google.com/sdk/gcloud/reference/compute/instances/get-serial-port-output#--port)`=`PORT`] [`[--start](https://cloud.google.com/sdk/gcloud/reference/compute/instances/get-serial-port-output#--start)`=`START`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/get-serial-port-output#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/get-serial-port-output#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud compute instances get-serial-port-output is used to get the output from a
Compute Engine virtual machine's serial port. The serial port output from the
virtual machine will be printed to standard output. This information can be
useful for diagnostic purposes.

**EXAMPLES**

: To get the output from instance's serial port, run:

```
gcloud compute instances get-serial-port-output example-instance --zone=us-central1-b
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--port**:
Instances can support up to four serial port outputs, numbered 1 through 4. By
default, this command will return the output of the first serial port. Setting
this flag will return the output of the requested serial port.

**--start**:
Specifies the byte index (zero-based) of the first byte you want returned. Use
this flag if you want to continue getting the output from a previous request
that was too long to return in one attempt. The last byte returned in a request
will be reported on STDERR.

**--zone**:
Zone of the instance to operate on. If not specified, you might be prompted to
select a zone (interactive mode only). `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` attempts to identify the
appropriate zone by searching for resources in your currently active project. If
the zone cannot be determined, `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with
all available Google Cloud Platform zones.
To avoid prompting when this flag is omitted, the user can set the
``compute/zone`` property:

```
gcloud config set compute/zone ZONE
```

A list of zones can be fetched by running:

```
gcloud compute zones list
```

To unset the property, run:

```
gcloud config unset compute/zone
```

Alternatively, the zone can be stored in the environment variable
``CLOUDSDK_COMPUTE_ZONE``.

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
gcloud alpha compute instances get-serial-port-output
```

```
gcloud beta compute instances get-serial-port-output
```