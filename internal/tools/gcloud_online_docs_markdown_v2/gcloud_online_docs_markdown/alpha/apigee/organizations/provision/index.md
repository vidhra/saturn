# gcloud alpha apigee organizations provision  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/provision](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/provision)*

**NAME**

: **gcloud alpha apigee organizations provision - provision an Apigee SaaS organization**

**SYNOPSIS**

: **`gcloud alpha apigee organizations provision` `[--authorized-network](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/provision#--authorized-network)`=`AUTHORIZED_NETWORK` [`[--analytics-region](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/provision#--analytics-region)`=`ANALYTICS_REGION`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/provision#--async)`] [`[--runtime-location](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/provision#--runtime-location)`=`RUNTIME_LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/provision#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Provision an Apigee SaaS organization.
`gcloud alpha apigee organizations provision` creates an Apigee
organization and populates it with the necessary child resources to be
immediately useable.
This is a long running operation and could take anywhere from 10 minutes to 1
hour to complete.
At the moment, only trial organizations are supported.

**EXAMPLES**

: To provision an organization for the active Cloud Platform project, attached to
a network named ``default`` run:

```
gcloud alpha apigee organizations provision --authorized-network=default
```

To provision an organization asynchronously and print only the name of the
launched operation, run:

```
gcloud alpha apigee organizations provision --authorized-network=default --async --format="value(name)"
```

To provision an organization for the project named
``my-proj``, with analytics and runtimes
located in ``us-central1``, run:

```
gcloud alpha apigee organizations provision --authorized-network=default --project=my-proj --analytics-region=us-central1 --runtime-location=us-central1-a
```

**REQUIRED FLAGS**

: **--authorized-network**:
Name of the network to which the provisioned organization should be attached.
This must be a VPC network peered through Service Networking. To get a list of
existing networks, run:

```
gcloud compute networks list
```

To check whether a network is peered through Service Networking, run:

```
gcloud services vpc-peerings list --network=NETWORK_NAME --service=servicenetworking.googleapis.com
```

To create a new network suitable for Apigee provisioning, choose a name for the
network and address range, and run:

```
gcloud compute networks create NETWORK_NAME --bgp-routing-mode=global --description='network for an Apigee trial'
gcloud compute addresses create ADDRESS_RANGE_NAME --global --prefix-length=16 --description="peering range for an Apigee trial" --network=NETWORK_NAME --purpose=vpc_peering
gcloud services vpc-peerings connect --service=servicenetworking.googleapis.com --network=NETWORK_NAME --ranges=ADDRESS_RANGE_NAME
```

**OPTIONAL FLAGS**

: **--analytics-region**:
Primary Cloud Platform region for analytics data storage. For valid values, see:
[https://docs.apigee.com/hybrid/latest/precog-provision](https://docs.apigee.com/hybrid/latest/precog-provision).
If unspecified, the default is ``us-west1``

**--async**:
If set, returns immediately and outputs a description of the long running
operation that was launched. Else, `gcloud alpha apigee organizations
provision` will block until the organization has been provisioned.
To monitor the operation once it's been launched, run `gcloud alpha apigee
operations describe OPERATION_NAME`.

**--runtime-location**:
Cloud Platform location for the runtime instance. For trial organizations, this
is a compute zone. To get a list of valid zones, run `[gcloud compute zones
list](https://cloud.google.com/sdk/gcloud/reference/compute/zones/list)`. If unspecified, the default is
``us-west1-a``.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist.