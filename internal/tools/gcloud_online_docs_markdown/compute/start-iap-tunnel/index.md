# gcloud compute start-iap-tunnel  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel](https://cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel)*

**NAME**

: **gcloud compute start-iap-tunnel - starts an IAP TCP forwarding tunnel**

**SYNOPSIS**

: **`gcloud compute start-iap-tunnel` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel#INSTANCE_NAME)` `[INSTANCE_PORT](https://cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel#INSTANCE_PORT)` [`[--iap-tunnel-disable-connection-check](https://cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel#--iap-tunnel-disable-connection-check)`] [`[--local-host-port](https://cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel#--local-host-port)`=`LOCAL_HOST_PORT`; default="localhost:0"] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel#--zone)`=`ZONE`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel#--network)`=`NETWORK` `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel#--region)`=`REGION` : `[--dest-group](https://cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel#--dest-group)`=`DEST_GROUP`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Starts a tunnel to Cloud Identity-Aware Proxy for TCP forwarding through which
another process can create a connection (eg. SSH, RDP) to a Google Compute
Engine instance.
To learn more, see the [IAP for TCP
forwarding documentation](https://cloud.google.com/iap/docs/tcp-forwarding-overview).
If the `--region` and `--network` flags are provided, then
an IP address or FQDN must be supplied instead of an instance name. This is most
useful for connecting to on-prem resources.

**EXAMPLES**

: To open a tunnel to the instances's RDP port on an arbitrary local port, run:

```
gcloud compute start-iap-tunnel my-instance 3389
```

To open a tunnel to the instance's RDP port on a specific local port, run:

```
gcloud compute start-iap-tunnel my-instance 3389 --local-host-port=localhost:3333
```

To use the IP address or FQDN of your remote VM (eg, for on-prem), you must also
specify the `--region` and `--network` flags:

```
gcloud compute start-iap-tunnel 10.1.2.3 3389 --region=us-central1 --network=default
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**`INSTANCE_PORT`**:
The name or number of the instance's port to connect to.

**FLAGS**

: **--iap-tunnel-disable-connection-check**:
Disables the immediate check of the connection.

**--local-host-port**:
`LOCAL_HOST:LOCAL_PORT` on which gcloud should bind and listen for
connections that should be tunneled.
`LOCAL_PORT` may be omitted, in which case it is treated as 0 and an
arbitrary unused local port is chosen. The colon also may be omitted in that
case.
If `LOCAL_PORT` is 0, an arbitrary unused local port is chosen.

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

**--network**:
Configures the VPC network to use when connecting via IP address or FQDN.

**--region**:
Configures the region to use when connecting via IP address or FQDN.

**--dest-group**:
Configures the destination group to use when connecting via IP address or FQDN.

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
gcloud alpha compute start-iap-tunnel
```

```
gcloud beta compute start-iap-tunnel
```