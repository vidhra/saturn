# gcloud compute service-attachments update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update)*

**NAME**

: **gcloud compute service-attachments update - update a Google Compute Engine service attachment**

**SYNOPSIS**

: **`gcloud compute service-attachments update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update#NAME)` [`[--connection-preference](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update#--connection-preference)`=`CONNECTION_PREFERENCE`] [`[--consumer-accept-list](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update#--consumer-accept-list)`=[`PROJECT_OR_NETWORK`=`LIMIT`,…]] [`[--consumer-reject-list](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update#--consumer-reject-list)`=[`REJECT_LIST`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update#--description)`=`DESCRIPTION`] [`[--[no-]enable-proxy-protocol](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update#--[no-]enable-proxy-protocol)`] [`[--nat-subnets](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update#--nat-subnets)`=`NAT_SUBNETS`,[`[NAT_SUBNETS](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update#NAT_SUBNETS)`,…]] [`[--nat-subnets-region](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update#--nat-subnets-region)`=`NAT_SUBNETS_REGION`] [`[--propagated-connection-limit](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update#--propagated-connection-limit)`=`PROPAGATED_CONNECTION_LIMIT`] [`[--[no-]reconcile-connections](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update#--[no-]reconcile-connections)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute service-attachments update` is used to update service
attachments. A service producer creates service attachments to make a service
available to consumers. Service consumers use Private Service Connect endpoints
to privately forward traffic to the service attachment.

**EXAMPLES**

: To update the connection policy of a service attachment to be ACCEPT_MANUAL,
run:

```
gcloud compute service-attachments update SERVICE_ATTACHMENT_NAME --region=us-central1 --connection-preference=ACCEPT_MANUAL
```

To update all supported fields of a service attachment, run:

```
gcloud compute service-attachments update SERVICE_ATTACHMENT_NAME --region=us-central1 --connection-preference=ACCEPT_AUTOMATIC --nat-subnets=MY_SUBNET1,MY_SUBNET2 --enable-proxy-protocol --consumer-reject-list=PROJECT_ID1,PROJECT_ID2 --consumer-accept-list=PROJECT_ID3=10,PROJECT_ID4=20
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the service attachment to update.

**FLAGS**

: **--connection-preference**:
This defines the service attachment's connection preference.
`CONNECTION_PREFERENCE` must be one of:

**`ACCEPT_AUTOMATIC`**:
Always accept connection requests from consumers automatically.

**`ACCEPT_MANUAL`**:
Only accept connection requests from consumers with the approval of the service
provider.

**--consumer-accept-list**:
Specifies which consumer projects or networks are allowed to connect to the
service attachment. Each project or network has a connection limit. A given
service attachment can manage connections at either the project or network
level. Therefore, both the accept and reject lists for a given service
attachment must contain either only projects or only networks.
For example, `--consumer-accept-list myProjectId1=20` accepts a
consumer project myProjectId1 with connection limit 20;
`--consumer-accept-list
projects/myProjectId1/global/networks/myNet1=20` accepts a consumer
network myNet1 with connection limit 20

- `PROJECT_OR_NETWORK` - Consumer project ID, project number or network
URL.
- `CONNECTION_LIMIT` - The maximum number of allowed connections.

**--consumer-reject-list**:
Specifies a comma separated list of projects or networks that are not allowed to
connect to this service attachment. The project can be specified using its
project ID or project number and the network can be specified using its URL. A
given service attachment can manage connections at either the project or network
level. Therefore, both the reject and accept lists for a given service
attachment must contain either only projects or only networks.

**--description**:
An optional, textual description for the service attachment.

**--[no-]enable-proxy-protocol**:
If True, then enable the proxy protocol which is for supplying client TCP/IP
address data in TCP connections that traverse proxies on their way to
destination servers. Use `--enable-proxy-protocol` to enable and
`--no-enable-proxy-protocol` to disable.

**--nat-subnets**:
The subnetworks provided by service producer to use for NAT

**--nat-subnets-region**:
Region of the subnetworks to operate on. If not specified, it will be set to the
region of the service attachment. Overrides the default
`compute/region` property value for this command invocation.

**--propagated-connection-limit**:
The number of consumer spokes that connected Private Service Connect endpoints
can be propagated to through Network Connectivity Center. This limit lets the
service producer limit how many propagated Private Service Connect connections
can be established to this service attachment from a single consumer.
If the connection preference of the service attachment is ACCEPT_MANUAL, the
limit applies to each project or network that is listed in the consumer accept
list. If the connection preference of the service attachment is
ACCEPT_AUTOMATIC, the limit applies to each project that contains a connected
endpoint.
If unspecified, the default propagated connection limit is 250.

**--[no-]reconcile-connections**:
Determines whether to apply changes to consumer accept or reject lists to
existing connections or only to new connections.
If false, existing endpoints with a connection status of ACCEPTED or REJECTED
are not updated.
If true, existing endpoints with a connection status of ACCEPTED or REJECTED are
updated based on the connection policy update. For example, if a project or
network is removed from the --consumer-accept-list and added to
--consumer-reject-list, all the endpoints in that project or network with the
ACCEPTED state are set to REJECTED.
Use `--reconcile-connections` to enable and
`--no-reconcile-connections` to disable.

**--region**:
Region of the service attachment to update. If not specified, you might be
prompted to select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

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
gcloud alpha compute service-attachments update
```

```
gcloud beta compute service-attachments update
```