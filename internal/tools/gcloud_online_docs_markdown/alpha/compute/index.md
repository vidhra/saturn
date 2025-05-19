# gcloud alpha compute  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute](https://cloud.google.com/sdk/gcloud/reference/alpha/compute)*

**NAME**

: **gcloud alpha compute - create and manipulate Compute Engine resources**

**SYNOPSIS**

: **`gcloud alpha compute` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/compute#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` The gcloud compute command group lets you create,
configure, and manipulate Compute Engine virtual machine (VM) instances.
With Compute Engine, you can create and run VMs on Google's infrastructure.
Compute Engine offers scale, performance, and value that lets you launch large
compute clusters on Google's infrastructure.
For more information about Compute Engine, see the [Compute Engine overview](https://cloud.google.com/compute/) and the [Compute Engine user
documentation](https://cloud.google.com/compute/docs/).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[accelerator-types](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/accelerator-types)`**:
`(ALPHA)` Read Compute Engine accelerator types.

**`[addresses](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses)`**:
`(ALPHA)` Read and manipulate Compute Engine addresses.

**`[advice](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/advice)`**:
`(ALPHA)` Provides recommendation on optimal allocation of resources
according to a flexible specifications.

**`[backend-buckets](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets)`**:
`(ALPHA)` Read and manipulate backend buckets.

**`[backend-services](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services)`**:
`(ALPHA)` List, create, and delete backend services.

**`[commitments](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments)`**:
`(ALPHA)` Manage Compute Engine commitments.

**`[diagnose](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/diagnose)`**:
`(ALPHA)` Debugging tools for Compute Engine virtual machine
instances.

**`[disk-settings](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disk-settings)`**:
`(ALPHA)` Read Compute Engine disk settings.

**`[disk-types](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disk-types)`**:
`(ALPHA)` Read Compute Engine virtual disk types.

**`[disks](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks)`**:
`(ALPHA)` Read and manipulate Compute Engine disks.

**`[external-vpn-gateways](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/external-vpn-gateways)`**:
`(ALPHA)` List, create, delete and update External VPN Gateways.

**`[firewall-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies)`**:
`(ALPHA)` Manage Compute Engine organization firewall policies.

**`[firewall-rules](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules)`**:
`(ALPHA)` List, create, update, and delete Compute Engine firewall
rules.

**`[forwarding-rules](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules)`**:
`(ALPHA)` Read and manipulate traffic forwarding rules to network
load balancers.

**`[future-reservations](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations)`**:
`(ALPHA)` Manage Compute Engine future reservations.

**`[health-checks](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks)`**:
`(ALPHA)` Read and manipulate health checks for load balanced
instances.

**`[http-health-checks](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/http-health-checks)`**:
`(ALPHA)` Read and manipulate HTTP health checks for load balanced
instances.

**`[https-health-checks](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks)`**:
`(ALPHA)` Read and manipulate HTTPS health checks for load balanced
instances.

**`[images](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images)`**:
`(ALPHA)` List, create, and delete Compute Engine images.

**`[instance-groups](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups)`**:
`(ALPHA)` Read and manipulate Compute Engine instance groups.

**`[instance-templates](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates)`**:
`(ALPHA)` Read and manipulate Compute Engine instances templates.

**`[instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances)`**:
`(ALPHA)` Read and manipulate Compute Engine virtual machine
instances.

**`[instant-snapshot-groups](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instant-snapshot-groups)`**:
`(ALPHA)` Create, list and delete Compute Engine instant snapshot
groups.

**`[instant-snapshots](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instant-snapshots)`**:
`(ALPHA)` Create, list and delete Compute Engine instant snapshots.

**`[interconnects](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects)`**:
`(ALPHA)` Read and manipulate Compute Engine interconnects.

**`[machine-images](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/machine-images)`**:
`(ALPHA)` Read and manage Compute Engine machine image resources.

**`[machine-types](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/machine-types)`**:
`(ALPHA)` Read Compute Engine virtual machine types.

**`[network-attachments](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/network-attachments)`**:
`(ALPHA)` Manage Compute Engine network attachment resources.

**`[network-edge-security-services](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/network-edge-security-services)`**:
`(ALPHA)` Read and manipulate network edge security services.

**`[network-endpoint-groups](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/network-endpoint-groups)`**:
`(ALPHA)` Read and manipulate Compute Engine network endpoint groups.

**`[network-firewall-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies)`**:
`(ALPHA)` Manage Compute Engine network firewall policies.

**`[network-profiles](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/network-profiles)`**:
`(ALPHA)` Read Compute Engine network profiles.

**`[networks](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/networks)`**:
`(ALPHA)` List, create, and delete Compute Engine networks.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/operations)`**:
`(ALPHA)` Read and manipulate Compute Engine operations.

**`[org-security-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/org-security-policies)`**:
`(ALPHA)` Manage Compute Engine organization security policies.

**`[os-config](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/os-config)`**:
`(ALPHA)` Manage OS Config tasks for Compute Engine VM instances.

**`[os-login](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/os-login)`**:
`(ALPHA)` Create and manipulate Compute Engine OS Login resources.

**`[packet-mirrorings](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/packet-mirrorings)`**:
`(ALPHA)` Manage Compute Engine packet mirroring resources.

**`[preview-features](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/preview-features)`**:
`(ALPHA)` Read and manipulate Compute Engine Preview Features.

**`[project-info](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/project-info)`**:
`(ALPHA)` Read and manipulate project-level data like quotas and
metadata.

**`[project-zonal-metadata](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/project-zonal-metadata)`**:
`(ALPHA)` Describe and update project zonal metadata.

**`[public-advertised-prefixes](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/public-advertised-prefixes)`**:
`(ALPHA)` Manage public advertised prefix resources.

**`[public-delegated-prefixes](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/public-delegated-prefixes)`**:
`(ALPHA)` Manage public delegated prefix resources.

**`[queued-resources](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/queued-resources)`**:
`(ALPHA)` Manage queued resources.

**`[regions](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/regions)`**:
`(ALPHA)` List Compute Engine regions.

**`[reservations](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/reservations)`**:
`(ALPHA)` Manage Compute Engine reservations.

**`[resource-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/resource-policies)`**:
`(ALPHA)` Manage Compute Engine Resource Policies.

**`[routers](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/routers)`**:
`(ALPHA)` List, create, and delete Compute Engine routers.

**`[routes](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/routes)`**:
`(ALPHA)` Read and manipulate routes.

**`[security-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/security-policies)`**:
`(ALPHA)` Read and manipulate Cloud Armor security policies.

**`[service-attachments](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/service-attachments)`**:
`(ALPHA)` Manage Compute Engine service attachment resources.

**`[shared-vpc](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/shared-vpc)`**:
`(ALPHA)` Configure shared VPC.

**`[snapshot-settings](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshot-settings)`**:
`(ALPHA)` Describe and update Compute Engine snapshot settings.

**`[snapshots](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshots)`**:
`(ALPHA)` List, describe, and delete Compute Engine snapshots.

**`[sole-tenancy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/sole-tenancy)`**:
`(ALPHA)` Read and manage Compute Engine sole-tenancy resources.

**`[ssl-certificates](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/ssl-certificates)`**:
`(ALPHA)` List, create, and delete Compute Engine SSL certificate
resources.

**`[ssl-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/ssl-policies)`**:
`(ALPHA)` List, create, delete and update Compute Engine SSL
policies.

**`[storage-pool-types](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/storage-pool-types)`**:
`(ALPHA)` Read storage pool types.

**`[storage-pools](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/storage-pools)`**:
`(ALPHA)` Read and manipulate storage pools.

**`[target-grpc-proxies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/target-grpc-proxies)`**:
`(ALPHA)` Manage Compute Engine target gRPC proxy resources.

**`[target-http-proxies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/target-http-proxies)`**:
`(ALPHA)` List, create, and delete target HTTP proxies.

**`[target-https-proxies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/target-https-proxies)`**:
`(ALPHA)` List, create, and delete target HTTPS proxies.

**`[target-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/target-instances)`**:
`(ALPHA)` Read and manipulate Compute Engine virtual target
instances.

**`[target-pools](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/target-pools)`**:
`(ALPHA)` Control Compute Engine target pools for network load
balancing.

**`[target-ssl-proxies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/target-ssl-proxies)`**:
`(ALPHA)` List, create, and delete target SSL proxies.

**`[target-tcp-proxies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/target-tcp-proxies)`**:
`(ALPHA)` List, create, and delete target TCP proxies.

**`[target-vpn-gateways](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/target-vpn-gateways)`**:
`(ALPHA)` Read and manipulate classic VPN gateways.

**`[tpus](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus)`**:
`(ALPHA)` List, create, and delete Cloud TPUs.

**`[url-maps](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/url-maps)`**:
`(ALPHA)` List, create, and delete URL maps.

**`[vpn-gateways](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/vpn-gateways)`**:
`(ALPHA)` read and manipulate Highly Available VPN Gateways.

**`[vpn-tunnels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/vpn-tunnels)`**:
`(ALPHA)` Read and manipulate Compute Engine VPN tunnels.

**`[zones](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/zones)`**:
`(ALPHA)` List Compute Engine zones.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[config-ssh](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/config-ssh)`**:
`(ALPHA)` Populate SSH config files with Host entries from each
instance.

**`[connect-to-serial-port](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/connect-to-serial-port)`**:
`(ALPHA)` Connect to the serial port of an instance.

**`[copy-files](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/copy-files)`**:
`(ALPHA)` Copy files to and from Google Compute Engine virtual
machines via scp.

**`[reset-windows-password](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/reset-windows-password)`**:
`(ALPHA)` Reset and return a password for a Windows machine instance.

**`[scp](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/scp)`**:
`(ALPHA)` Copy files to and from Google Compute Engine virtual
machines via scp.

**`[sign-url](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/sign-url)`**:
`(ALPHA)` Sign specified URL for use with Cloud CDN Signed URLs.

**`[ssh](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/ssh)`**:
`(ALPHA)` SSH into a virtual machine instance.

**`[start-iap-tunnel](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/start-iap-tunnel)`**:
`(ALPHA)` Starts an IAP TCP forwarding tunnel.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute
```

```
gcloud beta compute
```